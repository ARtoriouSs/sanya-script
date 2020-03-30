grammar SanyaScript;

// parser rules
sanyaScript: statement* EOF;

statement: defvar
         | deffun
         | funCall
         | assignment
         | printStat
         | println
         | returnStat;

assignment: defvar '=' value # assign
          | ID '=' value     # reassign;

cast: '(' type_ ')';

defvar: 'node' ID  # defnode
      | 'arc' ID   # defarc
      | 'graph' ID # defgraph
      | 'num' ID   # defnum;

deffun: type_ ID '(' funArg? ')' block
      | ID '(' funArg? ')' block;

block: 'go' statement* 'end';

funArg: type_ ID
      | type_ ID ',' funArg;

funCall: ID '(' paramValue? ')';

paramValue: value
          | value ',' paramValue;

returnStat: 'return' value;

value: cast? '(' value ')'                          # parenthesizedValue
     | left=value operation=('/' | '*') right=value # divMultValue
     | left=value operation=('+' | '-') right=value # sumSubtrValue
     | cast? '^' NUM                                # nodeValue
     | cast? '<' target=value arc source=value '>'  # arcValue
     | cast? '[' (value ',')* value ']'             # graphValue
     | cast? NUM                                    # numValue
     | cast? ID                                     # idValue
     | cast? funCall                                # funCallValue;

arc: '->'               # simpleArc
   | '<->'              # simpleUndirectedArc
   | '-[' NUM ']->'     # weightedArc
   | '<-[' NUM ']->'    # weightedUndirectedArc;

type_: 'node'
     | 'arc'
     | 'graph'
     | 'int'
     | 'float';

printStat: 'print' '(' value ')';
println: 'println' '(' value ')';

// lexer rules
NUM: '-'?([1-9][0-9]*|'0')(.[0-9]+)? ;

ID: [a-z][a-zA-Z0-9]* ;
WS: [ \t\r\n]+ -> skip ;
COMMENT: '#' ~[\n]+  -> skip ;
