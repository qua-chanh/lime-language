parser grammar Parser;

options {
	tokenVocab = Lexer;
}

module: (namedFunctionDeclaration)* EOF;

namedFunctionDeclaration: KW_FN identifier functionArms KW_END;

anonymousFunctionDeclaration: KW_FN functionArms KW_END;

functionArms: (functionArm)+;

functionArm:
	'(' (functionParameter (',' functionParameter)*)? ')' functionType? guard_clause? ':'
		functionBlock;

functionParameter: (identifier | literalExpression | '_') type;

functionType: '->' type;

type: atom;

functionBlock: (statement)*;

statement: expression;

assignExpression: identifier '=' expression;

caseExpression: KW_CASE expression ':' (caseArm)+ KW_END;

caseArm: (literalExpression | tupleLiteralExpression) '->' KW_END;

condExpression: KW_COND ':' (condArm)+ KW_END;

condArm: expression '->' KW_END;

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
	| anonymousFunctionDeclaration
	| literalExpression
	| caseExpression
	| condExpression
	| assignExpression
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