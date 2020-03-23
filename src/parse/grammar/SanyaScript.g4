grammar SanyaScript;

// parser rules
sanyaScript: statement* EOF;

statement: defvar
         | deffun
         | funCall
         | assignment
         | print;

assignment: defvar '=' value # assign
          | ID '=' value     # reassign;

cast: '(' type ')';

defvar: NODE_TYPE ID  # defnode
      | ARC_TYPE ID   # defarc
      | GRAPH_TYPE ID # defgraph;

deffun: type ID '(' funArg? ')' '{' statement* 'return' value '}' # typeFun
      | ID '(' funArg? ')' '{' statement* 'return' value '}'      # nullFun;

funArg
 : type ID            # paramArg
 | type ID ',' funArg # paramArgs;

funCall: ID '(' funValue? ')';

funValue
 : value              # paramValue
 | value ',' funValue # paramValues;

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
