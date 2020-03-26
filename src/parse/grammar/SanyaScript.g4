grammar SanyaScript;

// parser rules
sanyaScript: statement* EOF;

statement: defvar
         | deffun
         | funCall
         | assignment
         | print
         | returnStat;

assignment: defvar '=' value # assign
          | ID '=' value     # reassign;

cast: '(' type ')';

defvar: NODE_TYPE ID  # defnode
      | ARC_TYPE ID   # defarc
      | GRAPH_TYPE ID # defgraph;

deffun: type ID '(' funArg? ')' '{' funBody '}'
      | ID '(' funArg? ')' '{' funBody '}';

funBody: statement*;

funArg
 : type ID
 | type ID ',' funArg;

funCall: ID '(' paramValue? ')';

paramValue
 : value
 | value ',' paramValue;

returnStat: 'return' value;

value: (cast)? INT                        # nodeValue
     | (cast)? arcPart arc arcPart        # arcValue
     | (cast)? '[' (value ',')* value ']' # graphValue
     | (cast)? ID                         # idValue;

arc: '->'            # simpleArc
   | '<->'           # simpleUndirectedArc
   | '-[' INT ']->'  # weightedArc
   | '<-[' INT ']->' # weightedUndirectedArc;

arcPart: INT | ID;

type: NODE_TYPE
    | ARC_TYPE
    | GRAPH_TYPE;

print: 'print' ID;

// lexer rules
NODE_TYPE: 'node' ;
ARC_TYPE: 'arc' ;
GRAPH_TYPE: 'graph' ;

INT: [1-9][0-9]* ;

ID: [a-z][a-zA-Z0-9]* ;
WS: [ \t\r\n]+ -> skip ;
COMMENT: '#' ~[\n]+  -> skip ;
