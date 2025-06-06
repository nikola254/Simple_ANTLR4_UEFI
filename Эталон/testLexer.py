# Generated from test.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,6,49,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,
        0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,5,4,5,44,8,5,
        11,5,12,5,45,1,5,1,5,0,0,6,1,1,3,2,5,3,7,4,9,5,11,6,1,0,1,1,0,65,
        90,49,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,
        0,0,11,1,0,0,0,1,13,1,0,0,0,3,17,1,0,0,0,5,23,1,0,0,0,7,28,1,0,0,
        0,9,35,1,0,0,0,11,43,1,0,0,0,13,14,5,105,0,0,14,15,5,110,0,0,15,
        16,5,116,0,0,16,2,1,0,0,0,17,18,5,115,0,0,18,19,5,104,0,0,19,20,
        5,111,0,0,20,21,5,114,0,0,21,22,5,116,0,0,22,4,1,0,0,0,23,24,5,108,
        0,0,24,25,5,111,0,0,25,26,5,110,0,0,26,27,5,103,0,0,27,6,1,0,0,0,
        28,29,5,115,0,0,29,30,5,116,0,0,30,31,5,114,0,0,31,32,5,105,0,0,
        32,33,5,110,0,0,33,34,5,103,0,0,34,8,1,0,0,0,35,36,5,114,0,0,36,
        37,5,101,0,0,37,38,5,116,0,0,38,39,5,117,0,0,39,40,5,114,0,0,40,
        41,5,110,0,0,41,10,1,0,0,0,42,44,7,0,0,0,43,42,1,0,0,0,44,45,1,0,
        0,0,45,43,1,0,0,0,45,46,1,0,0,0,46,47,1,0,0,0,47,48,6,5,0,0,48,12,
        1,0,0,0,2,0,45,1,1,5,0
    ]

class testLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    IDENTIFIER = 6

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'int'", "'short'", "'long'", "'string'", "'return'" ]

    symbolicNames = [ "<INVALID>",
            "IDENTIFIER" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "IDENTIFIER" ]

    grammarFileName = "test.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[5] = self.IDENTIFIER_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def IDENTIFIER_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
             log("matched rule"); 
     


