parser grammar ExprParser;
options { tokenVocab=ExprLexer; }

types : NODE
    | ARC
    | GRAPH
    | TYPE_INT
    ;

operation : UNION
    | DIFF
    | SYMDIFF
    | INTERSEC
    | CART
    ;

anoun : types ID
    | TYPE_INT ID '=' INT
    | GRAPH ID '=' expr
    | ARC ID  '=' '<' node COMMA node '>'
    | GRAPH ID '=' '[' N_ELEM ':' '(' (node)? | (node (',' node)*) ')' ',' A_ELEM ':' '(' (arc)?     (arc (',' arc)*) ')' ']'
    ;

node : ID
    | NODE ID
    ;

arc : ID
    | ARC ID  '=' '<' node COMMA node '>' ';'
    | '<' node COMMA node '>'
    ;

program : (stat | anoun)* EOF;

stat: ID '=' expr ';'
    | expr ';'
    | anoun ';'
    | cicle 
    | condition
    | def
    ;

def : 'function' ID '(' (ID)? | (ID (',' ID)*) ')' '{' stat* '}' ;

expr: func
    | expr operation expr 
    | 'not' expr
    | expr 'and' expr
    | expr 'or' expr
    | expr ( ('<' | '>')('=')? | ('!' | '=')'=') expr
    | ID
    | INT
    | BREAK
    | CONTINUE
    | RETURN expr
    ;

cicle : WHILE '(' expr ')' '{' stat* '}'
    | FOR '(' (ID | TYPE_INT ID) '=' expr ';' expr ( ('<' | '>')('=')? | ('!' | '=')'=') expr ';' ID '=' expr ')' '{' stat* '}'
    ;

condition : 
    IF  '(' expr ')' '{' stat*'}' ('else' '{' stat*'}')?
    | SWITCH '(' ID ')' '{' ( CASE INT ':' stat*)* '}' ;

func : ID '(' expr (',' expr)* ')' ;