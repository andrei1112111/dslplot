# Generated from GraphPlot.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .GraphPlotParser import GraphPlotParser
else:
    from GraphPlotParser import GraphPlotParser

# This class defines a complete generic visitor for a parse tree produced by GraphPlotParser.

class GraphPlotVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by GraphPlotParser#parse.
    def visitParse(self, ctx:GraphPlotParser.ParseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphPlotParser#statement.
    def visitStatement(self, ctx:GraphPlotParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphPlotParser#plotStatement.
    def visitPlotStatement(self, ctx:GraphPlotParser.PlotStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphPlotParser#configStatement.
    def visitConfigStatement(self, ctx:GraphPlotParser.ConfigStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphPlotParser#labelStatement.
    def visitLabelStatement(self, ctx:GraphPlotParser.LabelStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphPlotParser#styleStatement.
    def visitStyleStatement(self, ctx:GraphPlotParser.StyleStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphPlotParser#scaleStatement.
    def visitScaleStatement(self, ctx:GraphPlotParser.ScaleStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphPlotParser#subplotStatement.
    def visitSubplotStatement(self, ctx:GraphPlotParser.SubplotStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphPlotParser#saveStatement.
    def visitSaveStatement(self, ctx:GraphPlotParser.SaveStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphPlotParser#dimension.
    def visitDimension(self, ctx:GraphPlotParser.DimensionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphPlotParser#chartType.
    def visitChartType(self, ctx:GraphPlotParser.ChartTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphPlotParser#dataSpec.
    def visitDataSpec(self, ctx:GraphPlotParser.DataSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphPlotParser#plotOptions.
    def visitPlotOptions(self, ctx:GraphPlotParser.PlotOptionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphPlotParser#option.
    def visitOption(self, ctx:GraphPlotParser.OptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphPlotParser#value.
    def visitValue(self, ctx:GraphPlotParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphPlotParser#axis.
    def visitAxis(self, ctx:GraphPlotParser.AxisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphPlotParser#scaleType.
    def visitScaleType(self, ctx:GraphPlotParser.ScaleTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphPlotParser#gridSize.
    def visitGridSize(self, ctx:GraphPlotParser.GridSizeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphPlotParser#position.
    def visitPosition(self, ctx:GraphPlotParser.PositionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphPlotParser#labelType.
    def visitLabelType(self, ctx:GraphPlotParser.LabelTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphPlotParser#configKey.
    def visitConfigKey(self, ctx:GraphPlotParser.ConfigKeyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphPlotParser#configValue.
    def visitConfigValue(self, ctx:GraphPlotParser.ConfigValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphPlotParser#styleKey.
    def visitStyleKey(self, ctx:GraphPlotParser.StyleKeyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GraphPlotParser#styleValue.
    def visitStyleValue(self, ctx:GraphPlotParser.StyleValueContext):
        return self.visitChildren(ctx)



del GraphPlotParser