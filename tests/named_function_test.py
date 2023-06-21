from .base import Base
from antlr4 import *
from lime.ParserListener import ParserListener


class NamedFunctionListener(ParserListener):
    def __init__(self):
        self.tokens = []

    def exitNamedFunction(self, ctx):
        self.ctx = ctx


class TestNamedFunction(Base):
    fname = "named_function/one_arm.lm"

    def test_parsed(self):
        printer = NamedFunctionListener()
        walker = ParseTreeWalker()
        walker.walk(printer, self.tree)

        self.assertEqual(printer.ctx.identifier().getText(), "validate_age")


class TestNamedFunctionWithGuard(Base):
    fname = "named_function/two_arms.lm"

    def test_parsed(self):
        printer = NamedFunctionListener()
        walker = ParseTreeWalker()
        walker.walk(printer, self.tree)

        self.assertEqual(printer.ctx.identifier().getText(), "validate_age")


class TestNamedFunctionWithTwoArgs(Base):
    fname = "named_function/two_arms_one_guard.lm"

    def test_parsed(self):
        printer = NamedFunctionListener()
        walker = ParseTreeWalker()
        walker.walk(printer, self.tree)

        self.assertEqual(printer.ctx.identifier().getText(), "validate_age")


class TestNamedFunctionNoReturn(Base):
    fname = "named_function/no_return.lm"

    def test_parsed(self):
        printer = NamedFunctionListener()
        walker = ParseTreeWalker()
        walker.walk(printer, self.tree)

        self.assertEqual(printer.ctx.identifier().getText(), "return_empty")