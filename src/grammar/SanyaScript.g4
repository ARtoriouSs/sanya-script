grammar SanyaScript;

// parser rules
sanyaScript: statement* EOF;

statement: defvar
         | assignment
         | print;

assignment: defvar EQUALS (cast)? value;

cast: '(' type ')';

defvar: NODE_TYPE ID  # defnode
      | ARC_TYPE ID   # defarc
      | GRAPH_TYPE ID # defgraph
      | ID            # redef;

arc: '->'                                               # simpleArc
   | '<->'                                              # simpleUndirectedArc
   | WEIGHTED_ARC_START INT WEIGHTED_ARC_END            # weightedArc
   | WEIGHTED_UNDIRECTED_ARC_START INT WEIGHTED_ARC_END # weightedUndirectedArc;

value: INT                        # nodeValue
     | (INT | ID) arc (INT | ID)  # arcValue
     | '[' (value ',')* value ']' # graphValue
     | ID                         # idValue;

type: NODE_TYPE
    | ARC_TYPE
    | GRAPH_TYPE;

print: PRINT ID;

// lexer rules
NODE_TYPE: 'node' ;
ARC_TYPE: 'arc' ;
GRAPH_TYPE: 'graph' ;

WEIGHTED_ARC_START: '-[' ;
WEIGHTED_UNDIRECTED_ARC_START: '<-[' ;
WEIGHTED_ARC_END: ']->' ;

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
