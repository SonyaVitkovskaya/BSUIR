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
        4,1,40,305,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,1,0,1,1,1,1,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,57,8,2,1,2,1,2,
        1,2,5,2,62,8,2,10,2,12,2,65,9,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,73,8,
        2,1,2,1,2,1,2,5,2,78,8,2,10,2,12,2,81,9,2,1,2,1,2,1,2,3,2,86,8,2,
        1,3,1,3,1,3,3,3,91,8,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,110,8,4,1,5,1,5,5,5,114,8,5,10,5,12,
        5,117,9,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,
        6,1,6,1,6,3,6,135,8,6,1,7,1,7,1,7,1,7,3,7,141,8,7,1,7,1,7,1,7,5,
        7,146,8,7,10,7,12,7,149,9,7,1,7,1,7,1,7,5,7,154,8,7,10,7,12,7,157,
        9,7,1,7,3,7,160,8,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,
        172,8,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,
        187,8,8,1,8,1,8,3,8,191,8,8,1,8,5,8,194,8,8,10,8,12,8,197,9,8,1,
        9,1,9,1,9,1,9,1,9,1,9,5,9,205,8,9,10,9,12,9,208,9,9,1,9,1,9,1,9,
        1,9,1,9,1,9,1,9,3,9,217,8,9,1,9,1,9,1,9,1,9,1,9,1,9,3,9,225,8,9,
        1,9,1,9,3,9,229,8,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,5,9,239,8,9,
        10,9,12,9,242,9,9,1,9,1,9,3,9,246,8,9,1,10,1,10,1,10,1,10,1,10,1,
        10,5,10,254,8,10,10,10,12,10,257,9,10,1,10,1,10,1,10,1,10,5,10,263,
        8,10,10,10,12,10,266,9,10,1,10,3,10,269,8,10,1,10,1,10,1,10,1,10,
        1,10,1,10,1,10,1,10,1,10,5,10,280,8,10,10,10,12,10,283,9,10,5,10,
        285,8,10,10,10,12,10,288,9,10,1,10,3,10,291,8,10,1,11,1,11,1,11,
        1,11,1,11,5,11,298,8,11,10,11,12,11,301,9,11,1,11,1,11,1,11,0,1,
        16,12,0,2,4,6,8,10,12,14,16,18,20,22,0,4,2,0,1,3,6,6,1,0,17,21,1,
        0,32,33,2,0,25,25,29,29,340,0,24,1,0,0,0,2,26,1,0,0,0,4,85,1,0,0,
        0,6,90,1,0,0,0,8,109,1,0,0,0,10,115,1,0,0,0,12,134,1,0,0,0,14,159,
        1,0,0,0,16,171,1,0,0,0,18,245,1,0,0,0,20,290,1,0,0,0,22,292,1,0,
        0,0,24,25,7,0,0,0,25,1,1,0,0,0,26,27,7,1,0,0,27,3,1,0,0,0,28,29,
        3,0,0,0,29,30,5,39,0,0,30,86,1,0,0,0,31,32,5,6,0,0,32,33,5,39,0,
        0,33,34,5,25,0,0,34,86,5,38,0,0,35,36,5,2,0,0,36,37,5,39,0,0,37,
        38,5,25,0,0,38,86,3,16,8,0,39,40,5,3,0,0,40,41,5,39,0,0,41,42,5,
        25,0,0,42,43,5,32,0,0,43,44,3,6,3,0,44,45,5,26,0,0,45,46,3,6,3,0,
        46,47,5,33,0,0,47,86,1,0,0,0,48,49,5,2,0,0,49,50,5,39,0,0,50,51,
        5,25,0,0,51,52,5,30,0,0,52,53,5,4,0,0,53,54,5,28,0,0,54,56,5,34,
        0,0,55,57,3,6,3,0,56,55,1,0,0,0,56,57,1,0,0,0,57,86,1,0,0,0,58,63,
        3,6,3,0,59,60,5,26,0,0,60,62,3,6,3,0,61,59,1,0,0,0,62,65,1,0,0,0,
        63,61,1,0,0,0,63,64,1,0,0,0,64,66,1,0,0,0,65,63,1,0,0,0,66,67,5,
        35,0,0,67,68,5,26,0,0,68,69,5,5,0,0,69,70,5,28,0,0,70,72,5,34,0,
        0,71,73,3,8,4,0,72,71,1,0,0,0,72,73,1,0,0,0,73,74,1,0,0,0,74,79,
        3,8,4,0,75,76,5,26,0,0,76,78,3,8,4,0,77,75,1,0,0,0,78,81,1,0,0,0,
        79,77,1,0,0,0,79,80,1,0,0,0,80,82,1,0,0,0,81,79,1,0,0,0,82,83,5,
        35,0,0,83,84,5,31,0,0,84,86,1,0,0,0,85,28,1,0,0,0,85,31,1,0,0,0,
        85,35,1,0,0,0,85,39,1,0,0,0,85,48,1,0,0,0,85,58,1,0,0,0,86,5,1,0,
        0,0,87,91,5,39,0,0,88,89,5,1,0,0,89,91,5,39,0,0,90,87,1,0,0,0,90,
        88,1,0,0,0,91,7,1,0,0,0,92,110,5,39,0,0,93,94,5,3,0,0,94,95,5,39,
        0,0,95,96,5,25,0,0,96,97,5,32,0,0,97,98,3,6,3,0,98,99,5,26,0,0,99,
        100,3,6,3,0,100,101,5,33,0,0,101,102,5,27,0,0,102,110,1,0,0,0,103,
        104,5,32,0,0,104,105,3,6,3,0,105,106,5,26,0,0,106,107,3,6,3,0,107,
        108,5,33,0,0,108,110,1,0,0,0,109,92,1,0,0,0,109,93,1,0,0,0,109,103,
        1,0,0,0,110,9,1,0,0,0,111,114,3,12,6,0,112,114,3,4,2,0,113,111,1,
        0,0,0,113,112,1,0,0,0,114,117,1,0,0,0,115,113,1,0,0,0,115,116,1,
        0,0,0,116,118,1,0,0,0,117,115,1,0,0,0,118,119,5,0,0,1,119,11,1,0,
        0,0,120,121,5,39,0,0,121,122,5,25,0,0,122,123,3,16,8,0,123,124,5,
        27,0,0,124,135,1,0,0,0,125,126,3,16,8,0,126,127,5,27,0,0,127,135,
        1,0,0,0,128,129,3,4,2,0,129,130,5,27,0,0,130,135,1,0,0,0,131,135,
        3,18,9,0,132,135,3,20,10,0,133,135,3,14,7,0,134,120,1,0,0,0,134,
        125,1,0,0,0,134,128,1,0,0,0,134,131,1,0,0,0,134,132,1,0,0,0,134,
        133,1,0,0,0,135,13,1,0,0,0,136,137,5,16,0,0,137,138,5,39,0,0,138,
        140,5,34,0,0,139,141,5,39,0,0,140,139,1,0,0,0,140,141,1,0,0,0,141,
        160,1,0,0,0,142,147,5,39,0,0,143,144,5,26,0,0,144,146,5,39,0,0,145,
        143,1,0,0,0,146,149,1,0,0,0,147,145,1,0,0,0,147,148,1,0,0,0,148,
        150,1,0,0,0,149,147,1,0,0,0,150,151,5,35,0,0,151,155,5,36,0,0,152,
        154,3,12,6,0,153,152,1,0,0,0,154,157,1,0,0,0,155,153,1,0,0,0,155,
        156,1,0,0,0,156,158,1,0,0,0,157,155,1,0,0,0,158,160,5,37,0,0,159,
        136,1,0,0,0,159,142,1,0,0,0,160,15,1,0,0,0,161,162,6,8,-1,0,162,
        172,3,22,11,0,163,164,5,24,0,0,164,172,3,16,8,9,165,172,5,39,0,0,
        166,172,5,38,0,0,167,172,5,13,0,0,168,172,5,15,0,0,169,170,5,14,
        0,0,170,172,3,16,8,1,171,161,1,0,0,0,171,163,1,0,0,0,171,165,1,0,
        0,0,171,166,1,0,0,0,171,167,1,0,0,0,171,168,1,0,0,0,171,169,1,0,
        0,0,172,195,1,0,0,0,173,174,10,10,0,0,174,175,3,2,1,0,175,176,3,
        16,8,11,176,194,1,0,0,0,177,178,10,8,0,0,178,179,5,22,0,0,179,194,
        3,16,8,9,180,181,10,7,0,0,181,182,5,23,0,0,182,194,3,16,8,8,183,
        190,10,6,0,0,184,186,7,2,0,0,185,187,5,25,0,0,186,185,1,0,0,0,186,
        187,1,0,0,0,187,191,1,0,0,0,188,189,7,3,0,0,189,191,5,25,0,0,190,
        184,1,0,0,0,190,188,1,0,0,0,191,192,1,0,0,0,192,194,3,16,8,7,193,
        173,1,0,0,0,193,177,1,0,0,0,193,180,1,0,0,0,193,183,1,0,0,0,194,
        197,1,0,0,0,195,193,1,0,0,0,195,196,1,0,0,0,196,17,1,0,0,0,197,195,
        1,0,0,0,198,199,5,8,0,0,199,200,5,34,0,0,200,201,3,16,8,0,201,202,
        5,35,0,0,202,206,5,36,0,0,203,205,3,12,6,0,204,203,1,0,0,0,205,208,
        1,0,0,0,206,204,1,0,0,0,206,207,1,0,0,0,207,209,1,0,0,0,208,206,
        1,0,0,0,209,210,5,37,0,0,210,246,1,0,0,0,211,212,5,7,0,0,212,216,
        5,34,0,0,213,217,5,39,0,0,214,215,5,6,0,0,215,217,5,39,0,0,216,213,
        1,0,0,0,216,214,1,0,0,0,217,218,1,0,0,0,218,219,5,25,0,0,219,220,
        3,16,8,0,220,221,5,27,0,0,221,228,3,16,8,0,222,224,7,2,0,0,223,225,
        5,25,0,0,224,223,1,0,0,0,224,225,1,0,0,0,225,229,1,0,0,0,226,227,
        7,3,0,0,227,229,5,25,0,0,228,222,1,0,0,0,228,226,1,0,0,0,229,230,
        1,0,0,0,230,231,3,16,8,0,231,232,5,27,0,0,232,233,5,39,0,0,233,234,
        5,25,0,0,234,235,3,16,8,0,235,236,5,35,0,0,236,240,5,36,0,0,237,
        239,3,12,6,0,238,237,1,0,0,0,239,242,1,0,0,0,240,238,1,0,0,0,240,
        241,1,0,0,0,241,243,1,0,0,0,242,240,1,0,0,0,243,244,5,37,0,0,244,
        246,1,0,0,0,245,198,1,0,0,0,245,211,1,0,0,0,246,19,1,0,0,0,247,248,
        5,9,0,0,248,249,5,34,0,0,249,250,3,16,8,0,250,251,5,35,0,0,251,255,
        5,36,0,0,252,254,3,12,6,0,253,252,1,0,0,0,254,257,1,0,0,0,255,253,
        1,0,0,0,255,256,1,0,0,0,256,258,1,0,0,0,257,255,1,0,0,0,258,268,
        5,37,0,0,259,260,5,10,0,0,260,264,5,36,0,0,261,263,3,12,6,0,262,
        261,1,0,0,0,263,266,1,0,0,0,264,262,1,0,0,0,264,265,1,0,0,0,265,
        267,1,0,0,0,266,264,1,0,0,0,267,269,5,37,0,0,268,259,1,0,0,0,268,
        269,1,0,0,0,269,291,1,0,0,0,270,271,5,11,0,0,271,272,5,34,0,0,272,
        273,5,39,0,0,273,274,5,35,0,0,274,286,5,36,0,0,275,276,5,12,0,0,
        276,277,5,38,0,0,277,281,5,28,0,0,278,280,3,12,6,0,279,278,1,0,0,
        0,280,283,1,0,0,0,281,279,1,0,0,0,281,282,1,0,0,0,282,285,1,0,0,
        0,283,281,1,0,0,0,284,275,1,0,0,0,285,288,1,0,0,0,286,284,1,0,0,
        0,286,287,1,0,0,0,287,289,1,0,0,0,288,286,1,0,0,0,289,291,5,37,0,
        0,290,247,1,0,0,0,290,270,1,0,0,0,291,21,1,0,0,0,292,293,5,39,0,
        0,293,294,5,34,0,0,294,299,3,16,8,0,295,296,5,26,0,0,296,298,3,16,
        8,0,297,295,1,0,0,0,298,301,1,0,0,0,299,297,1,0,0,0,299,300,1,0,
        0,0,300,302,1,0,0,0,301,299,1,0,0,0,302,303,5,35,0,0,303,23,1,0,
        0,0,32,56,63,72,79,85,90,109,113,115,134,140,147,155,159,171,186,
        190,193,195,206,216,224,228,240,245,255,264,268,281,286,290,299
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
                     "'['", "']'", "'<'", "'>'", "'('", "')'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "NODE", "GRAPH", "ARC", "N_ELEM", "A_ELEM", 
                      "TYPE_INT", "FOR", "WHILE", "IF", "ELSE", "SWITCH", 
                      "CASE", "BREAK", "RETURN", "CONTINUE", "FUNCTION", 
                      "UNION", "DIFF", "SYMDIFF", "INTERSEC", "CART", "AND", 
                      "OR", "NOT", "EQ", "COMMA", "SEMI", "COLON", "EXCLAM", 
                      "LSQUARE", "RSQUARE", "LANGLE", "RANGLE", "LPAREN", 
                      "RPAREN", "LCURLY", "RCURLY", "INT", "ID", "WS" ]

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
    RULE_func = 11

    ruleNames =  [ "types", "operation", "anoun", "node", "arc", "program", 
                   "stat", "def", "expr", "cicle", "condition", "func" ]

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
    INT=38
    ID=39
    WS=40

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




    def types(self):

        localctx = ExprParser.TypesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_types)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
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




    def operation(self):

        localctx = ExprParser.OperationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_operation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
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

        def COLON(self):
            return self.getToken(ExprParser.COLON, 0)

        def LPAREN(self):
            return self.getToken(ExprParser.LPAREN, 0)

        def RPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(ExprParser.RPAREN)
            else:
                return self.getToken(ExprParser.RPAREN, i)

        def A_ELEM(self):
            return self.getToken(ExprParser.A_ELEM, 0)

        def RSQUARE(self):
            return self.getToken(ExprParser.RSQUARE, 0)

        def arc(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ArcContext)
            else:
                return self.getTypedRuleContext(ExprParser.ArcContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_anoun

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnoun" ):
                listener.enterAnoun(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnoun" ):
                listener.exitAnoun(self)




    def anoun(self):

        localctx = ExprParser.AnounContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_anoun)
        self._la = 0 # Token type
        try:
            self.state = 85
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 28
                self.types()
                self.state = 29
                self.match(ExprParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 31
                self.match(ExprParser.TYPE_INT)
                self.state = 32
                self.match(ExprParser.ID)
                self.state = 33
                self.match(ExprParser.EQ)
                self.state = 34
                self.match(ExprParser.INT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 35
                self.match(ExprParser.GRAPH)
                self.state = 36
                self.match(ExprParser.ID)
                self.state = 37
                self.match(ExprParser.EQ)
                self.state = 38
                self.expr(0)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 39
                self.match(ExprParser.ARC)
                self.state = 40
                self.match(ExprParser.ID)
                self.state = 41
                self.match(ExprParser.EQ)
                self.state = 42
                self.match(ExprParser.LANGLE)
                self.state = 43
                self.node()
                self.state = 44
                self.match(ExprParser.COMMA)
                self.state = 45
                self.node()
                self.state = 46
                self.match(ExprParser.RANGLE)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 48
                self.match(ExprParser.GRAPH)
                self.state = 49
                self.match(ExprParser.ID)
                self.state = 50
                self.match(ExprParser.EQ)
                self.state = 51
                self.match(ExprParser.LSQUARE)
                self.state = 52
                self.match(ExprParser.N_ELEM)
                self.state = 53
                self.match(ExprParser.COLON)
                self.state = 54
                self.match(ExprParser.LPAREN)
                self.state = 56
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 55
                    self.node()


                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 58
                self.node()
                self.state = 63
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==26:
                    self.state = 59
                    self.match(ExprParser.COMMA)
                    self.state = 60
                    self.node()
                    self.state = 65
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 66
                self.match(ExprParser.RPAREN)
                self.state = 67
                self.match(ExprParser.COMMA)
                self.state = 68
                self.match(ExprParser.A_ELEM)
                self.state = 69
                self.match(ExprParser.COLON)
                self.state = 70
                self.match(ExprParser.LPAREN)
                self.state = 72
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                if la_ == 1:
                    self.state = 71
                    self.arc()


                self.state = 74
                self.arc()
                self.state = 79
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==26:
                    self.state = 75
                    self.match(ExprParser.COMMA)
                    self.state = 76
                    self.arc()
                    self.state = 81
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 82
                self.match(ExprParser.RPAREN)
                self.state = 83
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

        def NODE(self):
            return self.getToken(ExprParser.NODE, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_node

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNode" ):
                listener.enterNode(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNode" ):
                listener.exitNode(self)




    def node(self):

        localctx = ExprParser.NodeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_node)
        try:
            self.state = 90
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [39]:
                self.enterOuterAlt(localctx, 1)
                self.state = 87
                self.match(ExprParser.ID)
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 88
                self.match(ExprParser.NODE)
                self.state = 89
                self.match(ExprParser.ID)
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

        def SEMI(self):
            return self.getToken(ExprParser.SEMI, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_arc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArc" ):
                listener.enterArc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArc" ):
                listener.exitArc(self)




    def arc(self):

        localctx = ExprParser.ArcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_arc)
        try:
            self.state = 109
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [39]:
                self.enterOuterAlt(localctx, 1)
                self.state = 92
                self.match(ExprParser.ID)
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 93
                self.match(ExprParser.ARC)
                self.state = 94
                self.match(ExprParser.ID)
                self.state = 95
                self.match(ExprParser.EQ)
                self.state = 96
                self.match(ExprParser.LANGLE)
                self.state = 97
                self.node()
                self.state = 98
                self.match(ExprParser.COMMA)
                self.state = 99
                self.node()
                self.state = 100
                self.match(ExprParser.RANGLE)
                self.state = 101
                self.match(ExprParser.SEMI)
                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 3)
                self.state = 103
                self.match(ExprParser.LANGLE)
                self.state = 104
                self.node()
                self.state = 105
                self.match(ExprParser.COMMA)
                self.state = 106
                self.node()
                self.state = 107
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




    def program(self):

        localctx = ExprParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 824650623950) != 0):
                self.state = 113
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                if la_ == 1:
                    self.state = 111
                    self.stat()
                    pass

                elif la_ == 2:
                    self.state = 112
                    self.anoun()
                    pass


                self.state = 117
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 118
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




    def stat(self):

        localctx = ExprParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_stat)
        try:
            self.state = 134
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 120
                self.match(ExprParser.ID)
                self.state = 121
                self.match(ExprParser.EQ)
                self.state = 122
                self.expr(0)
                self.state = 123
                self.match(ExprParser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 125
                self.expr(0)
                self.state = 126
                self.match(ExprParser.SEMI)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 128
                self.anoun()
                self.state = 129
                self.match(ExprParser.SEMI)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 131
                self.cicle()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 132
                self.condition()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 133
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




    def def_(self):

        localctx = ExprParser.DefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_def)
        self._la = 0 # Token type
        try:
            self.state = 159
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                self.enterOuterAlt(localctx, 1)
                self.state = 136
                self.match(ExprParser.FUNCTION)
                self.state = 137
                self.match(ExprParser.ID)
                self.state = 138
                self.match(ExprParser.LPAREN)
                self.state = 140
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
                if la_ == 1:
                    self.state = 139
                    self.match(ExprParser.ID)


                pass
            elif token in [39]:
                self.enterOuterAlt(localctx, 2)
                self.state = 142
                self.match(ExprParser.ID)
                self.state = 147
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==26:
                    self.state = 143
                    self.match(ExprParser.COMMA)
                    self.state = 144
                    self.match(ExprParser.ID)
                    self.state = 149
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 150
                self.match(ExprParser.RPAREN)
                self.state = 151
                self.match(ExprParser.LCURLY)
                self.state = 155
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 824650623950) != 0):
                    self.state = 152
                    self.stat()
                    self.state = 157
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 158
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
            self.state = 171
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 162
                self.func()
                pass

            elif la_ == 2:
                self.state = 163
                self.match(ExprParser.NOT)
                self.state = 164
                self.expr(9)
                pass

            elif la_ == 3:
                self.state = 165
                self.match(ExprParser.ID)
                pass

            elif la_ == 4:
                self.state = 166
                self.match(ExprParser.INT)
                pass

            elif la_ == 5:
                self.state = 167
                self.match(ExprParser.BREAK)
                pass

            elif la_ == 6:
                self.state = 168
                self.match(ExprParser.CONTINUE)
                pass

            elif la_ == 7:
                self.state = 169
                self.match(ExprParser.RETURN)
                self.state = 170
                self.expr(1)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 195
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 193
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
                    if la_ == 1:
                        localctx = ExprParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 173
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 174
                        self.operation()
                        self.state = 175
                        self.expr(11)
                        pass

                    elif la_ == 2:
                        localctx = ExprParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 177
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 178
                        self.match(ExprParser.AND)
                        self.state = 179
                        self.expr(9)
                        pass

                    elif la_ == 3:
                        localctx = ExprParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 180
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 181
                        self.match(ExprParser.OR)
                        self.state = 182
                        self.expr(8)
                        pass

                    elif la_ == 4:
                        localctx = ExprParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 183
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 190
                        self._errHandler.sync(self)
                        token = self._input.LA(1)
                        if token in [32, 33]:
                            self.state = 184
                            _la = self._input.LA(1)
                            if not(_la==32 or _la==33):
                                self._errHandler.recoverInline(self)
                            else:
                                self._errHandler.reportMatch(self)
                                self.consume()
                            self.state = 186
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            if _la==25:
                                self.state = 185
                                self.match(ExprParser.EQ)


                            pass
                        elif token in [25, 29]:
                            self.state = 188
                            _la = self._input.LA(1)
                            if not(_la==25 or _la==29):
                                self._errHandler.recoverInline(self)
                            else:
                                self._errHandler.reportMatch(self)
                                self.consume()
                            self.state = 189
                            self.match(ExprParser.EQ)
                            pass
                        else:
                            raise NoViableAltException(self)

                        self.state = 192
                        self.expr(7)
                        pass

             
                self.state = 197
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

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




    def cicle(self):

        localctx = ExprParser.CicleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_cicle)
        self._la = 0 # Token type
        try:
            self.state = 245
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 198
                self.match(ExprParser.WHILE)
                self.state = 199
                self.match(ExprParser.LPAREN)
                self.state = 200
                self.expr(0)
                self.state = 201
                self.match(ExprParser.RPAREN)
                self.state = 202
                self.match(ExprParser.LCURLY)
                self.state = 206
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 824650623950) != 0):
                    self.state = 203
                    self.stat()
                    self.state = 208
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 209
                self.match(ExprParser.RCURLY)
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 211
                self.match(ExprParser.FOR)
                self.state = 212
                self.match(ExprParser.LPAREN)
                self.state = 216
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [39]:
                    self.state = 213
                    self.match(ExprParser.ID)
                    pass
                elif token in [6]:
                    self.state = 214
                    self.match(ExprParser.TYPE_INT)
                    self.state = 215
                    self.match(ExprParser.ID)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 218
                self.match(ExprParser.EQ)
                self.state = 219
                self.expr(0)
                self.state = 220
                self.match(ExprParser.SEMI)
                self.state = 221
                self.expr(0)
                self.state = 228
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [32, 33]:
                    self.state = 222
                    _la = self._input.LA(1)
                    if not(_la==32 or _la==33):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 224
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==25:
                        self.state = 223
                        self.match(ExprParser.EQ)


                    pass
                elif token in [25, 29]:
                    self.state = 226
                    _la = self._input.LA(1)
                    if not(_la==25 or _la==29):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 227
                    self.match(ExprParser.EQ)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 230
                self.expr(0)
                self.state = 231
                self.match(ExprParser.SEMI)
                self.state = 232
                self.match(ExprParser.ID)
                self.state = 233
                self.match(ExprParser.EQ)
                self.state = 234
                self.expr(0)
                self.state = 235
                self.match(ExprParser.RPAREN)
                self.state = 236
                self.match(ExprParser.LCURLY)
                self.state = 240
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 824650623950) != 0):
                    self.state = 237
                    self.stat()
                    self.state = 242
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 243
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




    def condition(self):

        localctx = ExprParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_condition)
        self._la = 0 # Token type
        try:
            self.state = 290
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9]:
                self.enterOuterAlt(localctx, 1)
                self.state = 247
                self.match(ExprParser.IF)
                self.state = 248
                self.match(ExprParser.LPAREN)
                self.state = 249
                self.expr(0)
                self.state = 250
                self.match(ExprParser.RPAREN)
                self.state = 251
                self.match(ExprParser.LCURLY)
                self.state = 255
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 824650623950) != 0):
                    self.state = 252
                    self.stat()
                    self.state = 257
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 258
                self.match(ExprParser.RCURLY)
                self.state = 268
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==10:
                    self.state = 259
                    self.match(ExprParser.ELSE)
                    self.state = 260
                    self.match(ExprParser.LCURLY)
                    self.state = 264
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while (((_la) & ~0x3f) == 0 and ((1 << _la) & 824650623950) != 0):
                        self.state = 261
                        self.stat()
                        self.state = 266
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 267
                    self.match(ExprParser.RCURLY)


                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 270
                self.match(ExprParser.SWITCH)
                self.state = 271
                self.match(ExprParser.LPAREN)
                self.state = 272
                self.match(ExprParser.ID)
                self.state = 273
                self.match(ExprParser.RPAREN)
                self.state = 274
                self.match(ExprParser.LCURLY)
                self.state = 286
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==12:
                    self.state = 275
                    self.match(ExprParser.CASE)
                    self.state = 276
                    self.match(ExprParser.INT)
                    self.state = 277
                    self.match(ExprParser.COLON)
                    self.state = 281
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while (((_la) & ~0x3f) == 0 and ((1 << _la) & 824650623950) != 0):
                        self.state = 278
                        self.stat()
                        self.state = 283
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 288
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 289
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

        def getRuleIndex(self):
            return ExprParser.RULE_func

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc" ):
                listener.enterFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc" ):
                listener.exitFunc(self)




    def func(self):

        localctx = ExprParser.FuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_func)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 292
            self.match(ExprParser.ID)
            self.state = 293
            self.match(ExprParser.LPAREN)
            self.state = 294
            self.expr(0)
            self.state = 299
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==26:
                self.state = 295
                self.match(ExprParser.COMMA)
                self.state = 296
                self.expr(0)
                self.state = 301
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 302
            self.match(ExprParser.RPAREN)
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
         




