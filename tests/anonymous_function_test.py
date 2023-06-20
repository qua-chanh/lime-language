from .base import Base
from antlr4 import *
from lime.ParserListener import ParserListener


class AnonymousFunctionListener(ParserListener):
    def __init__(self):
        self.tokens = []

    def exitAnonymousFunction(self, ctx):
        self.anonymous_function_ctx = ctx

    def exitNamedFunction(self, ctx):
        self.named_function_ctx = ctx


class TestAnonymousOneArm(Base):
    fname = "anonymous_function/one_arm.lm"

    def test_parsed(self):
        printer = AnonymousFunctionListener()
        walker = ParseTreeWalker()
        walker.walk(printer, self.tree)

        self.assertEqual(
            len(printer.anonymous_function_ctx.functionArms().functionArm()), 1
        )


class TestAnonymousAsArgument(Base):
    fname = "anonymous_function/argument.lm"

    def test_parsed(self):
        printer = AnonymousFunctionListener()
        walker = ParseTreeWalker()
        walker.walk(printer, self.tree)

        self.assertEqual(printer.named_function_ctx.identifier().getText(), "operate")


class TestAnonymousAsReturn(Base):
    fname = "anonymous_function/return.lm"

    def test_parsed(self):
        printer = AnonymousFunctionListener()
        walker = ParseTreeWalker()
        walker.walk(printer, self.tree)

        self.assertEqual(
            printer.named_function_ctx.identifier().getText(), "generate_operator"
        )
