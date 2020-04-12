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
         | pushToArray
         | returnStat
         | forCycle
         | whileCycle
         | ifStat;

assignment: defvar '=' value # assign
          | ID '=' value     # reassign;

defvar: CONST? type_ ID;

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
whileCycle: 'while' value block;
forCycle: 'for' defvar 'in' value block # forInCycle
        | 'for' defvar 'to' value block # forToCycle;

// values
value: cast value                                                               # castValue
     | '(' value ')'                                                            # parenthesizedValue
     | target=value '[' index=value ']'                                                # indexValue
     | 'not' value                                                              # notValue
     | left=value operation='and' right=value                                   # andValue
     | left=value operation='or' right=value                                    # orValue
     | left=value operation=('==' | '!=' | '>=' | '<=' | '>' | '<') right=value # comparisonValue
     | left=value operation=('/' | '*') right=value                             # divMultValue
     | left=value operation=('+' | '-') right=value                             # sumSubtrValue
     | '^' NUM                                                                  # nodeValue // ref
     | '<' source=value arc target=value '>'                                    # arcValue
     | '[' (value ',')* value ']'                                               # graphValue // ref
     | NUM                                                                      # numValue
     | ID                                                                       # idValue
     | funCall                                                                  # funCallValue
     | (yes='yes' | no='no')                                                    # logicValue
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
   | '-[' NUM ']->'  # weightedArc // ref
   | '<-[' NUM ']->' # weightedUndirectedArc;

// builtins
pushToArray: ID '<<' value;

//
// lexer rules
//

CONST: 'const' ;

NUM: '-'?([1-9][0-9]*|'0')(.[0-9]+)? ;

ID: [a-zA-Z_][a-zA-Z0-9_]* ;
WS: [ \t\r\n]+ -> skip ;
COMMENT: '#' ~[\n]+  -> skip ;
