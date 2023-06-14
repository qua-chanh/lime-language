from .base import Base
from antlr4 import *
from lime.ParserListener import ParserListener


class NamedFunctionListener(ParserListener):

    def __init__(self):
        self.tokens = []

    def exitNamedFunctionDeclaration(self, ctx):
        self.ctx = ctx


class TestNamedFunction(Base):
    fname = "named_function/named_function.l"

    def test_parsed(self):
        printer = NamedFunctionListener()
        walker = ParseTreeWalker()
        walker.walk(printer, self.tree)

        self.assertEqual(printer.ctx.identifier().getText(), "min_age")


class TestNamedFunctionWithGuard(Base):
    fname = "named_function/named_function_with_guard.l"

    def test_parsed(self):
        printer = NamedFunctionListener()
        walker = ParseTreeWalker()
        walker.walk(printer, self.tree)

        self.assertEqual(printer.ctx.identifier().getText(), "min_age")
