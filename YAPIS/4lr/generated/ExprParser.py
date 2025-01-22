# Generated from ExprParser.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,43,303,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,1,0,1,0,
        1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        5,2,61,8,2,10,2,12,2,64,9,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,
        74,8,2,10,2,12,2,77,9,2,1,2,1,2,1,2,3,2,82,8,2,1,3,1,3,1,4,1,4,1,
        4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,96,8,4,1,5,1,5,5,5,100,8,5,10,
        5,12,5,103,9,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,
        6,1,6,1,6,1,6,3,6,121,8,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,5,
        7,132,8,7,10,7,12,7,135,9,7,1,7,1,7,1,7,5,7,140,8,7,10,7,12,7,143,
        9,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,157,8,8,
        1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,172,8,8,
        1,8,1,8,3,8,176,8,8,1,8,5,8,179,8,8,10,8,12,8,182,9,8,1,9,1,9,1,
        9,1,9,1,9,1,9,5,9,190,8,9,10,9,12,9,193,9,9,1,9,1,9,1,9,1,9,1,9,
        1,9,1,9,3,9,202,8,9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,210,8,9,1,9,1,9,
        3,9,214,8,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,5,9,224,8,9,10,9,12,
        9,227,9,9,1,9,1,9,3,9,231,8,9,1,10,1,10,1,10,1,10,1,10,1,10,5,10,
        239,8,10,10,10,12,10,242,9,10,1,10,1,10,1,10,1,10,5,10,248,8,10,
        10,10,12,10,251,9,10,1,10,3,10,254,8,10,1,10,1,10,1,10,1,10,1,10,
        1,10,1,10,1,10,1,10,5,10,265,8,10,10,10,12,10,268,9,10,5,10,270,
        8,10,10,10,12,10,273,9,10,1,10,3,10,276,8,10,1,11,1,11,1,12,1,12,
        1,12,1,12,1,12,5,12,285,8,12,10,12,12,12,288,9,12,1,12,1,12,1,12,
        1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,3,12,301,8,12,1,12,0,1,16,
        13,0,2,4,6,8,10,12,14,16,18,20,22,24,0,5,2,0,1,3,6,6,1,0,17,21,1,
        0,32,33,2,0,25,25,29,29,1,0,38,40,331,0,26,1,0,0,0,2,28,1,0,0,0,
        4,81,1,0,0,0,6,83,1,0,0,0,8,95,1,0,0,0,10,101,1,0,0,0,12,120,1,0,
        0,0,14,122,1,0,0,0,16,156,1,0,0,0,18,230,1,0,0,0,20,275,1,0,0,0,
        22,277,1,0,0,0,24,300,1,0,0,0,26,27,7,0,0,0,27,1,1,0,0,0,28,29,7,
        1,0,0,29,3,1,0,0,0,30,31,3,0,0,0,31,32,5,42,0,0,32,82,1,0,0,0,33,
        34,5,6,0,0,34,35,5,42,0,0,35,36,5,25,0,0,36,82,5,41,0,0,37,38,5,
        2,0,0,38,39,5,42,0,0,39,40,5,25,0,0,40,82,3,16,8,0,41,42,5,3,0,0,
        42,43,5,42,0,0,43,44,5,25,0,0,44,45,5,32,0,0,45,46,3,6,3,0,46,47,
        5,26,0,0,47,48,3,6,3,0,48,49,5,33,0,0,49,82,1,0,0,0,50,51,5,2,0,
        0,51,52,5,42,0,0,52,53,5,25,0,0,53,54,5,30,0,0,54,55,5,4,0,0,55,
        56,5,28,0,0,56,57,5,34,0,0,57,62,3,6,3,0,58,59,5,26,0,0,59,61,3,
        6,3,0,60,58,1,0,0,0,61,64,1,0,0,0,62,60,1,0,0,0,62,63,1,0,0,0,63,
        65,1,0,0,0,64,62,1,0,0,0,65,66,5,35,0,0,66,67,5,26,0,0,67,68,5,5,
        0,0,68,69,5,28,0,0,69,70,5,34,0,0,70,75,3,8,4,0,71,72,5,26,0,0,72,
        74,3,8,4,0,73,71,1,0,0,0,74,77,1,0,0,0,75,73,1,0,0,0,75,76,1,0,0,
        0,76,78,1,0,0,0,77,75,1,0,0,0,78,79,5,35,0,0,79,80,5,31,0,0,80,82,
        1,0,0,0,81,30,1,0,0,0,81,33,1,0,0,0,81,37,1,0,0,0,81,41,1,0,0,0,
        81,50,1,0,0,0,82,5,1,0,0,0,83,84,5,42,0,0,84,7,1,0,0,0,85,96,5,42,
        0,0,86,87,5,3,0,0,87,88,5,42,0,0,88,89,5,25,0,0,89,90,5,32,0,0,90,
        91,3,6,3,0,91,92,5,26,0,0,92,93,3,6,3,0,93,94,5,33,0,0,94,96,1,0,
        0,0,95,85,1,0,0,0,95,86,1,0,0,0,96,9,1,0,0,0,97,100,3,12,6,0,98,
        100,3,4,2,0,99,97,1,0,0,0,99,98,1,0,0,0,100,103,1,0,0,0,101,99,1,
        0,0,0,101,102,1,0,0,0,102,104,1,0,0,0,103,101,1,0,0,0,104,105,5,
        0,0,1,105,11,1,0,0,0,106,107,5,42,0,0,107,108,5,25,0,0,108,109,3,
        16,8,0,109,110,5,27,0,0,110,121,1,0,0,0,111,112,3,16,8,0,112,113,
        5,27,0,0,113,121,1,0,0,0,114,115,3,4,2,0,115,116,5,27,0,0,116,121,
        1,0,0,0,117,121,3,18,9,0,118,121,3,20,10,0,119,121,3,14,7,0,120,
        106,1,0,0,0,120,111,1,0,0,0,120,114,1,0,0,0,120,117,1,0,0,0,120,
        118,1,0,0,0,120,119,1,0,0,0,121,13,1,0,0,0,122,123,5,16,0,0,123,
        124,5,42,0,0,124,125,5,34,0,0,125,126,3,0,0,0,126,133,5,42,0,0,127,
        128,5,26,0,0,128,129,3,0,0,0,129,130,5,42,0,0,130,132,1,0,0,0,131,
        127,1,0,0,0,132,135,1,0,0,0,133,131,1,0,0,0,133,134,1,0,0,0,134,
        136,1,0,0,0,135,133,1,0,0,0,136,137,5,35,0,0,137,141,5,36,0,0,138,
        140,3,12,6,0,139,138,1,0,0,0,140,143,1,0,0,0,141,139,1,0,0,0,141,
        142,1,0,0,0,142,144,1,0,0,0,143,141,1,0,0,0,144,145,5,37,0,0,145,
        15,1,0,0,0,146,147,6,8,-1,0,147,157,3,24,12,0,148,149,5,24,0,0,149,
        157,3,16,8,9,150,157,5,42,0,0,151,157,5,41,0,0,152,157,5,13,0,0,
        153,157,5,15,0,0,154,155,5,14,0,0,155,157,3,16,8,1,156,146,1,0,0,
        0,156,148,1,0,0,0,156,150,1,0,0,0,156,151,1,0,0,0,156,152,1,0,0,
        0,156,153,1,0,0,0,156,154,1,0,0,0,157,180,1,0,0,0,158,159,10,10,
        0,0,159,160,3,2,1,0,160,161,3,16,8,11,161,179,1,0,0,0,162,163,10,
        8,0,0,163,164,5,22,0,0,164,179,3,16,8,9,165,166,10,7,0,0,166,167,
        5,23,0,0,167,179,3,16,8,8,168,175,10,6,0,0,169,171,7,2,0,0,170,172,
        5,25,0,0,171,170,1,0,0,0,171,172,1,0,0,0,172,176,1,0,0,0,173,174,
        7,3,0,0,174,176,5,25,0,0,175,169,1,0,0,0,175,173,1,0,0,0,176,177,
        1,0,0,0,177,179,3,16,8,7,178,158,1,0,0,0,178,162,1,0,0,0,178,165,
        1,0,0,0,178,168,1,0,0,0,179,182,1,0,0,0,180,178,1,0,0,0,180,181,
        1,0,0,0,181,17,1,0,0,0,182,180,1,0,0,0,183,184,5,8,0,0,184,185,5,
        34,0,0,185,186,3,16,8,0,186,187,5,35,0,0,187,191,5,36,0,0,188,190,
        3,12,6,0,189,188,1,0,0,0,190,193,1,0,0,0,191,189,1,0,0,0,191,192,
        1,0,0,0,192,194,1,0,0,0,193,191,1,0,0,0,194,195,5,37,0,0,195,231,
        1,0,0,0,196,197,5,7,0,0,197,201,5,34,0,0,198,202,5,42,0,0,199,200,
        5,6,0,0,200,202,5,42,0,0,201,198,1,0,0,0,201,199,1,0,0,0,202,203,
        1,0,0,0,203,204,5,25,0,0,204,205,3,16,8,0,205,206,5,27,0,0,206,213,
        3,16,8,0,207,209,7,2,0,0,208,210,5,25,0,0,209,208,1,0,0,0,209,210,
        1,0,0,0,210,214,1,0,0,0,211,212,7,3,0,0,212,214,5,25,0,0,213,207,
        1,0,0,0,213,211,1,0,0,0,214,215,1,0,0,0,215,216,3,16,8,0,216,217,
        5,27,0,0,217,218,5,42,0,0,218,219,5,25,0,0,219,220,3,16,8,0,220,
        221,5,35,0,0,221,225,5,36,0,0,222,224,3,12,6,0,223,222,1,0,0,0,224,
        227,1,0,0,0,225,223,1,0,0,0,225,226,1,0,0,0,226,228,1,0,0,0,227,
        225,1,0,0,0,228,229,5,37,0,0,229,231,1,0,0,0,230,183,1,0,0,0,230,
        196,1,0,0,0,231,19,1,0,0,0,232,233,5,9,0,0,233,234,5,34,0,0,234,
        235,3,16,8,0,235,236,5,35,0,0,236,240,5,36,0,0,237,239,3,12,6,0,
        238,237,1,0,0,0,239,242,1,0,0,0,240,238,1,0,0,0,240,241,1,0,0,0,
        241,243,1,0,0,0,242,240,1,0,0,0,243,253,5,37,0,0,244,245,5,10,0,
        0,245,249,5,36,0,0,246,248,3,12,6,0,247,246,1,0,0,0,248,251,1,0,
        0,0,249,247,1,0,0,0,249,250,1,0,0,0,250,252,1,0,0,0,251,249,1,0,
        0,0,252,254,5,37,0,0,253,244,1,0,0,0,253,254,1,0,0,0,254,276,1,0,
        0,0,255,256,5,11,0,0,256,257,5,34,0,0,257,258,5,42,0,0,258,259,5,
        35,0,0,259,271,5,36,0,0,260,261,5,12,0,0,261,262,5,41,0,0,262,266,
        5,28,0,0,263,265,3,12,6,0,264,263,1,0,0,0,265,268,1,0,0,0,266,264,
        1,0,0,0,266,267,1,0,0,0,267,270,1,0,0,0,268,266,1,0,0,0,269,260,
        1,0,0,0,270,273,1,0,0,0,271,269,1,0,0,0,271,272,1,0,0,0,272,274,
        1,0,0,0,273,271,1,0,0,0,274,276,5,37,0,0,275,232,1,0,0,0,275,255,
        1,0,0,0,276,21,1,0,0,0,277,278,7,4,0,0,278,23,1,0,0,0,279,280,5,
        42,0,0,280,281,5,34,0,0,281,286,3,16,8,0,282,283,5,26,0,0,283,285,
        3,16,8,0,284,282,1,0,0,0,285,288,1,0,0,0,286,284,1,0,0,0,286,287,
        1,0,0,0,287,289,1,0,0,0,288,286,1,0,0,0,289,290,5,35,0,0,290,301,
        1,0,0,0,291,292,3,22,11,0,292,293,5,34,0,0,293,294,3,16,8,0,294,
        295,5,26,0,0,295,296,3,16,8,0,296,297,5,26,0,0,297,298,3,16,8,0,
        298,299,5,35,0,0,299,301,1,0,0,0,300,279,1,0,0,0,300,291,1,0,0,0,
        301,25,1,0,0,0,28,62,75,81,95,99,101,120,133,141,156,171,175,178,
        180,191,201,209,213,225,230,240,249,253,266,271,275,286,300
    ]

class ExprParser ( Parser ):

    grammarFileName = "ExprParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'node'", "'graph'", "'arc'", "'nodes'", 
                     "'arcs'", "'int'", "'for'", "'while'", "'if'", "'else'", 
                     "'switch'", "'case'", "'break'", "'return'", "'continue'", 
                     "'function'", "'+'", "'-'", "'/'", "'&'", "'*'", "'and'", 
                     "'or'", "'not'", "'='", "','", "';'", "':'", "'!'", 
                     "'['", "']'", "'<'", "'>'", "'('", "')'", "'{'", "'}'", 
                     "'depth_first_search'", "'breadth_first_search'", "'shortest_path'" ]

    symbolicNames = [ "<INVALID>", "NODE", "GRAPH", "ARC", "N_ELEM", "A_ELEM", 
                      "TYPE_INT", "FOR", "WHILE", "IF", "ELSE", "SWITCH", 
                      "CASE", "BREAK", "RETURN", "CONTINUE", "FUNCTION", 
                      "UNION", "DIFF", "SYMDIFF", "INTERSEC", "CART", "AND", 
                      "OR", "NOT", "EQ", "COMMA", "SEMI", "COLON", "EXCLAM", 
                      "LSQUARE", "RSQUARE", "LANGLE", "RANGLE", "LPAREN", 
                      "RPAREN", "LCURLY", "RCURLY", "DEPTH_FIRST_SEARCH", 
                      "BREADTH_FIRST_SEARCH", "SHORTEST_PATH", "INT", "ID", 
                      "WS" ]

    RULE_types = 0
    RULE_operation = 1
    RULE_anoun = 2
    RULE_node = 3
    RULE_arc = 4
    RULE_program = 5
    RULE_stat = 6
    RULE_def = 7
    RULE_expr = 8
    RULE_cicle = 9
    RULE_condition = 10
    RULE_or_func = 11
    RULE_func = 12

    ruleNames =  [ "types", "operation", "anoun", "node", "arc", "program", 
                   "stat", "def", "expr", "cicle", "condition", "or_func", 
                   "func" ]

    EOF = Token.EOF
    NODE=1
    GRAPH=2
    ARC=3
    N_ELEM=4
    A_ELEM=5
    TYPE_INT=6
    FOR=7
    WHILE=8
    IF=9
    ELSE=10
    SWITCH=11
    CASE=12
    BREAK=13
    RETURN=14
    CONTINUE=15
    FUNCTION=16
    UNION=17
    DIFF=18
    SYMDIFF=19
    INTERSEC=20
    CART=21
    AND=22
    OR=23
    NOT=24
    EQ=25
    COMMA=26
    SEMI=27
    COLON=28
    EXCLAM=29
    LSQUARE=30
    RSQUARE=31
    LANGLE=32
    RANGLE=33
    LPAREN=34
    RPAREN=35
    LCURLY=36
    RCURLY=37
    DEPTH_FIRST_SEARCH=38
    BREADTH_FIRST_SEARCH=39
    SHORTEST_PATH=40
    INT=41
    ID=42
    WS=43

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class TypesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NODE(self):
            return self.getToken(ExprParser.NODE, 0)

        def ARC(self):
            return self.getToken(ExprParser.ARC, 0)

        def GRAPH(self):
            return self.getToken(ExprParser.GRAPH, 0)

        def TYPE_INT(self):
            return self.getToken(ExprParser.TYPE_INT, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_types

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypes" ):
                listener.enterTypes(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypes" ):
                listener.exitTypes(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypes" ):
                return visitor.visitTypes(self)
            else:
                return visitor.visitChildren(self)




    def types(self):

        localctx = ExprParser.TypesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_types)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 78) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def UNION(self):
            return self.getToken(ExprParser.UNION, 0)

        def DIFF(self):
            return self.getToken(ExprParser.DIFF, 0)

        def SYMDIFF(self):
            return self.getToken(ExprParser.SYMDIFF, 0)

        def INTERSEC(self):
            return self.getToken(ExprParser.INTERSEC, 0)

        def CART(self):
            return self.getToken(ExprParser.CART, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_operation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperation" ):
                listener.enterOperation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperation" ):
                listener.exitOperation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperation" ):
                return visitor.visitOperation(self)
            else:
                return visitor.visitChildren(self)




    def operation(self):

        localctx = ExprParser.OperationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_operation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4063232) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AnounContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def types(self):
            return self.getTypedRuleContext(ExprParser.TypesContext,0)


        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def TYPE_INT(self):
            return self.getToken(ExprParser.TYPE_INT, 0)

        def EQ(self):
            return self.getToken(ExprParser.EQ, 0)

        def INT(self):
            return self.getToken(ExprParser.INT, 0)

        def GRAPH(self):
            return self.getToken(ExprParser.GRAPH, 0)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def ARC(self):
            return self.getToken(ExprParser.ARC, 0)

        def LANGLE(self):
            return self.getToken(ExprParser.LANGLE, 0)

        def node(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.NodeContext)
            else:
                return self.getTypedRuleContext(ExprParser.NodeContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.COMMA)
            else:
                return self.getToken(ExprParser.COMMA, i)

        def RANGLE(self):
            return self.getToken(ExprParser.RANGLE, 0)

        def LSQUARE(self):
            return self.getToken(ExprParser.LSQUARE, 0)

        def N_ELEM(self):
            return self.getToken(ExprParser.N_ELEM, 0)

        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.COLON)
            else:
                return self.getToken(ExprParser.COLON, i)

        def LPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.LPAREN)
            else:
                return self.getToken(ExprParser.LPAREN, i)

        def RPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.RPAREN)
            else:
                return self.getToken(ExprParser.RPAREN, i)

        def A_ELEM(self):
            return self.getToken(ExprParser.A_ELEM, 0)

        def arc(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ArcContext)
            else:
                return self.getTypedRuleContext(ExprParser.ArcContext,i)


        def RSQUARE(self):
            return self.getToken(ExprParser.RSQUARE, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_anoun

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnoun" ):
                listener.enterAnoun(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnoun" ):
                listener.exitAnoun(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAnoun" ):
                return visitor.visitAnoun(self)
            else:
                return visitor.visitChildren(self)




    def anoun(self):

        localctx = ExprParser.AnounContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_anoun)
        self._la = 0 # Token type
        try:
            self.state = 81
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 30
                self.types()
                self.state = 31
                self.match(ExprParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 33
                self.match(ExprParser.TYPE_INT)
                self.state = 34
                self.match(ExprParser.ID)
                self.state = 35
                self.match(ExprParser.EQ)
                self.state = 36
                self.match(ExprParser.INT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 37
                self.match(ExprParser.GRAPH)
                self.state = 38
                self.match(ExprParser.ID)
                self.state = 39
                self.match(ExprParser.EQ)
                self.state = 40
                self.expr(0)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 41
                self.match(ExprParser.ARC)
                self.state = 42
                self.match(ExprParser.ID)
                self.state = 43
                self.match(ExprParser.EQ)
                self.state = 44
                self.match(ExprParser.LANGLE)
                self.state = 45
                self.node()
                self.state = 46
                self.match(ExprParser.COMMA)
                self.state = 47
                self.node()
                self.state = 48
                self.match(ExprParser.RANGLE)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 50
                self.match(ExprParser.GRAPH)
                self.state = 51
                self.match(ExprParser.ID)
                self.state = 52
                self.match(ExprParser.EQ)
                self.state = 53
                self.match(ExprParser.LSQUARE)
                self.state = 54
                self.match(ExprParser.N_ELEM)
                self.state = 55
                self.match(ExprParser.COLON)
                self.state = 56
                self.match(ExprParser.LPAREN)
                self.state = 57
                self.node()
                self.state = 62
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==26:
                    self.state = 58
                    self.match(ExprParser.COMMA)
                    self.state = 59
                    self.node()
                    self.state = 64
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 65
                self.match(ExprParser.RPAREN)
                self.state = 66
                self.match(ExprParser.COMMA)
                self.state = 67
                self.match(ExprParser.A_ELEM)
                self.state = 68
                self.match(ExprParser.COLON)
                self.state = 69
                self.match(ExprParser.LPAREN)
                self.state = 70
                self.arc()
                self.state = 75
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==26:
                    self.state = 71
                    self.match(ExprParser.COMMA)
                    self.state = 72
                    self.arc()
                    self.state = 77
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 78
                self.match(ExprParser.RPAREN)
                self.state = 79
                self.match(ExprParser.RSQUARE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NodeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_node

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNode" ):
                listener.enterNode(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNode" ):
                listener.exitNode(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNode" ):
                return visitor.visitNode(self)
            else:
                return visitor.visitChildren(self)




    def node(self):

        localctx = ExprParser.NodeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_node)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.match(ExprParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArcContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def ARC(self):
            return self.getToken(ExprParser.ARC, 0)

        def EQ(self):
            return self.getToken(ExprParser.EQ, 0)

        def LANGLE(self):
            return self.getToken(ExprParser.LANGLE, 0)

        def node(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.NodeContext)
            else:
                return self.getTypedRuleContext(ExprParser.NodeContext,i)


        def COMMA(self):
            return self.getToken(ExprParser.COMMA, 0)

        def RANGLE(self):
            return self.getToken(ExprParser.RANGLE, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_arc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArc" ):
                listener.enterArc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArc" ):
                listener.exitArc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArc" ):
                return visitor.visitArc(self)
            else:
                return visitor.visitChildren(self)




    def arc(self):

        localctx = ExprParser.ArcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_arc)
        try:
            self.state = 95
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [42]:
                self.enterOuterAlt(localctx, 1)
                self.state = 85
                self.match(ExprParser.ID)
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 86
                self.match(ExprParser.ARC)
                self.state = 87
                self.match(ExprParser.ID)
                self.state = 88
                self.match(ExprParser.EQ)
                self.state = 89
                self.match(ExprParser.LANGLE)
                self.state = 90
                self.node()
                self.state = 91
                self.match(ExprParser.COMMA)
                self.state = 92
                self.node()
                self.state = 93
                self.match(ExprParser.RANGLE)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(ExprParser.EOF, 0)

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.StatContext)
            else:
                return self.getTypedRuleContext(ExprParser.StatContext,i)


        def anoun(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.AnounContext)
            else:
                return self.getTypedRuleContext(ExprParser.AnounContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = ExprParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8521232018382) != 0):
                self.state = 99
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                if la_ == 1:
                    self.state = 97
                    self.stat()
                    pass

                elif la_ == 2:
                    self.state = 98
                    self.anoun()
                    pass


                self.state = 103
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 104
            self.match(ExprParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def EQ(self):
            return self.getToken(ExprParser.EQ, 0)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def SEMI(self):
            return self.getToken(ExprParser.SEMI, 0)

        def anoun(self):
            return self.getTypedRuleContext(ExprParser.AnounContext,0)


        def cicle(self):
            return self.getTypedRuleContext(ExprParser.CicleContext,0)


        def condition(self):
            return self.getTypedRuleContext(ExprParser.ConditionContext,0)


        def def_(self):
            return self.getTypedRuleContext(ExprParser.DefContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStat" ):
                listener.enterStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStat" ):
                listener.exitStat(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStat" ):
                return visitor.visitStat(self)
            else:
                return visitor.visitChildren(self)




    def stat(self):

        localctx = ExprParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_stat)
        try:
            self.state = 120
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 106
                self.match(ExprParser.ID)
                self.state = 107
                self.match(ExprParser.EQ)
                self.state = 108
                self.expr(0)
                self.state = 109
                self.match(ExprParser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 111
                self.expr(0)
                self.state = 112
                self.match(ExprParser.SEMI)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 114
                self.anoun()
                self.state = 115
                self.match(ExprParser.SEMI)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 117
                self.cicle()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 118
                self.condition()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 119
                self.def_()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION(self):
            return self.getToken(ExprParser.FUNCTION, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.ID)
            else:
                return self.getToken(ExprParser.ID, i)

        def LPAREN(self):
            return self.getToken(ExprParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(ExprParser.RPAREN, 0)

        def LCURLY(self):
            return self.getToken(ExprParser.LCURLY, 0)

        def RCURLY(self):
            return self.getToken(ExprParser.RCURLY, 0)

        def types(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.TypesContext)
            else:
                return self.getTypedRuleContext(ExprParser.TypesContext,i)


        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.StatContext)
            else:
                return self.getTypedRuleContext(ExprParser.StatContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.COMMA)
            else:
                return self.getToken(ExprParser.COMMA, i)

        def getRuleIndex(self):
            return ExprParser.RULE_def

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDef" ):
                listener.enterDef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDef" ):
                listener.exitDef(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDef" ):
                return visitor.visitDef(self)
            else:
                return visitor.visitChildren(self)




    def def_(self):

        localctx = ExprParser.DefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_def)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.match(ExprParser.FUNCTION)
            self.state = 123
            self.match(ExprParser.ID)
            self.state = 124
            self.match(ExprParser.LPAREN)

            self.state = 125
            self.types()
            self.state = 126
            self.match(ExprParser.ID)
            self.state = 133
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==26:
                self.state = 127
                self.match(ExprParser.COMMA)
                self.state = 128
                self.types()
                self.state = 129
                self.match(ExprParser.ID)
                self.state = 135
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 136
            self.match(ExprParser.RPAREN)
            self.state = 137
            self.match(ExprParser.LCURLY)
            self.state = 141
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8521232018382) != 0):
                self.state = 138
                self.stat()
                self.state = 143
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 144
            self.match(ExprParser.RCURLY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def func(self):
            return self.getTypedRuleContext(ExprParser.FuncContext,0)


        def NOT(self):
            return self.getToken(ExprParser.NOT, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)


        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def INT(self):
            return self.getToken(ExprParser.INT, 0)

        def BREAK(self):
            return self.getToken(ExprParser.BREAK, 0)

        def CONTINUE(self):
            return self.getToken(ExprParser.CONTINUE, 0)

        def RETURN(self):
            return self.getToken(ExprParser.RETURN, 0)

        def operation(self):
            return self.getTypedRuleContext(ExprParser.OperationContext,0)


        def AND(self):
            return self.getToken(ExprParser.AND, 0)

        def OR(self):
            return self.getToken(ExprParser.OR, 0)

        def EQ(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.EQ)
            else:
                return self.getToken(ExprParser.EQ, i)

        def LANGLE(self):
            return self.getToken(ExprParser.LANGLE, 0)

        def RANGLE(self):
            return self.getToken(ExprParser.RANGLE, 0)

        def EXCLAM(self):
            return self.getToken(ExprParser.EXCLAM, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ExprParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 16
        self.enterRecursionRule(localctx, 16, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 147
                self.func()
                pass

            elif la_ == 2:
                self.state = 148
                self.match(ExprParser.NOT)
                self.state = 149
                self.expr(9)
                pass

            elif la_ == 3:
                self.state = 150
                self.match(ExprParser.ID)
                pass

            elif la_ == 4:
                self.state = 151
                self.match(ExprParser.INT)
                pass

            elif la_ == 5:
                self.state = 152
                self.match(ExprParser.BREAK)
                pass

            elif la_ == 6:
                self.state = 153
                self.match(ExprParser.CONTINUE)
                pass

            elif la_ == 7:
                self.state = 154
                self.match(ExprParser.RETURN)
                self.state = 155
                self.expr(1)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 180
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 178
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
                    if la_ == 1:
                        localctx = ExprParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 158
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 159
                        self.operation()
                        self.state = 160
                        self.expr(11)
                        pass

                    elif la_ == 2:
                        localctx = ExprParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 162
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 163
                        self.match(ExprParser.AND)
                        self.state = 164
                        self.expr(9)
                        pass

                    elif la_ == 3:
                        localctx = ExprParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 165
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 166
                        self.match(ExprParser.OR)
                        self.state = 167
                        self.expr(8)
                        pass

                    elif la_ == 4:
                        localctx = ExprParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 168
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 175
                        self._errHandler.sync(self)
                        token = self._input.LA(1)
                        if token in [32, 33]:
                            self.state = 169
                            _la = self._input.LA(1)
                            if not(_la==32 or _la==33):
                                self._errHandler.recoverInline(self)
                            else:
                                self._errHandler.reportMatch(self)
                                self.consume()
                            self.state = 171
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            if _la==25:
                                self.state = 170
                                self.match(ExprParser.EQ)


                            pass
                        elif token in [25, 29]:
                            self.state = 173
                            _la = self._input.LA(1)
                            if not(_la==25 or _la==29):
                                self._errHandler.recoverInline(self)
                            else:
                                self._errHandler.reportMatch(self)
                                self.consume()
                            self.state = 174
                            self.match(ExprParser.EQ)
                            pass
                        else:
                            raise NoViableAltException(self)

                        self.state = 177
                        self.expr(7)
                        pass

             
                self.state = 182
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class CicleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(ExprParser.WHILE, 0)

        def LPAREN(self):
            return self.getToken(ExprParser.LPAREN, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)


        def RPAREN(self):
            return self.getToken(ExprParser.RPAREN, 0)

        def LCURLY(self):
            return self.getToken(ExprParser.LCURLY, 0)

        def RCURLY(self):
            return self.getToken(ExprParser.RCURLY, 0)

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.StatContext)
            else:
                return self.getTypedRuleContext(ExprParser.StatContext,i)


        def FOR(self):
            return self.getToken(ExprParser.FOR, 0)

        def EQ(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.EQ)
            else:
                return self.getToken(ExprParser.EQ, i)

        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.SEMI)
            else:
                return self.getToken(ExprParser.SEMI, i)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.ID)
            else:
                return self.getToken(ExprParser.ID, i)

        def TYPE_INT(self):
            return self.getToken(ExprParser.TYPE_INT, 0)

        def LANGLE(self):
            return self.getToken(ExprParser.LANGLE, 0)

        def RANGLE(self):
            return self.getToken(ExprParser.RANGLE, 0)

        def EXCLAM(self):
            return self.getToken(ExprParser.EXCLAM, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_cicle

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCicle" ):
                listener.enterCicle(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCicle" ):
                listener.exitCicle(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCicle" ):
                return visitor.visitCicle(self)
            else:
                return visitor.visitChildren(self)




    def cicle(self):

        localctx = ExprParser.CicleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_cicle)
        self._la = 0 # Token type
        try:
            self.state = 230
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 183
                self.match(ExprParser.WHILE)
                self.state = 184
                self.match(ExprParser.LPAREN)
                self.state = 185
                self.expr(0)
                self.state = 186
                self.match(ExprParser.RPAREN)
                self.state = 187
                self.match(ExprParser.LCURLY)
                self.state = 191
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8521232018382) != 0):
                    self.state = 188
                    self.stat()
                    self.state = 193
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 194
                self.match(ExprParser.RCURLY)
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 196
                self.match(ExprParser.FOR)
                self.state = 197
                self.match(ExprParser.LPAREN)
                self.state = 201
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [42]:
                    self.state = 198
                    self.match(ExprParser.ID)
                    pass
                elif token in [6]:
                    self.state = 199
                    self.match(ExprParser.TYPE_INT)
                    self.state = 200
                    self.match(ExprParser.ID)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 203
                self.match(ExprParser.EQ)
                self.state = 204
                self.expr(0)
                self.state = 205
                self.match(ExprParser.SEMI)
                self.state = 206
                self.expr(0)
                self.state = 213
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [32, 33]:
                    self.state = 207
                    _la = self._input.LA(1)
                    if not(_la==32 or _la==33):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 209
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==25:
                        self.state = 208
                        self.match(ExprParser.EQ)


                    pass
                elif token in [25, 29]:
                    self.state = 211
                    _la = self._input.LA(1)
                    if not(_la==25 or _la==29):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 212
                    self.match(ExprParser.EQ)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 215
                self.expr(0)
                self.state = 216
                self.match(ExprParser.SEMI)
                self.state = 217
                self.match(ExprParser.ID)
                self.state = 218
                self.match(ExprParser.EQ)
                self.state = 219
                self.expr(0)
                self.state = 220
                self.match(ExprParser.RPAREN)
                self.state = 221
                self.match(ExprParser.LCURLY)
                self.state = 225
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8521232018382) != 0):
                    self.state = 222
                    self.stat()
                    self.state = 227
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 228
                self.match(ExprParser.RCURLY)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(ExprParser.IF, 0)

        def LPAREN(self):
            return self.getToken(ExprParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(ExprParser.RPAREN, 0)

        def LCURLY(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.LCURLY)
            else:
                return self.getToken(ExprParser.LCURLY, i)

        def RCURLY(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.RCURLY)
            else:
                return self.getToken(ExprParser.RCURLY, i)

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.StatContext)
            else:
                return self.getTypedRuleContext(ExprParser.StatContext,i)


        def ELSE(self):
            return self.getToken(ExprParser.ELSE, 0)

        def SWITCH(self):
            return self.getToken(ExprParser.SWITCH, 0)

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def CASE(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.CASE)
            else:
                return self.getToken(ExprParser.CASE, i)

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.INT)
            else:
                return self.getToken(ExprParser.INT, i)

        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.COLON)
            else:
                return self.getToken(ExprParser.COLON, i)

        def getRuleIndex(self):
            return ExprParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition" ):
                return visitor.visitCondition(self)
            else:
                return visitor.visitChildren(self)




    def condition(self):

        localctx = ExprParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_condition)
        self._la = 0 # Token type
        try:
            self.state = 275
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9]:
                self.enterOuterAlt(localctx, 1)
                self.state = 232
                self.match(ExprParser.IF)
                self.state = 233
                self.match(ExprParser.LPAREN)
                self.state = 234
                self.expr(0)
                self.state = 235
                self.match(ExprParser.RPAREN)
                self.state = 236
                self.match(ExprParser.LCURLY)
                self.state = 240
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8521232018382) != 0):
                    self.state = 237
                    self.stat()
                    self.state = 242
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 243
                self.match(ExprParser.RCURLY)
                self.state = 253
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==10:
                    self.state = 244
                    self.match(ExprParser.ELSE)
                    self.state = 245
                    self.match(ExprParser.LCURLY)
                    self.state = 249
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8521232018382) != 0):
                        self.state = 246
                        self.stat()
                        self.state = 251
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 252
                    self.match(ExprParser.RCURLY)


                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 255
                self.match(ExprParser.SWITCH)
                self.state = 256
                self.match(ExprParser.LPAREN)
                self.state = 257
                self.match(ExprParser.ID)
                self.state = 258
                self.match(ExprParser.RPAREN)
                self.state = 259
                self.match(ExprParser.LCURLY)
                self.state = 271
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==12:
                    self.state = 260
                    self.match(ExprParser.CASE)
                    self.state = 261
                    self.match(ExprParser.INT)
                    self.state = 262
                    self.match(ExprParser.COLON)
                    self.state = 266
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8521232018382) != 0):
                        self.state = 263
                        self.stat()
                        self.state = 268
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 273
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 274
                self.match(ExprParser.RCURLY)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Or_funcContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEPTH_FIRST_SEARCH(self):
            return self.getToken(ExprParser.DEPTH_FIRST_SEARCH, 0)

        def BREADTH_FIRST_SEARCH(self):
            return self.getToken(ExprParser.BREADTH_FIRST_SEARCH, 0)

        def SHORTEST_PATH(self):
            return self.getToken(ExprParser.SHORTEST_PATH, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_or_func

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOr_func" ):
                listener.enterOr_func(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOr_func" ):
                listener.exitOr_func(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOr_func" ):
                return visitor.visitOr_func(self)
            else:
                return visitor.visitChildren(self)




    def or_func(self):

        localctx = ExprParser.Or_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_or_func)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 277
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1924145348608) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def LPAREN(self):
            return self.getToken(ExprParser.LPAREN, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)


        def RPAREN(self):
            return self.getToken(ExprParser.RPAREN, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.COMMA)
            else:
                return self.getToken(ExprParser.COMMA, i)

        def or_func(self):
            return self.getTypedRuleContext(ExprParser.Or_funcContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_func

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc" ):
                listener.enterFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc" ):
                listener.exitFunc(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc" ):
                return visitor.visitFunc(self)
            else:
                return visitor.visitChildren(self)




    def func(self):

        localctx = ExprParser.FuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_func)
        self._la = 0 # Token type
        try:
            self.state = 300
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [42]:
                self.enterOuterAlt(localctx, 1)
                self.state = 279
                self.match(ExprParser.ID)
                self.state = 280
                self.match(ExprParser.LPAREN)
                self.state = 281
                self.expr(0)
                self.state = 286
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==26:
                    self.state = 282
                    self.match(ExprParser.COMMA)
                    self.state = 283
                    self.expr(0)
                    self.state = 288
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 289
                self.match(ExprParser.RPAREN)
                pass
            elif token in [38, 39, 40]:
                self.enterOuterAlt(localctx, 2)
                self.state = 291
                self.or_func()
                self.state = 292
                self.match(ExprParser.LPAREN)
                self.state = 293
                self.expr(0)
                self.state = 294
                self.match(ExprParser.COMMA)
                self.state = 295
                self.expr(0)
                self.state = 296
                self.match(ExprParser.COMMA)
                self.state = 297
                self.expr(0)
                self.state = 298
                self.match(ExprParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[8] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 6)
         




