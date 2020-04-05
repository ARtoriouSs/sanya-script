grammar SanyaScript;

// parser rules
sanyaScript: statement* EOF;

statement: defvar
         | deffun
         | funCall
         | assignment
         | printStat
         | println
         | returnStat
         | ifStat;

assignment: defvar '=' value # assign
          | ID '=' value     # reassign;

cast: '(' type_ ')';

defvar: 'node' ID  # defnode
      | 'arc' ID   # defarc
      | 'graph' ID # defgraph
      | 'num' ID   # defnum
      | 'logic' ID # deflogic;

deffun: type_ ID '(' funArg? ')' block
      | ID '(' funArg? ')' block;

block: 'go' statement* 'end';

ifBlock: 'go' then=ifBlockPart 'else' else_=ifBlockPart 'end' # ifThenElseBlock
       | 'go' then=ifBlockPart 'end'                          # ifThenBlock;

ifBlockPart: statement*;

funArg: type_ ID
      | type_ ID ',' funArg;

funCall: ID '(' paramValue? ')';

paramValue: value
          | value ',' paramValue;

returnStat: 'return' value;

ifStat: 'if' value ifBlock;

value: cast? '(' value ')'                                                      # parenthesizedValue
     | 'not' value                                                              # notValue
     | left=value 'and' right=value                                             # andValue
     | left=value 'or' right=value                                              # orValue
     | left=value operation=('==' | '!=' | '>=' | '<=' | '>' | '<') right=value # comparisonValue
     | left=value operation=('/' | '*') right=value                             # divMultValue
     | left=value operation=('+' | '-') right=value                             # sumSubtrValue
     | cast? '^' NUM                                                            # nodeValue
     | cast? '<' source=value arc target=value '>'                              # arcValue
     | cast? '[' (value ',')* value ']'                                         # graphValue
     | cast? NUM                                                                # numValue
     | cast? ID                                                                 # idValue
     | cast? funCall                                                            # funCallValue
     | cast? (yes='yes' | no='no')                                              # logicValue
     | 'nope'                                                                   # nopeValue;

arc: '->'               # simpleArc
   | '<->'              # simpleUndirectedArc
   | '-[' NUM ']->'     # weightedArc
   | '<-[' NUM ']->'    # weightedUndirectedArc;

type_: 'node'
     | 'arc'
     | 'graph'
     | 'num'
     | 'logic';

printStat: 'print' '(' value ')';
println: 'println' '(' value ')';

// lexer rules
NUM: '-'?([1-9][0-9]*|'0')(.[0-9]+)? ;

ID: [a-z][a-zA-Z0-9]* ;
WS: [ \t\r\n]+ -> skip ;
COMMENT: '#' ~[\n]+  -> skip ;
