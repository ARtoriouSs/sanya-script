grammar SanyaScript;

// parser rules
sanyaScript: (defvar | assignment | print)* EOF;

assignment: (defvar | ID) EQUALS (cast)? (value | ID);

defvar: (defnode | defarc | defgraph);
defnode: NODE_TYPE ID;
defarc: ARC_TYPE ID;
defgraph: GRAPH_TYPE ID;

arc: (simpleArc | simpleUndirectedArc | weightedArc | weightedUndirectedArc);
simpleArc: '->';
simpleUndirectedArc: '<->';
weightedArc: WEIGHTED_ARC_START INT WEIGHTED_ARC_END;
weightedUndirectedArc: WEIGHTED_UNDIRECTED_ARC_START INT WEIGHTED_ARC_END;

value: (nodeValue | arcValue | graphValue);
nodeValue: INT;
arcValue: (nodeValue | ID) arc (nodeValue | ID);
graphValue: '[' ((value | ID) ',')* (value | ID) ']';

type: (NODE_TYPE | ARC_TYPE | GRAPH_TYPE);
cast: '(' type ')';

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
