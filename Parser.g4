parser grammar Parser;

options {
	tokenVocab = Lexer;
}

module: (namedFunction)* EOF;

namedFunction: KW_FN identifier functionArms;

anonymousFunction: KW_FN functionArms;

functionArms: (functionArm)+;

functionArm:
	'(' (functionParameter (',' functionParameter)*)? ')' functionType? guard_clause? ':' block
		KW_END;

functionParameter: (identifier type | literalExpression | '_');

functionType: '->' type;

type: atom | atom '<' atom (',' atom)* '>' | typeFunction;

typeFunction: '(' atom (',' atom)* ')' '->' atom;

statement: expression;

assignExpression: identifier '=' expression;

caseExpression: KW_CASE expression ':' (caseArm)+ KW_END;

caseArm: (literalExpression | tupleLiteralExpression) ':' block KW_END;

condExpression: KW_COND ':' (condArm)+ KW_END;

condArm: expression ':' block KW_END;

block: (expression)*;

guard_clause: 'guard' guard_expression;

guard_expression:
	identifier
	| identifier comparisonOperator (
		identifier
		| literalExpression
	);

expression:
	identifier
	| atom
	| anonymousFunction
	| literalExpression
	| caseExpression
	| condExpression
	| assignExpression
	| expression ('*' | '/' | '%') expression
	| expression ('+' | '-') expression
	| expression comparisonOperator expression
	| '[' (expression (',' expression)*)? ']'
	| '(' expression (',' expression)* ')'
	| '{' (
		STRING_LITERAL ':' expression (
			',' STRING_LITERAL ':' expression
		)*
	)? '}';

comparisonOperator: '==' | '!=' | '>' | '<' | '>=' | '<=';

literalExpression:
	STRING_LITERAL
	| INTEGER_LITERAL
	| FLOAT_LITERAL;

tupleLiteralExpression:
	'(' literalExpression (',' literalExpression)* ')';

identifier: NON_KEYWORD_IDENTIFIER;

atom: ATOM;

keyword: KW_FN | KW_END | KW_CASE | KW_COND;