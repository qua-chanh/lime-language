lexer grammar Lexer;

KW_END: 'end';
KW_FN: 'fn';
KW_COND: 'cond';
KW_GUARD: 'guard';

LINE_COMMENT: '//' ~[\r\n]* -> channel(HIDDEN);
BLOCK_COMMENT: '/*' .*? '*/' -> channel(HIDDEN);

WHITESPACE: [\p{Zs}] -> skip;
NEWLINE: '\r'? '\n' -> skip;

NON_KEYWORD_IDENTIFIER: [a-z_][a-zA-Z0-9_]*;
ATOM: [A-Z][a-zA-Z0-9_]*;

STRING_LITERAL: '"' ( ~["] | QUOTE_ESCAPE | ESC_NEWLINE)* '"';
INTEGER_LITERAL: DEC_LITERAL;
FLOAT_LITERAL: DEC_LITERAL ('.' DEC_LITERAL)?;
DEC_LITERAL: DEC_DIGIT+;

fragment QUOTE_ESCAPE: '\\' ['"];
fragment ESC_NEWLINE: '\\' '\n';
fragment DEC_DIGIT: [0-9];

PLUS: '+';
MINUS: '-';
STAR: '*';
SLASH: '/';
PERCENT: '%';
NOT: '!';
AND: '&&';
OR: '||';
PLUSEQ: '+=';
MINUSEQ: '-=';
STARED: '*=';
SLASHEQ: '/=';
PERCENTEQ: '%=';
EQ: '=';
EQEQ: '==';
NE: '!=';
GT: '>';
LT: '<';
GE: '>=';
LE: '<=';
UNDERSCORE: '_';
DOT: '.';
COMMA: ',';
COLON: ':';
PIPE: '|>';
RIGHT_ARROW: '->';
LEFT_ARROW: '<-';

LCURLYBRACE: '{';
RCURLYBRACE: '}';
LSQUAREBRACKET: '[';
RSQUAREBRACKET: ']';
LPAREN: '(';
RPAREN: ')';