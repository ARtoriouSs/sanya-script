grammar SanyaScript;

// parser rules
sanyaScript: statement* EOF;

statement: defvar
         | deffun
         | funCall
         | assignment
         | printStat
         | returnStat;

assignment: defvar '=' value # assign
          | ID '=' value     # reassign;

cast: '(' type_ ')';

defvar: 'node' ID  # defnode
      | 'arc' ID   # defarc
      | 'graph' ID # defgraph;

deffun: type_ ID '(' funArg? ')' block
      | ID '(' funArg? ')' block;

block: 'go' statement* 'end';

funArg
 : type_ ID
 | type_ ID ',' funArg;

funCall: ID '(' paramValue? ')';

paramValue
 : value
 | value ',' paramValue;

returnStat: 'return' value;

value: (cast)? INT                        # nodeValue
     | (cast)? arcPart arc arcPart        # arcValue
     | (cast)? '[' (value ',')* value ']' # graphValue
     | (cast)? ID                         # idValue
     | (cast)? funCall                    # funCallValue;

arc: '->'            # simpleArc
   | '<->'           # simpleUndirectedArc
   | '-[' INT ']->'  # weightedArc
   | '<-[' INT ']->' # weightedUndirectedArc;

arcPart: INT | ID;

type_: 'node'
     | 'arc'
     | 'graph';

printStat: 'print' '(' value ')';

// lexer rules
INT: '-'?[1-9][0-9]* ;

ID: [a-z][a-zA-Z0-9]* ;
WS: [ \t\r\n]+ -> skip ;
COMMENT: '#' ~[\n]+  -> skip ;
