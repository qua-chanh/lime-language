# Generated from Parser.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .Parser import Parser
else:
    from Parser import Parser

# This class defines a complete listener for a parse tree produced by Parser.
class ParserListener(ParseTreeListener):

    # Enter a parse tree produced by Parser#module.
    def enterModule(self, ctx:Parser.ModuleContext):
        pass

    # Exit a parse tree produced by Parser#module.
    def exitModule(self, ctx:Parser.ModuleContext):
        pass


    # Enter a parse tree produced by Parser#namedFunctionDeclaration.
    def enterNamedFunctionDeclaration(self, ctx:Parser.NamedFunctionDeclarationContext):
        pass

    # Exit a parse tree produced by Parser#namedFunctionDeclaration.
    def exitNamedFunctionDeclaration(self, ctx:Parser.NamedFunctionDeclarationContext):
        pass


    # Enter a parse tree produced by Parser#anonymousFunctionDeclaration.
    def enterAnonymousFunctionDeclaration(self, ctx:Parser.AnonymousFunctionDeclarationContext):
        pass

    # Exit a parse tree produced by Parser#anonymousFunctionDeclaration.
    def exitAnonymousFunctionDeclaration(self, ctx:Parser.AnonymousFunctionDeclarationContext):
        pass


    # Enter a parse tree produced by Parser#functionArms.
    def enterFunctionArms(self, ctx:Parser.FunctionArmsContext):
        pass

    # Exit a parse tree produced by Parser#functionArms.
    def exitFunctionArms(self, ctx:Parser.FunctionArmsContext):
        pass


    # Enter a parse tree produced by Parser#functionArm.
    def enterFunctionArm(self, ctx:Parser.FunctionArmContext):
        pass

    # Exit a parse tree produced by Parser#functionArm.
    def exitFunctionArm(self, ctx:Parser.FunctionArmContext):
        pass


    # Enter a parse tree produced by Parser#functionParameter.
    def enterFunctionParameter(self, ctx:Parser.FunctionParameterContext):
        pass

    # Exit a parse tree produced by Parser#functionParameter.
    def exitFunctionParameter(self, ctx:Parser.FunctionParameterContext):
        pass


    # Enter a parse tree produced by Parser#functionType.
    def enterFunctionType(self, ctx:Parser.FunctionTypeContext):
        pass

    # Exit a parse tree produced by Parser#functionType.
    def exitFunctionType(self, ctx:Parser.FunctionTypeContext):
        pass


    # Enter a parse tree produced by Parser#type.
    def enterType(self, ctx:Parser.TypeContext):
        pass

    # Exit a parse tree produced by Parser#type.
    def exitType(self, ctx:Parser.TypeContext):
        pass


    # Enter a parse tree produced by Parser#functionBlock.
    def enterFunctionBlock(self, ctx:Parser.FunctionBlockContext):
        pass

    # Exit a parse tree produced by Parser#functionBlock.
    def exitFunctionBlock(self, ctx:Parser.FunctionBlockContext):
        pass


    # Enter a parse tree produced by Parser#statement.
    def enterStatement(self, ctx:Parser.StatementContext):
        pass

    # Exit a parse tree produced by Parser#statement.
    def exitStatement(self, ctx:Parser.StatementContext):
        pass


    # Enter a parse tree produced by Parser#assignExpression.
    def enterAssignExpression(self, ctx:Parser.AssignExpressionContext):
        pass

    # Exit a parse tree produced by Parser#assignExpression.
    def exitAssignExpression(self, ctx:Parser.AssignExpressionContext):
        pass


    # Enter a parse tree produced by Parser#caseExpression.
    def enterCaseExpression(self, ctx:Parser.CaseExpressionContext):
        pass

    # Exit a parse tree produced by Parser#caseExpression.
    def exitCaseExpression(self, ctx:Parser.CaseExpressionContext):
        pass


    # Enter a parse tree produced by Parser#caseArm.
    def enterCaseArm(self, ctx:Parser.CaseArmContext):
        pass

    # Exit a parse tree produced by Parser#caseArm.
    def exitCaseArm(self, ctx:Parser.CaseArmContext):
        pass


    # Enter a parse tree produced by Parser#condExpression.
    def enterCondExpression(self, ctx:Parser.CondExpressionContext):
        pass

    # Exit a parse tree produced by Parser#condExpression.
    def exitCondExpression(self, ctx:Parser.CondExpressionContext):
        pass


    # Enter a parse tree produced by Parser#condArm.
    def enterCondArm(self, ctx:Parser.CondArmContext):
        pass

    # Exit a parse tree produced by Parser#condArm.
    def exitCondArm(self, ctx:Parser.CondArmContext):
        pass


    # Enter a parse tree produced by Parser#guard_clause.
    def enterGuard_clause(self, ctx:Parser.Guard_clauseContext):
        pass

    # Exit a parse tree produced by Parser#guard_clause.
    def exitGuard_clause(self, ctx:Parser.Guard_clauseContext):
        pass


    # Enter a parse tree produced by Parser#guard_expression.
    def enterGuard_expression(self, ctx:Parser.Guard_expressionContext):
        pass

    # Exit a parse tree produced by Parser#guard_expression.
    def exitGuard_expression(self, ctx:Parser.Guard_expressionContext):
        pass


    # Enter a parse tree produced by Parser#expression.
    def enterExpression(self, ctx:Parser.ExpressionContext):
        pass

    # Exit a parse tree produced by Parser#expression.
    def exitExpression(self, ctx:Parser.ExpressionContext):
        pass


    # Enter a parse tree produced by Parser#comparisonOperator.
    def enterComparisonOperator(self, ctx:Parser.ComparisonOperatorContext):
        pass

    # Exit a parse tree produced by Parser#comparisonOperator.
    def exitComparisonOperator(self, ctx:Parser.ComparisonOperatorContext):
        pass


    # Enter a parse tree produced by Parser#literalExpression.
    def enterLiteralExpression(self, ctx:Parser.LiteralExpressionContext):
        pass

    # Exit a parse tree produced by Parser#literalExpression.
    def exitLiteralExpression(self, ctx:Parser.LiteralExpressionContext):
        pass


    # Enter a parse tree produced by Parser#tupleLiteralExpression.
    def enterTupleLiteralExpression(self, ctx:Parser.TupleLiteralExpressionContext):
        pass

    # Exit a parse tree produced by Parser#tupleLiteralExpression.
    def exitTupleLiteralExpression(self, ctx:Parser.TupleLiteralExpressionContext):
        pass


    # Enter a parse tree produced by Parser#identifier.
    def enterIdentifier(self, ctx:Parser.IdentifierContext):
        pass

    # Exit a parse tree produced by Parser#identifier.
    def exitIdentifier(self, ctx:Parser.IdentifierContext):
        pass


    # Enter a parse tree produced by Parser#atom.
    def enterAtom(self, ctx:Parser.AtomContext):
        pass

    # Exit a parse tree produced by Parser#atom.
    def exitAtom(self, ctx:Parser.AtomContext):
        pass


    # Enter a parse tree produced by Parser#keyword.
    def enterKeyword(self, ctx:Parser.KeywordContext):
        pass

    # Exit a parse tree produced by Parser#keyword.
    def exitKeyword(self, ctx:Parser.KeywordContext):
        pass



del Parser