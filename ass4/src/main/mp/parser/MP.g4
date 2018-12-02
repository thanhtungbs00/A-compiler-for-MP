/* Cao Thanh Tung - 1613989 */
grammar MP;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}
program: (declaration)+ EOF;

declaration
    : varblock
    | funcblock
    | procblock
    ;
//--------------COMMENT------------------------
TRADITIONAL_CMT
	: '(*' .*? '*)' ->skip
    ;
BLOCK_CMT
    : '{' .*? '}' ->skip
    ;
LINE_CMT
    : '//' ~[\r\n]* ->skip
    ;
//--------------End comment-------------------
//--------------type-------------
ptypes: BOOLEANTYPE | INTTYPE | REALTYPE | STRINGTYPE ;
ctypes: ARRAY LSB index RSB OF ptypes;
index: lower DD lower ;
lower: SUBOP?INTLIT;
//------------Variable declaration-----------
varblock: VAR (var_dec SEMI)+ ;
var_dec 
	: listid COLON ptypes 
    | listid COLON ctypes
	;
listid: ID COMMA listid | ID ;
//------------End Variable-------------------

//------------Procedure----------------------
procblock
    : PROCEDURE ID LB listpara? RB SEMI varblock* compound_stt
    //| PROCEDURE MAIN LB  RB SEMI varblock* compound_stt
    ;
//------------End Procedure------------------
//------------Function-----------------------
funcblock
    : FUNCTION ID LB listpara? RB COLON return_type SEMI varblock* compound_stt 
    //| FUNCTION MAIN LB listpara? RB COLON return_type SEMI varblock* compound_stt 
    ;
//funcall: ID LB ((exp COMMA)* exp)? RB ;
funcall: ID LB list_exp? RB ;
list_exp: para_call COMMA list_exp | para_call ;
para_call: exp|STRINGLIT;
listpara: var_dec SEMI listpara | var_dec ; 	

return_type: ptypes | ctypes ;   				

compound_stt: BEGIN liststt? END ; // Not completed

liststt: statements liststt | statements;

funcall_stt: ID LB list_exp? RB SEMI ;

statements
    : assignment
    | ifstatement 
    | ifnostatement
    | whilestatement
    | forstatement
    | breakstatement
    | continuestatement
    | returnstatement 
    | compound_stt
    | withstatement 
    | funcall_stt
    ;
//------------End Function-------------------
//------------statements---------------------

breakstatement: BREAK SEMI ;

continuestatement: CONTINUE SEMI;

returnstatement: RETURN exp? SEMI;

assignment: idassign exp SEMI ;
idassign: (ID|indexexp) ASSIGN idassign | (ID|indexexp) ASSIGN ;
/* 
assignment: (idassign ASSIGN)+ exp SEMI ;
idassign: ID|indexexp ;
*/
ifstatement: IF exp THEN statements (ELSE statements)? ;
ifnostatement:  IF exp THEN statements (NO ELSE statements)? ;

whilestatement: WHILE exp DO statements;

forstatement: FOR identifier ASSIGN exp typefor exp DO statements;
typefor: TO | DOWNTO;
identifier: ID;// phải là integer chưa làm

withstatement: WITH list_var_dec DO statements;
list_var_dec: var_dec SEMI list_var_dec|var_dec SEMI ;
//------------end statement -----------------

orelse: OR ELSE;
andthen: AND THEN;
exp: exp (andthen|orelse) exp1 | exp1;
exp1: exp2 op1 exp2 | exp2 ;
op1: EQ| NEQ | LT | GT | LTE | GTE;
exp2: exp2 (ADDOP | SUBOP | OR) exp3 | exp3;
exp3: exp3 (DIV | DIVOP | MULOP | MOD | AND) exp4 | exp4;
exp4: (SUBOP|NOT) exp4 | unary;

unary
    : INTLIT 
    | REALLIT 
    | STRINGLIT 
    | TRUE | FALSE
    | ID
    | indexexp
    | funcall 
    | LB exp RB 
    ;

indexexp: literal LSB exp RSB;
literal: INTLIT | REALLIT | ID | funcall | LB exp RB  ;
/* 
exp: (SUBOP|NOT) exp | exp1;
exp1: exp1 (DIV | DIVOP | MULOP | MOD | AND) exp2 | exp2 ;
exp2: exp2 (ADDOP | SUBOP | OR) exp3 | exp3;
exp3: exp3 (EQ| NEQ | LT | GT | LTE | GTE) exp4 | exp4;
exp4: exp4 (AND THEN | OR ELSE) exp5 |unary;
exp5: exp | unary;


exp: (SUBOP|NOT) exp | expression;
expression: expression (DIV | DIVOP | MULOP | MOD | AND) evaluemul|evaluemul;
evaluemul: evaluemul (ADDOP | SUBOP | OR) evalueadd|evalueadd;
evalueadd:evalueadd (EQ| NEQ | LT | GT | LTE | GTE) compare|compare;
compare:compare (AND THEN | OR ELSE) exp2 |exp2;
exp2: exp2 lst_call_exp |unary;
lst_call_exp: LSB exp RSB lst_call_exp | LSB exp RSB ;
*/
//Keywords
NO: N O;

BEGIN: B E G I N ;

END: E N D;

PROCEDURE: P R O C E D U R E;

FUNCTION: F U N C T I O N;

IF: I F ;

THEN: T H E N;

ELSE: E L S E;

WHILE : W H I L E;

DO: D O;

FOR: F O R;

TO: T O;

DOWNTO : D O W N T O;

BREAK: B R E A K;

CONTINUE: C O N T I N U E;

RETURN: R E T U R N;

WITH: W I T H;

VAR: V A R;

BOOLEANTYPE: B O O L E A N;

INTTYPE: I N T E G E R ;

REALTYPE: R E A L;

STRINGTYPE: S T R I N G;

ARRAY: A R R A Y;

OF: O F;

NOT: N O T;

OR: O R;

AND: A N D;

DIV: D I V;

MOD: M O D;

TRUE : T R U E;

FALSE: F A L S E;

//Literal
INTLIT: DIGIT;

BOOLLIT: (TRUE) | (FALSE);  // ko sài bị lỗi

REALLIT     
    : DIGIT '.' [0-9]* EXPONENT?
    |'.' DIGIT EXPONENT?
    | DIGIT EXPONENT
    ;

fragment DIGIT: [0-9]+ ;

fragment EXPONENT: ('e'|'E') ('-')? [0-9]+; 
    
STRINGLIT
    : '"'(ESC | ~[\r\n"\\EOF])*'"' 
        {
            s=self.text[1:-1]
            self.text=s
        }
    ;

LSB: '[' ;

RSB: ']' ;

LB: '(' ;

RB: ')' ;

SEMI: ';' ;

COMMA: ',';

COLON: ':';

DD: '..';

WS: [ \t\r\n\f]+ -> skip ; // skip spaces, tabs, newlines

//Operator

ASSIGN: ':=';

ADDOP: '+';

MULOP: '*';

SUBOP: '-';

DIVOP: '/';

NEQ: '<>';

EQ: '=';

LT: '<';

GT: '>';

LTE: '<=';

GTE: '>=';

ID: [_a-zA-Z][_a-zA-Z0-9]* ;


fragment A
   : ('a' | 'A')
   ;


fragment B
   : ('b' | 'B')
   ;


fragment C
   : ('c' | 'C')
   ;


fragment D
   : ('d' | 'D')
   ;


fragment E
   : ('e' | 'E')
   ;


fragment F
   : ('f' | 'F')
   ;


fragment G
   : ('g' | 'G')
   ;


fragment H
   : ('h' | 'H')
   ;


fragment I
   : ('i' | 'I')
   ;


fragment J
   : ('j' | 'J')
   ;


fragment K
   : ('k' | 'K')
   ;


fragment L
   : ('l' | 'L')
   ;


fragment M
   : ('m' | 'M')
   ;


fragment N
   : ('n' | 'N')
   ;


fragment O
   : ('o' | 'O')
   ;


fragment P
   : ('p' | 'P')
   ;


fragment Q
   : ('q' | 'Q')
   ;


fragment R
   : ('r' | 'R')
   ;


fragment S
   : ('s' | 'S')
   ;


fragment T
   : ('t' | 'T')
   ;


fragment U
   : ('u' | 'U')
   ;


fragment V
   : ('v' | 'V')
   ;


fragment W
   : ('w' | 'W')
   ;


fragment X
   : ('x' | 'X')
   ;


fragment Y
   : ('y' | 'Y')
   ;


fragment Z
   : ('z' | 'Z')
   ;

fragment ESC: '\\' [btnfr'"\\];

fragment IESC: '\\' ~[btnfr'"\\];



ERROR_CHAR
    : .
        { 
            raise ErrorToken(self.text) 
        }
    ;

ILLEGAL_ESCAPE
    : '"' (ESC | ~["\\])*? ([\\] ~[bfrnt'"\\]) 
        {
           raise IllegalEscape(self.text[1:])
        }
    ;

UNCLOSE_STRING
    :  '"' (ESC | ~["\r\n] |((~'\\')'\\"'))* ('\n'| EOF)
        {
            if self.text[-1]=='\n':
                raise UncloseString(self.text[1:-1])
            else:
                raise UncloseString(self.text[1:])
        }
    ;