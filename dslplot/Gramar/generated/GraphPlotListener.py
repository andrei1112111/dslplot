# Generated from GraphPlot.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .GraphPlotParser import GraphPlotParser
else:
    from GraphPlotParser import GraphPlotParser

# This class defines a complete listener for a parse tree produced by GraphPlotParser.
class GraphPlotListener(ParseTreeListener):

    # Enter a parse tree produced by GraphPlotParser#parse.
    def enterParse(self, ctx:GraphPlotParser.ParseContext):
        pass

    # Exit a parse tree produced by GraphPlotParser#parse.
    def exitParse(self, ctx:GraphPlotParser.ParseContext):
        pass


    # Enter a parse tree produced by GraphPlotParser#statement.
    def enterStatement(self, ctx:GraphPlotParser.StatementContext):
        pass

    # Exit a parse tree produced by GraphPlotParser#statement.
    def exitStatement(self, ctx:GraphPlotParser.StatementContext):
        pass


    # Enter a parse tree produced by GraphPlotParser#plotStatement.
    def enterPlotStatement(self, ctx:GraphPlotParser.PlotStatementContext):
        pass

    # Exit a parse tree produced by GraphPlotParser#plotStatement.
    def exitPlotStatement(self, ctx:GraphPlotParser.PlotStatementContext):
        pass


    # Enter a parse tree produced by GraphPlotParser#configStatement.
    def enterConfigStatement(self, ctx:GraphPlotParser.ConfigStatementContext):
        pass

    # Exit a parse tree produced by GraphPlotParser#configStatement.
    def exitConfigStatement(self, ctx:GraphPlotParser.ConfigStatementContext):
        pass


    # Enter a parse tree produced by GraphPlotParser#labelStatement.
    def enterLabelStatement(self, ctx:GraphPlotParser.LabelStatementContext):
        pass

    # Exit a parse tree produced by GraphPlotParser#labelStatement.
    def exitLabelStatement(self, ctx:GraphPlotParser.LabelStatementContext):
        pass


    # Enter a parse tree produced by GraphPlotParser#styleStatement.
    def enterStyleStatement(self, ctx:GraphPlotParser.StyleStatementContext):
        pass

    # Exit a parse tree produced by GraphPlotParser#styleStatement.
    def exitStyleStatement(self, ctx:GraphPlotParser.StyleStatementContext):
        pass


    # Enter a parse tree produced by GraphPlotParser#scaleStatement.
    def enterScaleStatement(self, ctx:GraphPlotParser.ScaleStatementContext):
        pass

    # Exit a parse tree produced by GraphPlotParser#scaleStatement.
    def exitScaleStatement(self, ctx:GraphPlotParser.ScaleStatementContext):
        pass


    # Enter a parse tree produced by GraphPlotParser#subplotStatement.
    def enterSubplotStatement(self, ctx:GraphPlotParser.SubplotStatementContext):
        pass

    # Exit a parse tree produced by GraphPlotParser#subplotStatement.
    def exitSubplotStatement(self, ctx:GraphPlotParser.SubplotStatementContext):
        pass


    # Enter a parse tree produced by GraphPlotParser#saveStatement.
    def enterSaveStatement(self, ctx:GraphPlotParser.SaveStatementContext):
        pass

    # Exit a parse tree produced by GraphPlotParser#saveStatement.
    def exitSaveStatement(self, ctx:GraphPlotParser.SaveStatementContext):
        pass


    # Enter a parse tree produced by GraphPlotParser#dimension.
    def enterDimension(self, ctx:GraphPlotParser.DimensionContext):
        pass

    # Exit a parse tree produced by GraphPlotParser#dimension.
    def exitDimension(self, ctx:GraphPlotParser.DimensionContext):
        pass


    # Enter a parse tree produced by GraphPlotParser#chartType.
    def enterChartType(self, ctx:GraphPlotParser.ChartTypeContext):
        pass

    # Exit a parse tree produced by GraphPlotParser#chartType.
    def exitChartType(self, ctx:GraphPlotParser.ChartTypeContext):
        pass


    # Enter a parse tree produced by GraphPlotParser#dataSpec.
    def enterDataSpec(self, ctx:GraphPlotParser.DataSpecContext):
        pass

    # Exit a parse tree produced by GraphPlotParser#dataSpec.
    def exitDataSpec(self, ctx:GraphPlotParser.DataSpecContext):
        pass


    # Enter a parse tree produced by GraphPlotParser#plotOptions.
    def enterPlotOptions(self, ctx:GraphPlotParser.PlotOptionsContext):
        pass

    # Exit a parse tree produced by GraphPlotParser#plotOptions.
    def exitPlotOptions(self, ctx:GraphPlotParser.PlotOptionsContext):
        pass


    # Enter a parse tree produced by GraphPlotParser#option.
    def enterOption(self, ctx:GraphPlotParser.OptionContext):
        pass

    # Exit a parse tree produced by GraphPlotParser#option.
    def exitOption(self, ctx:GraphPlotParser.OptionContext):
        pass


    # Enter a parse tree produced by GraphPlotParser#value.
    def enterValue(self, ctx:GraphPlotParser.ValueContext):
        pass

    # Exit a parse tree produced by GraphPlotParser#value.
    def exitValue(self, ctx:GraphPlotParser.ValueContext):
        pass


    # Enter a parse tree produced by GraphPlotParser#axis.
    def enterAxis(self, ctx:GraphPlotParser.AxisContext):
        pass

    # Exit a parse tree produced by GraphPlotParser#axis.
    def exitAxis(self, ctx:GraphPlotParser.AxisContext):
        pass


    # Enter a parse tree produced by GraphPlotParser#scaleType.
    def enterScaleType(self, ctx:GraphPlotParser.ScaleTypeContext):
        pass

    # Exit a parse tree produced by GraphPlotParser#scaleType.
    def exitScaleType(self, ctx:GraphPlotParser.ScaleTypeContext):
        pass


    # Enter a parse tree produced by GraphPlotParser#gridSize.
    def enterGridSize(self, ctx:GraphPlotParser.GridSizeContext):
        pass

    # Exit a parse tree produced by GraphPlotParser#gridSize.
    def exitGridSize(self, ctx:GraphPlotParser.GridSizeContext):
        pass


    # Enter a parse tree produced by GraphPlotParser#position.
    def enterPosition(self, ctx:GraphPlotParser.PositionContext):
        pass

    # Exit a parse tree produced by GraphPlotParser#position.
    def exitPosition(self, ctx:GraphPlotParser.PositionContext):
        pass


    # Enter a parse tree produced by GraphPlotParser#labelType.
    def enterLabelType(self, ctx:GraphPlotParser.LabelTypeContext):
        pass

    # Exit a parse tree produced by GraphPlotParser#labelType.
    def exitLabelType(self, ctx:GraphPlotParser.LabelTypeContext):
        pass


    # Enter a parse tree produced by GraphPlotParser#configKey.
    def enterConfigKey(self, ctx:GraphPlotParser.ConfigKeyContext):
        pass

    # Exit a parse tree produced by GraphPlotParser#configKey.
    def exitConfigKey(self, ctx:GraphPlotParser.ConfigKeyContext):
        pass


    # Enter a parse tree produced by GraphPlotParser#configValue.
    def enterConfigValue(self, ctx:GraphPlotParser.ConfigValueContext):
        pass

    # Exit a parse tree produced by GraphPlotParser#configValue.
    def exitConfigValue(self, ctx:GraphPlotParser.ConfigValueContext):
        pass


    # Enter a parse tree produced by GraphPlotParser#styleKey.
    def enterStyleKey(self, ctx:GraphPlotParser.StyleKeyContext):
        pass

    # Exit a parse tree produced by GraphPlotParser#styleKey.
    def exitStyleKey(self, ctx:GraphPlotParser.StyleKeyContext):
        pass


    # Enter a parse tree produced by GraphPlotParser#styleValue.
    def enterStyleValue(self, ctx:GraphPlotParser.StyleValueContext):
        pass

    # Exit a parse tree produced by GraphPlotParser#styleValue.
    def exitStyleValue(self, ctx:GraphPlotParser.StyleValueContext):
        pass



del GraphPlotParser