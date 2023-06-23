from .base import Base
from antlr4 import *
from lime.ParserListener import ParserListener


class StructListener(ParserListener):
    def __init__(self):
        self.tokens = []

    def exitStruct(self, ctx):
        self.ctx = ctx


class TestColor(Base):
    fname = "struct/color.lm"

    def test_parsed(self):
        printer = StructListener()
        walker = ParseTreeWalker()
        walker.walk(printer, self.tree)

        self.assertEqual(printer.ctx.atom().getText(), "Color")
