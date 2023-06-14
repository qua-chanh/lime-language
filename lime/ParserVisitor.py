# Generated from Parser.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .Parser import Parser
else:
    from Parser import Parser

# This class defines a complete generic visitor for a parse tree produced by Parser.

class ParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by Parser#module.
    def visitModule(self, ctx:Parser.ModuleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Parser#namedFunctionDeclaration.
    def visitNamedFunctionDeclaration(self, ctx:Parser.NamedFunctionDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Parser#anonymousFunctionDeclaration.
    def visitAnonymousFunctionDeclaration(self, ctx:Parser.AnonymousFunctionDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Parser#functionArms.
    def visitFunctionArms(self, ctx:Parser.FunctionArmsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Parser#functionArm.
    def visitFunctionArm(self, ctx:Parser.FunctionArmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Parser#functionParameter.
    def visitFunctionParameter(self, ctx:Parser.FunctionParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Parser#functionType.
    def visitFunctionType(self, ctx:Parser.FunctionTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Parser#type.
    def visitType(self, ctx:Parser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Parser#functionBlock.
    def visitFunctionBlock(self, ctx:Parser.FunctionBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Parser#statement.
    def visitStatement(self, ctx:Parser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Parser#assignExpression.
    def visitAssignExpression(self, ctx:Parser.AssignExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Parser#caseExpression.
    def visitCaseExpression(self, ctx:Parser.CaseExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Parser#caseArm.
    def visitCaseArm(self, ctx:Parser.CaseArmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Parser#condExpression.
    def visitCondExpression(self, ctx:Parser.CondExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Parser#condArm.
    def visitCondArm(self, ctx:Parser.CondArmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Parser#guard_clause.
    def visitGuard_clause(self, ctx:Parser.Guard_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Parser#guard_expression.
    def visitGuard_expression(self, ctx:Parser.Guard_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Parser#expression.
    def visitExpression(self, ctx:Parser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Parser#comparisonOperator.
    def visitComparisonOperator(self, ctx:Parser.ComparisonOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Parser#literalExpression.
    def visitLiteralExpression(self, ctx:Parser.LiteralExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Parser#tupleLiteralExpression.
    def visitTupleLiteralExpression(self, ctx:Parser.TupleLiteralExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Parser#identifier.
    def visitIdentifier(self, ctx:Parser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Parser#atom.
    def visitAtom(self, ctx:Parser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Parser#keyword.
    def visitKeyword(self, ctx:Parser.KeywordContext):
        return self.visitChildren(ctx)



del Parser