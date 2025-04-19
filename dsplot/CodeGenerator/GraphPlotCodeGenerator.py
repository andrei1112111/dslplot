from dsplot.Gramar.generated.GraphPlotParser import GraphPlotParser
from dsplot.Gramar.generated.GraphPlotVisitor import GraphPlotVisitor


REQUIRED_PACKAGES = {
    ("matplotlib.pyplot", "plt"),
    ("seaborn", "sns")
}


class CodeGenerator(GraphPlotVisitor):
    def __init__(self):
        self.code = []
        self.imports = ["import matplotlib.pyplot as plt", "import seaborn as sns"]
        self.subplots = False
        self.subplot_rows = 1
        self.subplot_cols = 1
        self.current_subplot = (1, 1)
        self.log_scale = {'x': False, 'y': False}
        self.theme = None

    def generate(self):
        imports = '\n'.join(sorted(self.imports))
        body = '\n'.join(self.code)
        return f"{imports}\n\n{body}\nplt.tight_layout()\n"

    def visitParse(self, ctx: GraphPlotParser.ParseContext):
        for stmt in ctx.statement():
            self.visit(stmt)
        return self.generate()

    def visitPlotStatement(self, ctx: GraphPlotParser.PlotStatementContext):
        chart = ctx.chartType().getText().lower()
        args = [i.getText() for i in ctx.dataSpec().IDENTIFIER()]
        opts = {}

        if ctx.plotOptions():
            for opt in ctx.plotOptions().option():
                key = opt.IDENTIFIER().getText()
                val = opt.value().getText()
                opts[key] = val

        call = ""

        if chart == "line":
            call = f"plt.plot({', '.join(args)}"
        elif chart == "scatter":
            call = f"plt.scatter({', '.join(args)}"
        elif chart == "bar":
            call = f"plt.bar({', '.join(args)}"
        elif chart == "hist":
            call = f"plt.hist({args[0]}"
        elif chart == "pie":
            call = f"plt.pie({args[0]}"
        elif chart == "box":
            call = f"plt.boxplot({args[0]}"
        else:
            call = "# Unsupported chart type"

        if opts:
            call += ", " + ", ".join(f"{k}={v}" for k, v in opts.items())

        call += ")"
        self.code.append(call)

        # apply log scale if needed
        if self.log_scale['x']:
            self.code.append("plt.xscale('log')")
        if self.log_scale['y']:
            self.code.append("plt.yscale('log')")

        return None

    def visitLabelStatement(self, ctx: GraphPlotParser.LabelStatementContext):
        label_type = ctx.labelType().getText().lower()
        text = ctx.STRING().getText()
        if label_type == "title":
            self.code.append(f"plt.title({text})")
        elif label_type == "x":
            self.code.append(f"plt.xlabel({text})")
        elif label_type == "y":
            self.code.append(f"plt.ylabel({text})")
        return None

    def visitConfigStatement(self, ctx: GraphPlotParser.ConfigStatementContext):
        key = ctx.configKey().getText()
        val = ctx.configValue().getText()

        if key == "FIGSIZE":
            self.code.insert(0, f"plt.figure(figsize=({val}, {val}))")
        elif key == "THEME":
            self.code.insert(0, f"sns.set_theme(style={val})")
        elif key == "GRID":
            self.code.append(f"plt.grid({val})")

        return None

    def visitStyleStatement(self, ctx: GraphPlotParser.StyleStatementContext):
        # Not implemented yet: could affect global seaborn/pyplot styles
        return None

    def visitScaleStatement(self, ctx: GraphPlotParser.ScaleStatementContext):
        axis = ctx.axis().getText().lower()
        scale = ctx.scaleType().getText().lower()
        self.log_scale[axis] = (scale == "log")
        return None

    def visitSaveStatement(self, ctx: GraphPlotParser.SaveStatementContext):
        filename = ctx.STRING().getText()
        self.code.append(f"plt.savefig({filename})")
        return None

    def visitSubplotStatement(self, ctx: GraphPlotParser.SubplotStatementContext):
        if ctx.getChild(1).getText() == "GRID":
            rows = int(ctx.gridSize().NUMBER(0).getText())
            cols = int(ctx.gridSize().NUMBER(1).getText())
            self.subplots = True
            self.subplot_rows = rows
            self.subplot_cols = cols
            self.code.insert(0, f"fig, axs = plt.subplots({rows}, {cols})")
        elif ctx.getChild(1).getText() == "SELECT":
            row = int(ctx.position().NUMBER(0).getText()) - 1
            col = int(ctx.position().NUMBER(1).getText()) - 1
            self.code.append(f"plt.sca(axs[{row},{col}])")

        return None
