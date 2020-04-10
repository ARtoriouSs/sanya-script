grammar SanyaScript;

//
// parser rules
//

sanyaScript: statement* EOF;

// definitions
statement: defvar
         | deffun
         | funCall
         | assignment
         | printStat
         | println
         | pushToArray
         | returnStat
         | forCycle
         | whileCycle
         | ifStat;

assignment: defvar '=' value # assign
          | ID '=' value     # reassign;

defvar: type_ ID;

// functions
deffun: type_ ID '(' funArg? ')' block
      | ID '(' funArg? ')' block;

funArg: type_ ID
      | type_ ID ',' funArg;

block: 'go' statement* 'end';

funCall: ID '(' paramValue? ')';

paramValue: value
          | value ',' paramValue;

returnStat: 'return' value;

// ifs
ifStat: 'if' value ifBlock;

ifBlock: 'go' then=ifBlockPart 'else' else_=ifBlockPart 'end' # ifThenElseBlock
       | 'go' then=ifBlockPart 'end'                          # ifThenBlock;

ifBlockPart: statement*;

// cycles
forCycle: 'for' defvar 'in' value block;
whileCycle: 'while' value block;

// values
value: cast? '(' value ')'                                                      # parenthesizedValue
     | 'not' value                                                              # notValue
     | left=value operation='and' right=value                                   # andValue
     | left=value operation='or' right=value                                    # orValue
     | left=value operation=('==' | '!=' | '>=' | '<=' | '>' | '<') right=value # comparisonValue
     | left=value operation=('/' | '*') right=value                             # divMultValue
     | left=value operation=('+' | '-') right=value                             # sumSubtrValue
     | cast? '^' NUM                                                            # nodeValue
     | cast? '<' source=value arc target=value '>'                              # arcValue
     | cast? '[' (value ',')* value ']'                                         # graphValue
     | cast? NUM                                                                # numValue
     | cast? ID ('[' value ']')?                                                # idValue
     | cast? funCall                                                            # funCallValue
     | cast? (yes='yes' | no='no')                                              # logicValue
     | 'nope'                                                                   # nopeValue;

cast: '(' type_ ')';

type_: 'node'
     | 'arc'
     | 'graph'
     | 'num'
     | 'logic'
     | 'node{}'
     | 'arc{}'
     | 'graph{}'
     | 'num{}'
     | 'logic{}';

arc: '->'            # simpleArc
   | '<->'           # simpleUndirectedArc
   | '-[' NUM ']->'  # weightedArc
   | '<-[' NUM ']->' # weightedUndirectedArc;

// builtins
printStat: 'print' '(' value ')';
println: 'println' '(' value ')';
pushToArray: ID '<<' value;

//
// lexer rules
//

NUM: '-'?([1-9][0-9]*|'0')(.[0-9]+)? ;

ID: [a-z][a-zA-Z0-9]* ;
WS: [ \t\r\n]+ -> skip ;
COMMENT: '#' ~[\n]+  -> skip ;
