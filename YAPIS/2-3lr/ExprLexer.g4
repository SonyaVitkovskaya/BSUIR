lexer grammar ExprLexer;

NODE : 'node';
GRAPH : 'graph';
ARC: 'arc';
N_ELEM : 'nodes';
A_ELEM : 'arcs';
TYPE_INT: 'int';

FOR : 'for' ;
WHILE : 'while' ;
IF : 'if' ;
ELSE : 'else' ;
SWITCH : 'switch' ;
CASE : 'case' ;
BREAK : 'break' ;
RETURN : 'return' ;
CONTINUE : 'continue' ;
FUNCTION : 'function' ;

UNION : '+' ;
DIFF : '-' ;
SYMDIFF : '/' ;
INTERSEC : '&' ;
CART : '*' ;

AND : 'and' ;
OR : 'or' ;
NOT : 'not' ;
EQ : '=' ;
COMMA : ',' ;
SEMI : ';' ;
COLON : ':' ;
EXCLAM : '!' ;

LSQUARE : '[' ;
RSQUARE : ']' ;
LANGLE : '<' ;
RANGLE : '>' ;
LPAREN : '(' ;
RPAREN : ')' ;
LCURLY : '{' ;
RCURLY : '}' ;

INT : [0-9]+ ;
ID: [a-zA-Z_][a-zA-Z_0-9]* ;
WS: [ \t\n\r\f]+ -> skip ;
