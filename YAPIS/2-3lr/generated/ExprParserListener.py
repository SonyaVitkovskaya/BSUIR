# Generated from ExprParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete listener for a parse tree produced by ExprParser.
class ExprParserListener(ParseTreeListener):

    # Enter a parse tree produced by ExprParser#types.
    def enterTypes(self, ctx:ExprParser.TypesContext):
        pass

    # Exit a parse tree produced by ExprParser#types.
    def exitTypes(self, ctx:ExprParser.TypesContext):
        pass


    # Enter a parse tree produced by ExprParser#operation.
    def enterOperation(self, ctx:ExprParser.OperationContext):
        pass

    # Exit a parse tree produced by ExprParser#operation.
    def exitOperation(self, ctx:ExprParser.OperationContext):
        pass


    # Enter a parse tree produced by ExprParser#anoun.
    def enterAnoun(self, ctx:ExprParser.AnounContext):
        pass

    # Exit a parse tree produced by ExprParser#anoun.
    def exitAnoun(self, ctx:ExprParser.AnounContext):
        pass


    # Enter a parse tree produced by ExprParser#node.
    def enterNode(self, ctx:ExprParser.NodeContext):
        pass

    # Exit a parse tree produced by ExprParser#node.
    def exitNode(self, ctx:ExprParser.NodeContext):
        pass


    # Enter a parse tree produced by ExprParser#arc.
    def enterArc(self, ctx:ExprParser.ArcContext):
        pass

    # Exit a parse tree produced by ExprParser#arc.
    def exitArc(self, ctx:ExprParser.ArcContext):
        pass


    # Enter a parse tree produced by ExprParser#program.
    def enterProgram(self, ctx:ExprParser.ProgramContext):
        pass

    # Exit a parse tree produced by ExprParser#program.
    def exitProgram(self, ctx:ExprParser.ProgramContext):
        pass


    # Enter a parse tree produced by ExprParser#stat.
    def enterStat(self, ctx:ExprParser.StatContext):
        pass

    # Exit a parse tree produced by ExprParser#stat.
    def exitStat(self, ctx:ExprParser.StatContext):
        pass


    # Enter a parse tree produced by ExprParser#def.
    def enterDef(self, ctx:ExprParser.DefContext):
        pass

    # Exit a parse tree produced by ExprParser#def.
    def exitDef(self, ctx:ExprParser.DefContext):
        pass


    # Enter a parse tree produced by ExprParser#expr.
    def enterExpr(self, ctx:ExprParser.ExprContext):
        pass

    # Exit a parse tree produced by ExprParser#expr.
    def exitExpr(self, ctx:ExprParser.ExprContext):
        pass


    # Enter a parse tree produced by ExprParser#cicle.
    def enterCicle(self, ctx:ExprParser.CicleContext):
        pass

    # Exit a parse tree produced by ExprParser#cicle.
    def exitCicle(self, ctx:ExprParser.CicleContext):
        pass


    # Enter a parse tree produced by ExprParser#condition.
    def enterCondition(self, ctx:ExprParser.ConditionContext):
        pass

    # Exit a parse tree produced by ExprParser#condition.
    def exitCondition(self, ctx:ExprParser.ConditionContext):
        pass


    # Enter a parse tree produced by ExprParser#func.
    def enterFunc(self, ctx:ExprParser.FuncContext):
        pass

    # Exit a parse tree produced by ExprParser#func.
    def exitFunc(self, ctx:ExprParser.FuncContext):
        pass



del ExprParser