import unittest
import os
from antlr4 import *
from lime.Lexer import Lexer
from lime.Parser import Parser


class Base(unittest.TestCase):

    fname = None

    def setUp(self):
        self.parsed = []
        input = FileStream(os.path.join(
            "samples", self.fname), encoding="utf-8")
        lexer = Lexer(input)
        stream = CommonTokenStream(lexer)
        parser = Parser(stream)
        tree = parser.module()
        self.tree = tree

    def tearDown(self):
        self.parsed = []
