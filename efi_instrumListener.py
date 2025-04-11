# Generated from efi_instrum.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .efi_instrumParser import efi_instrumParser
else:
    from efi_instrumParser import efi_instrumParser

# This class defines a complete listener for a parse tree produced by efi_instrumParser.
class efi_instrumListener(ParseTreeListener):

    # Enter a parse tree produced by efi_instrumParser#start.
    def enterStart(self, ctx:efi_instrumParser.StartContext):
        pass

    # Exit a parse tree produced by efi_instrumParser#start.
    def exitStart(self, ctx:efi_instrumParser.StartContext):
        pass


    # Enter a parse tree produced by efi_instrumParser#main.
    def enterMain(self, ctx:efi_instrumParser.MainContext):
        pass

    # Exit a parse tree produced by efi_instrumParser#main.
    def exitMain(self, ctx:efi_instrumParser.MainContext):
        pass


    # Enter a parse tree produced by efi_instrumParser#efi_main.
    def enterEfi_main(self, ctx:efi_instrumParser.Efi_mainContext):
        pass

    # Exit a parse tree produced by efi_instrumParser#efi_main.
    def exitEfi_main(self, ctx:efi_instrumParser.Efi_mainContext):
        pass


    # Enter a parse tree produced by efi_instrumParser#waitForKey.
    def enterWaitForKey(self, ctx:efi_instrumParser.WaitForKeyContext):
        pass

    # Exit a parse tree produced by efi_instrumParser#waitForKey.
    def exitWaitForKey(self, ctx:efi_instrumParser.WaitForKeyContext):
        pass


    # Enter a parse tree produced by efi_instrumParser#conditionalBranch.
    def enterConditionalBranch(self, ctx:efi_instrumParser.ConditionalBranchContext):
        pass

    # Exit a parse tree produced by efi_instrumParser#conditionalBranch.
    def exitConditionalBranch(self, ctx:efi_instrumParser.ConditionalBranchContext):
        pass


    # Enter a parse tree produced by efi_instrumParser#bootkit_hook_call.
    def enterBootkit_hook_call(self, ctx:efi_instrumParser.Bootkit_hook_callContext):
        pass

    # Exit a parse tree produced by efi_instrumParser#bootkit_hook_call.
    def exitBootkit_hook_call(self, ctx:efi_instrumParser.Bootkit_hook_callContext):
        pass


    # Enter a parse tree produced by efi_instrumParser#resetSystem_call.
    def enterResetSystem_call(self, ctx:efi_instrumParser.ResetSystem_callContext):
        pass

    # Exit a parse tree produced by efi_instrumParser#resetSystem_call.
    def exitResetSystem_call(self, ctx:efi_instrumParser.ResetSystem_callContext):
        pass



del efi_instrumParser