grammar SanyaScript;

// parser rules
sanyaScript: statement* EOF;

statement: defvar
         | assignment
         | print;

assignment: defvar EQUALS (cast)? value # assign
          | ID EQUALS (cast)? value     # reassign;

cast: '(' type ')';

defvar: NODE_TYPE ID  # defnode
      | ARC_TYPE ID   # defarc
      | GRAPH_TYPE ID # defgraph;

arc: '->'            # simpleArc
   | '<->'           # simpleUndirectedArc
   | '-[' INT ']->'  # weightedArc
   | '<-[' INT ']->' # weightedUndirectedArc;

value: INT                        # nodeValue
     | arcPart arc arcPart        # arcValue
     | '[' (value ',')* value ']' # graphValue
     | ID                         # idValue;

arcPart: INT | ID;

type: NODE_TYPE
    | ARC_TYPE
    | GRAPH_TYPE;

print: PRINT ID;

// lexer rules
NODE_TYPE: 'node' ;
ARC_TYPE: 'arc' ;
GRAPH_TYPE: 'graph' ;

PRINT: 'print' ;
EQUALS: '=' ;
PLUS: '+' ;
MINUS: '-' ;
MULT: '*' ;
DIV: '/' ;

INT: [1-9][0-9]* ;

ID: [a-z][a-zA-Z0-9]* ;
WS: [ \t\r\n]+ -> skip ;
COMMENT: '#' ~[\n]+  -> skip ;
