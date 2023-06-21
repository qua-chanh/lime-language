parser grammar Parser;

options {
	tokenVocab = Lexer;
}

module: (namedFunction)* EOF;

namedFunction: KW_FN identifier functionArms KW_END;

anonymousFunction: KW_FN functionArms KW_END;

functionArms: (functionArm)+;

functionArm:
	'(' (functionParameter (',' functionParameter)*)? ')' returnType guard? ':' block;

functionParameter: (identifier type | literalExpression | '_');

returnType: '->' type;

cond: KW_COND ':' (condArm)+ KW_END;

condArm: expression returnType ':' block KW_END;

type: atom | typeConstructor | typeFunction;

typeConstructor: atom '<' type (',' type)* '>';

typeFunction: '(' (type (',' type)*)? ')' '->' type;

assignExpression: identifier '=' expression;

block: (expression)*;

guard: 'guard' guardExpression;

guardExpression:
	identifier
	| identifier comparisonOperator (
		identifier
		| literalExpression
	);

callFunctionExpression: (identifier | anonymousFunction) '(' callFunctionParamsExpression? ')';

callFunctionParamsExpression: expression (',' expression)*;

expression:
	identifier
	| atom
	| anonymousFunction
	| literalExpression
	| cond
	| assignExpression
	| callFunctionExpression
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

keyword: KW_FN | KW_END | KW_COND;