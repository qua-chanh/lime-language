from .base import Base
from antlr4 import *
from lime.ParserListener import ParserListener


class CondListener(ParserListener):
    def __init__(self):
        self.tokens = []

    def exitNamedFunction(self, ctx):
        self.ctx = ctx


class TestNamedFunction(Base):
    fname = "cond/two_arms.lm"

    def test_parsed(self):
        printer = CondListener()
        walker = ParseTreeWalker()
        walker.walk(printer, self.tree)

        self.assertEqual(printer.ctx.identifier().getText(), "validate_age")
