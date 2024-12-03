# Generated from UEFI.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .UEFIParser import UEFIParser
else:
    from UEFIParser import UEFIParser

# This class defines a complete listener for a parse tree produced by UEFIParser.
class UEFIListener(ParseTreeListener):

    # Enter a parse tree produced by UEFIParser#compilationUnit.
    def enterCompilationUnit(self, ctx:UEFIParser.CompilationUnitContext):
        print("Entering compilation unit")

    # Exit a parse tree produced by UEFIParser#compilationUnit.
    def exitCompilationUnit(self, ctx:UEFIParser.CompilationUnitContext):
        print("Exiting compilation unit")


    # Enter a parse tree produced by UEFIParser#statement.
    def enterStatement(self, ctx:UEFIParser.StatementContext):
        print("Entering statement")

    # Exit a parse tree produced by UEFIParser#statement.
    def exitStatement(self, ctx:UEFIParser.StatementContext):
        print("Exiting statement")


    # Enter a parse tree produced by UEFIParser#includeStatement.
    def enterIncludeStatement(self, ctx:UEFIParser.IncludeStatementContext):
        print(f"Including file: {ctx.STRING().getText()}")

    # Exit a parse tree produced by UEFIParser#includeStatement.
    def exitIncludeStatement(self, ctx:UEFIParser.IncludeStatementContext):
        pass


    # Enter a parse tree produced by UEFIParser#variableDeclaration.
    def enterVariableDeclaration(self, ctx:UEFIParser.VariableDeclarationContext):
            # Извлечение типа переменной
        var_type = ctx.type_().getText() if ctx.type_() is not None else "Unknown type"
        
        # Извлечение указателя, если он есть
        var_pointer = ctx.cursor().getText() if ctx.cursor() is not None else ""
        
        # Извлечение имени переменной
        var_name = ctx.identifier().getText() if ctx.identifier() is not None else "No identifier"
        
        # Извлечение выражения, если оно есть
        var_expression = ctx.expression().getText() if ctx.expression() is not None else "No expression"
        
        # Вывод информации о переменной
        print(f"Variable declaration: {var_type} {var_pointer} {var_name} = {var_expression}")

    # Exit a parse tree produced by UEFIParser#variableDeclaration.
    def exitVariableDeclaration(self, ctx:UEFIParser.VariableDeclarationContext):
        identifier = ctx.identifier()
        if identifier is not None:
            print(f"Exiting variable declaration: {identifier.getText()}")
        else:
            print("No identifier found in variable declaration context.")


    # Enter a parse tree produced by UEFIParser#functionDeclaration.
    def enterFunctionDeclaration(self, ctx:UEFIParser.FunctionDeclarationContext):
        print(f"Entering function: {ctx.identifier().getText()}")

    # Exit a parse tree produced by UEFIParser#functionDeclaration.
    def exitFunctionDeclaration(self, ctx:UEFIParser.FunctionDeclarationContext):
        print(f"Exiting function: {ctx.identifier().getText()}")


    # Enter a parse tree produced by UEFIParser#parameterList.
    def enterParameterList(self, ctx:UEFIParser.ParameterListContext):
        print("Entering parameter list")

    # Exit a parse tree produced by UEFIParser#parameterList.
    def exitParameterList(self, ctx:UEFIParser.ParameterListContext):
        print("Exiting parameter list")


    # Enter a parse tree produced by UEFIParser#parametr.
    def enterParametr(self, ctx:UEFIParser.ParametrContext):
        if ctx.identifier() is not None:
            param_name = ctx.identifier().getText()
            print(f"Parameter name: {param_name}")
        else:
            print("No identifier found in parameter context.")

    # Exit a parse tree produced by UEFIParser#parametr.
    def exitParametr(self, ctx:UEFIParser.ParametrContext):
        pass


    # Enter a parse tree produced by UEFIParser#block.
    def enterBlock(self, ctx:UEFIParser.BlockContext):
        print("Entering block")

    # Exit a parse tree produced by UEFIParser#block.
    def exitBlock(self, ctx:UEFIParser.BlockContext):
        print("Exiting block")


    # Enter a parse tree produced by UEFIParser#warning.
    def enterWarning(self, ctx:UEFIParser.WarningContext):
        pass

    # Exit a parse tree produced by UEFIParser#warning.
    def exitWarning(self, ctx:UEFIParser.WarningContext):
        pass


    # Enter a parse tree produced by UEFIParser#expressionStatement.
    def enterExpressionStatement(self, ctx:UEFIParser.ExpressionStatementContext):
        print("Entering expression statement")

    # Exit a parse tree produced by UEFIParser#expressionStatement.
    def exitExpressionStatement(self, ctx:UEFIParser.ExpressionStatementContext):
        print("Exiting expression statement")


    # Enter a parse tree produced by UEFIParser#expression.
    def enterExpression(self, ctx:UEFIParser.ExpressionContext):
        pass

    # Exit a parse tree produced by UEFIParser#expression.
    def exitExpression(self, ctx:UEFIParser.ExpressionContext):
        pass


    # Enter a parse tree produced by UEFIParser#assignmentExpression.
    def enterAssignmentExpression(self, ctx:UEFIParser.AssignmentExpressionContext):
        print("Entering assignment expression")

    # Exit a parse tree produced by UEFIParser#assignmentExpression.
    def exitAssignmentExpression(self, ctx:UEFIParser.AssignmentExpressionContext):
        print("Exiting assignment expression")


    # Enter a parse tree produced by UEFIParser#methodCall.
    def enterMethodCall(self, ctx:UEFIParser.MethodCallContext):
        identifiers = ctx.identifier()
        if identifiers:
            method_name = identifiers[0].getText()  # Access the first identifier
            print(f"Entering method call: {method_name}")
        else:
            print("No identifiers found in method call context.")

    # Exit a parse tree produced by UEFIParser#methodCall.
    def exitMethodCall(self, ctx:UEFIParser.MethodCallContext):
        identifiers = ctx.identifier()
        if identifiers:
            method_name = identifiers[0].getText()  # Access the first identifier
            print(f"Exiting method call: {method_name}")
        else:
            print("No identifiers found in method call context.")

    # Enter a parse tree produced by UEFIParser#argumentList.
    def enterArgumentList(self, ctx:UEFIParser.ArgumentListContext):
        print("Entering argument list")

    # Exit a parse tree produced by UEFIParser#argumentList.
    def exitArgumentList(self, ctx:UEFIParser.ArgumentListContext):
        print("Exiting argument list")


    # Enter a parse tree produced by UEFIParser#whileStatement.
    def enterWhileStatement(self, ctx:UEFIParser.WhileStatementContext):
        print("Entering a while loop")

    # Exit a parse tree produced by UEFIParser#whileStatement.
    def exitWhileStatement(self, ctx:UEFIParser.WhileStatementContext):
        print("Exiting while loop")


    # Enter a parse tree produced by UEFIParser#exit.
    def enterExit(self, ctx:UEFIParser.ExitContext):
        pass

    # Exit a parse tree produced by UEFIParser#exit.
    def exitExit(self, ctx:UEFIParser.ExitContext):
        pass


    # Enter a parse tree produced by UEFIParser#operator.
    def enterOperator(self, ctx:UEFIParser.OperatorContext):
        pass

    # Exit a parse tree produced by UEFIParser#operator.
    def exitOperator(self, ctx:UEFIParser.OperatorContext):
        pass


    # Enter a parse tree produced by UEFIParser#literal.
    def enterLiteral(self, ctx:UEFIParser.LiteralContext):
        print(f"Literal value: {ctx.getText()}")

    # Exit a parse tree produced by UEFIParser#literal.
    def exitLiteral(self, ctx:UEFIParser.LiteralContext):
        pass


    # Enter a parse tree produced by UEFIParser#type.
    def enterType(self, ctx:UEFIParser.TypeContext):
        print(f"Type: {ctx.getText()}")

    # Exit a parse tree produced by UEFIParser#type.
    def exitType(self, ctx:UEFIParser.TypeContext):
        pass


    # Enter a parse tree produced by UEFIParser#identifier.
    def enterIdentifier(self, ctx:UEFIParser.IdentifierContext):
        print(f"Identifier: {ctx.getText()}")

    # Exit a parse tree produced by UEFIParser#identifier.
    def exitIdentifier(self, ctx:UEFIParser.IdentifierContext):
        pass


    # Enter a parse tree produced by UEFIParser#macros.
    def enterMacros(self, ctx:UEFIParser.MacrosContext):
        pass

    # Exit a parse tree produced by UEFIParser#macros.
    def exitMacros(self, ctx:UEFIParser.MacrosContext):
        pass


    # Enter a parse tree produced by UEFIParser#cursor.
    def enterCursor(self, ctx:UEFIParser.CursorContext):
        pass

    # Exit a parse tree produced by UEFIParser#cursor.
    def exitCursor(self, ctx:UEFIParser.CursorContext):
        pass


    # Enter a parse tree produced by UEFIParser#link.
    def enterLink(self, ctx:UEFIParser.LinkContext):
        pass

    # Exit a parse tree produced by UEFIParser#link.
    def exitLink(self, ctx:UEFIParser.LinkContext):
        pass


    # Enter a parse tree produced by UEFIParser#comment.
    def enterComment(self, ctx:UEFIParser.CommentContext):
        print(f"Comment: {ctx.getText()}")

    # Exit a parse tree produced by UEFIParser#comment.
    def exitComment(self, ctx:UEFIParser.CommentContext):
        pass



del UEFIParser