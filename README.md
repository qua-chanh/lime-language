# Lime Language

## Build

```
$ antlr4 -Dlanguage=Python3 Lexer.g4 Parser.g4 -visitor -o lime
```

## Test

```
$ python -m unittest
```