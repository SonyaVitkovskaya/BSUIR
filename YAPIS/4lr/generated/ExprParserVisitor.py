# Generated from ExprParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete generic visitor for a parse tree produced by ExprParser.

class ExprParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ExprParser#types.
    def visitTypes(self, ctx:ExprParser.TypesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#operation.
    def visitOperation(self, ctx:ExprParser.OperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#anoun.
    def visitAnoun(self, ctx:ExprParser.AnounContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#node.
    def visitNode(self, ctx:ExprParser.NodeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#arc.
    def visitArc(self, ctx:ExprParser.ArcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#program.
    def visitProgram(self, ctx:ExprParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#stat.
    def visitStat(self, ctx:ExprParser.StatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#def.
    def visitDef(self, ctx:ExprParser.DefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#expr.
    def visitExpr(self, ctx:ExprParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#cicle.
    def visitCicle(self, ctx:ExprParser.CicleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#condition.
    def visitCondition(self, ctx:ExprParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#or_func.
    def visitOr_func(self, ctx:ExprParser.Or_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#func.
    def visitFunc(self, ctx:ExprParser.FuncContext):
        return self.visitChildren(ctx)



del ExprParser