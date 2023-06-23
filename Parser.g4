parser grammar Parser;

options {
	tokenVocab = Lexer;
}

module: (statement)* EOF;

statement: namedFunction | struct;

struct:
	KW_STRUCT atom '(' identifierType (',' identifierType)* ')';

namedFunction: KW_FN identifier functionArms;

anonymousFunction: KW_FN functionArms;

functionArms: (functionArm)+;

functionArm:
	'(' (functionParameter (',' functionParameter)*)? ')' returnType guard? ':' block KW_END;

functionParameter: (identifierType | literalExpression | '_');

identifierType: identifier type (defaultValue)?;

defaultValue: '=' literalExpression;

returnType: '->' type;

cond: KW_COND (condArm)+;

condArm: expression returnType ':' block KW_END;

type: atom | typeConstructor | typeFunction | typeVoid;

typeConstructor: atom '<' type (',' type)* '>';

typeFunction: '(' (type (',' type)*)? ')' '->' type;

typeVoid: '(' ')';

assignExpression: identifier '=' expression;

block: (expression)*;

guard: 'guard' guardExpression;

guardExpression:
	identifier
	| identifier comparisonOperator (
		identifier
		| literalExpression
	);

callFunctionExpression:
	identifier callFunctionParams
	| (anonymousFunction | cond | identifier) '<-' (
		callFunctionParams
		| identifier
	);

callFunctionParams: '(' (expression (',' expression)*)? ')';

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

keyword: KW_FN | KW_END | KW_COND | KW_GUARD | KW_STRUCT;