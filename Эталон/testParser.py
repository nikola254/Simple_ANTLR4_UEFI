# Generated from test.g4 by ANTLR 4.13.2
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
        4,1,6,50,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,6,
        2,7,7,7,2,8,7,8,2,9,7,9,1,0,1,0,1,0,1,1,4,1,25,8,1,11,1,12,1,26,
        1,2,1,2,1,2,1,3,1,3,1,4,1,4,1,4,1,4,3,4,38,8,4,1,5,1,5,1,6,1,6,1,
        7,1,7,1,8,1,8,1,9,1,9,1,9,0,0,10,0,2,4,6,8,10,12,14,16,18,0,0,43,
        0,20,1,0,0,0,2,24,1,0,0,0,4,28,1,0,0,0,6,31,1,0,0,0,8,37,1,0,0,0,
        10,39,1,0,0,0,12,41,1,0,0,0,14,43,1,0,0,0,16,45,1,0,0,0,18,47,1,
        0,0,0,20,21,3,2,1,0,21,22,3,6,3,0,22,1,1,0,0,0,23,25,3,4,2,0,24,
        23,1,0,0,0,25,26,1,0,0,0,26,24,1,0,0,0,26,27,1,0,0,0,27,3,1,0,0,
        0,28,29,3,8,4,0,29,30,5,6,0,0,30,5,1,0,0,0,31,32,3,18,9,0,32,7,1,
        0,0,0,33,38,3,10,5,0,34,38,3,12,6,0,35,38,3,14,7,0,36,38,3,16,8,
        0,37,33,1,0,0,0,37,34,1,0,0,0,37,35,1,0,0,0,37,36,1,0,0,0,38,9,1,
        0,0,0,39,40,5,1,0,0,40,11,1,0,0,0,41,42,5,2,0,0,42,13,1,0,0,0,43,
        44,5,3,0,0,44,15,1,0,0,0,45,46,5,4,0,0,46,17,1,0,0,0,47,48,5,5,0,
        0,48,19,1,0,0,0,2,26,37
    ]

class testParser ( Parser ):

    grammarFileName = "test.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'int'", "'short'", "'long'", "'string'", 
                     "'return'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "IDENTIFIER" ]

    RULE_start = 0
    RULE_body = 1
    RULE_variable = 2
    RULE_exit = 3
    RULE_type = 4
    RULE_int = 5
    RULE_short = 6
    RULE_long = 7
    RULE_string = 8
    RULE_return = 9

    ruleNames =  [ "start", "body", "variable", "exit", "type", "int", "short", 
                   "long", "string", "return" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    IDENTIFIER=6

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def body(self):
            return self.getTypedRuleContext(testParser.BodyContext,0)


        def exit(self):
            return self.getTypedRuleContext(testParser.ExitContext,0)


        def getRuleIndex(self):
            return testParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)




    def start(self):

        localctx = testParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self.body()
            self.state = 21
            self.exit()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(testParser.VariableContext)
            else:
                return self.getTypedRuleContext(testParser.VariableContext,i)


        def getRuleIndex(self):
            return testParser.RULE_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBody" ):
                listener.enterBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBody" ):
                listener.exitBody(self)




    def body(self):

        localctx = testParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 23
                self.variable()
                self.state = 26 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 30) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(testParser.TypeContext,0)


        def IDENTIFIER(self):
            return self.getToken(testParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return testParser.RULE_variable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable" ):
                listener.enterVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable" ):
                listener.exitVariable(self)




    def variable(self):

        localctx = testParser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.type_()
            self.state = 29
            self.match(testParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def return_(self):
            return self.getTypedRuleContext(testParser.ReturnContext,0)


        def getRuleIndex(self):
            return testParser.RULE_exit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExit" ):
                listener.enterExit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExit" ):
                listener.exitExit(self)




    def exit(self):

        localctx = testParser.ExitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_exit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self.return_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return testParser.RULE_type

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class TypeIntContext(TypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a testParser.TypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def int_(self):
            return self.getTypedRuleContext(testParser.IntContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeInt" ):
                listener.enterTypeInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeInt" ):
                listener.exitTypeInt(self)


    class TypeShortContext(TypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a testParser.TypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def short(self):
            return self.getTypedRuleContext(testParser.ShortContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeShort" ):
                listener.enterTypeShort(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeShort" ):
                listener.exitTypeShort(self)


    class TypeStringContext(TypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a testParser.TypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def string(self):
            return self.getTypedRuleContext(testParser.StringContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeString" ):
                listener.enterTypeString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeString" ):
                listener.exitTypeString(self)


    class TypeLongContext(TypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a testParser.TypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def long(self):
            return self.getTypedRuleContext(testParser.LongContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeLong" ):
                listener.enterTypeLong(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeLong" ):
                listener.exitTypeLong(self)



    def type_(self):

        localctx = testParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_type)
        try:
            self.state = 37
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                localctx = testParser.TypeIntContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 33
                self.int_()
                pass
            elif token in [2]:
                localctx = testParser.TypeShortContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 34
                self.short()
                pass
            elif token in [3]:
                localctx = testParser.TypeLongContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 35
                self.long()
                pass
            elif token in [4]:
                localctx = testParser.TypeStringContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 36
                self.string()
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


    class IntContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return testParser.RULE_int

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt" ):
                listener.enterInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt" ):
                listener.exitInt(self)




    def int_(self):

        localctx = testParser.IntContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_int)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.match(testParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ShortContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return testParser.RULE_short

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterShort" ):
                listener.enterShort(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitShort" ):
                listener.exitShort(self)




    def short(self):

        localctx = testParser.ShortContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_short)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self.match(testParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LongContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return testParser.RULE_long

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLong" ):
                listener.enterLong(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLong" ):
                listener.exitLong(self)




    def long(self):

        localctx = testParser.LongContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_long)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(testParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return testParser.RULE_string

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString" ):
                listener.enterString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString" ):
                listener.exitString(self)




    def string(self):

        localctx = testParser.StringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_string)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.match(testParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return testParser.RULE_return

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturn" ):
                listener.enterReturn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturn" ):
                listener.exitReturn(self)




    def return_(self):

        localctx = testParser.ReturnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_return)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.match(testParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





