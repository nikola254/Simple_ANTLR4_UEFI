# Generated from efi_instrum.g4 by ANTLR 4.13.2
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
        4,1,11,46,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,1,0,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,3,2,34,8,2,1,2,1,2,1,3,1,3,1,4,1,4,1,5,1,5,1,6,1,6,
        1,6,0,0,7,0,2,4,6,8,10,12,0,0,39,0,14,1,0,0,0,2,16,1,0,0,0,4,20,
        1,0,0,0,6,37,1,0,0,0,8,39,1,0,0,0,10,41,1,0,0,0,12,43,1,0,0,0,14,
        15,3,2,1,0,15,1,1,0,0,0,16,17,5,1,0,0,17,18,3,4,2,0,18,19,5,2,0,
        0,19,3,1,0,0,0,20,21,5,3,0,0,21,22,3,6,3,0,22,23,5,4,0,0,23,24,5,
        5,0,0,24,33,3,8,4,0,25,26,5,7,0,0,26,27,3,10,5,0,27,28,5,8,0,0,28,
        34,1,0,0,0,29,30,5,9,0,0,30,31,3,12,6,0,31,32,5,10,0,0,32,34,1,0,
        0,0,33,25,1,0,0,0,33,29,1,0,0,0,34,35,1,0,0,0,35,36,5,6,0,0,36,5,
        1,0,0,0,37,38,1,0,0,0,38,7,1,0,0,0,39,40,1,0,0,0,40,9,1,0,0,0,41,
        42,1,0,0,0,42,11,1,0,0,0,43,44,1,0,0,0,44,13,1,0,0,0,1,33
    ]

class efi_instrumParser ( Parser ):

    grammarFileName = "efi_instrum.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'ENTER_main'", "'EXIT_main'", "'ENTER_key'", 
                     "'EXIT_key'", "'ENTER_conditional'", "'EXIT_conditional'", 
                     "'ENTER_hook'", "'EXIT_hook'", "'ENTER_reset'", "'EXIT_reset'" ]

    symbolicNames = [ "<INVALID>", "TRACE_ENTER1", "TRACE_EXIT1", "TRACE_ENTER2", 
                      "TRACE_EXIT2", "TRACE_ENTER3", "TRACE_EXIT3", "TRACE_ENTER4", 
                      "TRACE_EXIT4", "TRACE_ENTER5", "TRACE_EXIT5", "WS" ]

    RULE_start = 0
    RULE_main = 1
    RULE_efi_main = 2
    RULE_waitForKey = 3
    RULE_conditionalBranch = 4
    RULE_bootkit_hook_call = 5
    RULE_resetSystem_call = 6

    ruleNames =  [ "start", "main", "efi_main", "waitForKey", "conditionalBranch", 
                   "bootkit_hook_call", "resetSystem_call" ]

    EOF = Token.EOF
    TRACE_ENTER1=1
    TRACE_EXIT1=2
    TRACE_ENTER2=3
    TRACE_EXIT2=4
    TRACE_ENTER3=5
    TRACE_EXIT3=6
    TRACE_ENTER4=7
    TRACE_EXIT4=8
    TRACE_ENTER5=9
    TRACE_EXIT5=10
    WS=11

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

        def main(self):
            return self.getTypedRuleContext(efi_instrumParser.MainContext,0)


        def getRuleIndex(self):
            return efi_instrumParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)




    def start(self):

        localctx = efi_instrumParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self.main()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MainContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRACE_ENTER1(self):
            return self.getToken(efi_instrumParser.TRACE_ENTER1, 0)

        def efi_main(self):
            return self.getTypedRuleContext(efi_instrumParser.Efi_mainContext,0)


        def TRACE_EXIT1(self):
            return self.getToken(efi_instrumParser.TRACE_EXIT1, 0)

        def getRuleIndex(self):
            return efi_instrumParser.RULE_main

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMain" ):
                listener.enterMain(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMain" ):
                listener.exitMain(self)




    def main(self):

        localctx = efi_instrumParser.MainContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_main)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            self.match(efi_instrumParser.TRACE_ENTER1)
            self.state = 17
            self.efi_main()
            self.state = 18
            self.match(efi_instrumParser.TRACE_EXIT1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Efi_mainContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRACE_ENTER2(self):
            return self.getToken(efi_instrumParser.TRACE_ENTER2, 0)

        def waitForKey(self):
            return self.getTypedRuleContext(efi_instrumParser.WaitForKeyContext,0)


        def TRACE_EXIT2(self):
            return self.getToken(efi_instrumParser.TRACE_EXIT2, 0)

        def TRACE_ENTER3(self):
            return self.getToken(efi_instrumParser.TRACE_ENTER3, 0)

        def conditionalBranch(self):
            return self.getTypedRuleContext(efi_instrumParser.ConditionalBranchContext,0)


        def TRACE_EXIT3(self):
            return self.getToken(efi_instrumParser.TRACE_EXIT3, 0)

        def TRACE_ENTER4(self):
            return self.getToken(efi_instrumParser.TRACE_ENTER4, 0)

        def bootkit_hook_call(self):
            return self.getTypedRuleContext(efi_instrumParser.Bootkit_hook_callContext,0)


        def TRACE_EXIT4(self):
            return self.getToken(efi_instrumParser.TRACE_EXIT4, 0)

        def TRACE_ENTER5(self):
            return self.getToken(efi_instrumParser.TRACE_ENTER5, 0)

        def resetSystem_call(self):
            return self.getTypedRuleContext(efi_instrumParser.ResetSystem_callContext,0)


        def TRACE_EXIT5(self):
            return self.getToken(efi_instrumParser.TRACE_EXIT5, 0)

        def getRuleIndex(self):
            return efi_instrumParser.RULE_efi_main

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEfi_main" ):
                listener.enterEfi_main(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEfi_main" ):
                listener.exitEfi_main(self)




    def efi_main(self):

        localctx = efi_instrumParser.Efi_mainContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_efi_main)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self.match(efi_instrumParser.TRACE_ENTER2)
            self.state = 21
            self.waitForKey()
            self.state = 22
            self.match(efi_instrumParser.TRACE_EXIT2)
            self.state = 23
            self.match(efi_instrumParser.TRACE_ENTER3)
            self.state = 24
            self.conditionalBranch()
            self.state = 33
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.state = 25
                self.match(efi_instrumParser.TRACE_ENTER4)
                self.state = 26
                self.bootkit_hook_call()
                self.state = 27
                self.match(efi_instrumParser.TRACE_EXIT4)
                pass
            elif token in [9]:
                self.state = 29
                self.match(efi_instrumParser.TRACE_ENTER5)
                self.state = 30
                self.resetSystem_call()
                self.state = 31
                self.match(efi_instrumParser.TRACE_EXIT5)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 35
            self.match(efi_instrumParser.TRACE_EXIT3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WaitForKeyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return efi_instrumParser.RULE_waitForKey

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWaitForKey" ):
                listener.enterWaitForKey(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWaitForKey" ):
                listener.exitWaitForKey(self)




    def waitForKey(self):

        localctx = efi_instrumParser.WaitForKeyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_waitForKey)
        try:
            self.enterOuterAlt(localctx, 1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionalBranchContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return efi_instrumParser.RULE_conditionalBranch

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditionalBranch" ):
                listener.enterConditionalBranch(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditionalBranch" ):
                listener.exitConditionalBranch(self)




    def conditionalBranch(self):

        localctx = efi_instrumParser.ConditionalBranchContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_conditionalBranch)
        try:
            self.enterOuterAlt(localctx, 1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Bootkit_hook_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return efi_instrumParser.RULE_bootkit_hook_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBootkit_hook_call" ):
                listener.enterBootkit_hook_call(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBootkit_hook_call" ):
                listener.exitBootkit_hook_call(self)




    def bootkit_hook_call(self):

        localctx = efi_instrumParser.Bootkit_hook_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_bootkit_hook_call)
        try:
            self.enterOuterAlt(localctx, 1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ResetSystem_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return efi_instrumParser.RULE_resetSystem_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterResetSystem_call" ):
                listener.enterResetSystem_call(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitResetSystem_call" ):
                listener.exitResetSystem_call(self)




    def resetSystem_call(self):

        localctx = efi_instrumParser.ResetSystem_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_resetSystem_call)
        try:
            self.enterOuterAlt(localctx, 1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





