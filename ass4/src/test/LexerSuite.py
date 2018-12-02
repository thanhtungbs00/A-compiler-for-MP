import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    def test_vardec1(self):
        self.assertTrue(TestLexer.test("var f: real;","var,f,:,real,;,<EOF>",100))
    def test_funcdec(self):
        self.assertTrue(TestLexer.test("function foo():integer;","function,foo,(,),:,integer,;,<EOF>",101))
    def test_vardec(self):
        self.assertTrue(TestLexer.test("var f: real;a: array [0 .. 5] of int;","var,f,:,real,;,a,:,array,[,0,..,5,],of,int,;,<EOF>",102))
    def test_key(self):
        self.assertTrue(TestLexer.test("inT","inT,<EOF>",103))
    def test_key1(self):
        self.assertTrue(TestLexer.test("real void","real,void,<EOF>",104))
    def test_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("_abc","_abc,<EOF>",105))
        self.assertTrue(TestLexer.test("_aCB5bdc","_aCB5bdc,<EOF>",106))
        self.assertTrue(TestLexer.test("abcd_1234","abcd_1234,<EOF>",107))
    def test_integer(self):
        """test integers"""
        self.assertTrue(TestLexer.test("12323","12323,<EOF>",108))
    def test_cmt1(self):
        self.assertTrue(TestLexer.test("(* sad *)","<EOF>",109))
    def test_cmt2(self):
        self.assertTrue(TestLexer.test("{ sad \n}","<EOF>",110))
    def test_cmt3(self):
        self.assertTrue(TestLexer.test("// sad \n ","<EOF>",111))
    def test_cmt4(self):
        self.assertTrue(TestLexer.test("{saasdsd} ad {ascsac} ","ad,<EOF>",112))
    def test_cmt5(self):
        self.assertTrue(TestLexer.test("{saasdsd{as} ad {{{ac}","ad,<EOF>",113))
    def test_cmt6(self):
        self.assertTrue(TestLexer.test("(*4zx(((****) 5x+4","5,x,+,4,<EOF>",114))
    def test_cmt7(self):
        self.assertTrue(TestLexer.test("(*a{a}bcsd","(,*,a,bcsd,<EOF>",115))
    def test_cmt8(self):
        self.assertTrue(TestLexer.test("5e10//3x+5","5e10,<EOF>",116))
    def test_cmt9(self):
        self.assertTrue(TestLexer.test("//{}(*//}*)))","<EOF>",117))
    def test_op(self):
        self.assertTrue(TestLexer.test("a=5","a,=,5,<EOF>",118))
    def test_op1(self):
        self.assertTrue(TestLexer.test("array a div not 5","array,a,div,not,5,<EOF>",119))
    def test_string(self):
        self.assertTrue(TestLexer.test("id=\"cao thanh tung\" ","id,=,cao thanh tung,<EOF>",120))
    def test_funct(self):
        self.assertTrue(TestLexer.test("funcTion foo(a,b:integer;c:real):array [1 .. 2] of integer;" ,"funcTion,foo,(,a,,,b,:,integer,;,c,:,real,),:,array,[,1,..,2,],of,integer,;,<EOF>",121))
    def test_procedure(self):
        self.assertTrue(TestLexer.test("Procedure foo(a,b:integer;c:real);" ,"Procedure,foo,(,a,,,b,:,integer,;,c,:,real,),;,<EOF>",122))
    def test_errortoken(self):
        self.assertTrue(TestLexer.test("\\","Error Token \\",123))
    def test_integer_value(self):
        self.assertTrue(TestLexer.test("a=-100","a,=,-,100,<EOF>",124))
    def test_integer_value2(self):
        self.assertTrue(TestLexer.test("a=--100 , b = not100","a,=,-,-,100,,,b,=,not100,<EOF>",125))
    def test_assign(self):
        self.assertTrue(TestLexer.test("a:=-100","a,:=,-,100,<EOF>",126))
    def test_assign_list(self):
        self.assertTrue(TestLexer.test("a:=b:=5:=-100","a,:=,b,:=,5,:=,-,100,<EOF>",127))
    def test_assign_list_index(self):
        self.assertTrue(TestLexer.test("a:=b[5]:=5:=-100","a,:=,b,[,5,],:=,5,:=,-,100,<EOF>",128))
    def test_assign_list_index_func(self):
        self.assertTrue(TestLexer.test("a:=b[5]:=foo(5):=-100","a,:=,b,[,5,],:=,foo,(,5,),:=,-,100,<EOF>",129))
    def test_funcall(self):
        self.assertTrue(TestLexer.test("foo(2)[3+x] := a[b[2]] +3;","foo,(,2,),[,3,+,x,],:=,a,[,b,[,2,],],+,3,;,<EOF>",130))
    def test_string_assign(self):
        self.assertTrue(TestLexer.test("a:=\"hien\"","a,:=,hien,<EOF>",131))
    def test_array_exp(self):
        self.assertTrue(TestLexer.test("var i : array [ 1-1 .. 1+1 ] of integer; ","var,i,:,array,[,1,-,1,..,1,+,1,],of,integer,;,<EOF>",132))
    def test_identifiers(self):    
        self.assertTrue(TestLexer.test("_ 4","_,4,<EOF>",133))
    def test_num_identifiers(self):    
        self.assertTrue(TestLexer.test("123_321","123,_321,<EOF>",134))
    def test_unclosed_str(self):
        self.assertTrue(TestLexer.test(""" "String \n here " ""","Unclosed String: String ",135))
    def test_unclosed_str1(self):
        self.assertTrue(TestLexer.test(""" Not string"  ""","Not,string,Unclosed String:   ",136))
    def test_cmt_in_string(self):
        self.assertTrue(TestLexer.test(""" "{(*// This is string too} " ""","{(*// This is string too} ,<EOF>",137))
    def test_unclosed_str2(self):
        self.assertTrue(TestLexer.test(""" "Not string""","Unclosed String: Not string",138))
    def test_int(self):
        self.assertTrue(TestLexer.test("+111","+,111,<EOF>",139))
    def test_int_neg(self):
        self.assertTrue(TestLexer.test("-111","-,111,<EOF>",140))
    def test_int_zero_0(self):
        self.assertTrue(TestLexer.test("000","000,<EOF>",141))
    def test_int_zero_1(self):
        self.assertTrue(TestLexer.test("01","01,<EOF>",142))
    def test_type_real(self):
        self.assertTrue(TestLexer.test("1.5","1.5,<EOF>",143))
    def test_type_real1(self):   
        self.assertTrue(TestLexer.test(".4e258",".4e258,<EOF>",144))
    def test_not_real_id(self):    
        self.assertTrue(TestLexer.test("555EEE","555,EEE,<EOF>",145))
    def test_real_not_dig_before_e(self):
        self.assertTrue(TestLexer.test("e32","e32,<EOF>",146))
    def test_errortoken_real(self):
        self.assertTrue(TestLexer.test(".e","Error Token .",147))
    def test_not_dig_after_e(self):
        self.assertTrue(TestLexer.test("143e","143,e,<EOF>",148))
    def test_not_dig_befor_e(self):
        self.assertTrue(TestLexer.test("e154","e154,<EOF>",149))
    def test_real_negs(self):
        self.assertTrue(TestLexer.test("-----4E5","-,-,-,-,-,4E5,<EOF>",150))
    def test_real_error(self):    
        self.assertTrue(TestLexer.test("1.2.3.4","1.2,.3,.4,<EOF>",151))
    def test_boolean(self):
        self.assertTrue(TestLexer.test("faLse AND TRUE","faLse,AND,TRUE,<EOF>",154))
    def test_bool_neg(self):
        self.assertTrue(TestLexer.test("-false+true","-,false,+,true,<EOF>",152))
    def test_bool_dd(self):
        self.assertTrue(TestLexer.test("False.. FaLSE","False,..,FaLSE,<EOF>",153))
    def test_bool_int(self):
        self.assertTrue(TestLexer.test("5False 43aFalse","5,False,43,aFalse,<EOF>",154))
    def test_keywords_if(self):
        self.assertTrue(TestLexer.test("iF if3 2IF 8e0IF","iF,if3,2,IF,8e0,IF,<EOF>",155))
    def test_keywords_then(self):
        self.assertTrue(TestLexer.test("thEN theN","thEN,theN,<EOF>",156))
    def test_keywords_else(self):
        self.assertTrue(TestLexer.test("8ELSE ELSELSE","8,ELSE,ELSELSE,<EOF>",157))
    def test_keywords_while(self):
        self.assertTrue(TestLexer.test("whILE .33e32while","whILE,.33e32,while,<EOF>",158))
    def test_keywords_begin(self):
        self.assertTrue(TestLexer.test("begin beGIN be3gin \n \n","begin,beGIN,be3gin,<EOF>",159))
    def test_keywords_end(self):
        self.assertTrue(TestLexer.test("end END 10e-2end","end,END,10e-2,end,<EOF>",160))
    def test_keywords_for(self):
        self.assertTrue(TestLexer.test("for 5for","for,5,for,<EOF>",161))
    def test_keywords_to(self):
        self.assertTrue(TestLexer.test("To _TO","To,_TO,<EOF>",162))
    def test_keywords_downto(self):
        self.assertTrue(TestLexer.test("downto down _downto","downto,down,_downto,<EOF>",163))
    def test_keywords_do(self):
        self.assertTrue(TestLexer.test("do _do_ acdDO","do,_do_,acdDO,<EOF>",164))
    def test_keywords_break(self):
        self.assertTrue(TestLexer.test("break BREak 43break break3 _break .e10break","break,BREak,43,break,break3,_break,Error Token .",165))
    def test_keywords_continue(self):
        self.assertTrue(TestLexer.test("3continue _continue ","3,continue,_continue,<EOF>",166))
    def test_keywords_return(self):
        self.assertTrue(TestLexer.test("REturn 10e11return return10e11","REturn,10e11,return,return10e11,<EOF>",167))
    def test_keywords_with(self):
        self.assertTrue(TestLexer.test("with WiTH 4wiTH with3 asWITH 3.4e10WITH","with,WiTH,4,wiTH,with3,asWITH,3.4e10,WITH,<EOF>",168))
    def test_keywords_function(self):
        self.assertTrue(TestLexer.test("function FUNCTION {fucntion 232} 5function","function,FUNCTION,5,function,<EOF>",169))
    def test_keywords_procedure(self):   
        self.assertTrue(TestLexer.test("procedure ProceDure (*procedure*) //43e-32procedure","procedure,ProceDure,<EOF>",170))
    def test_keywords_var(self):
        self.assertTrue(TestLexer.test("var //////////var \n VAr {var 3e10Var}","var,VAr,<EOF>",171))
    def test_keywords_true(self):
        self.assertTrue(TestLexer.test("true TRUE 3true -.5e-43trUE _true","true,TRUE,3,true,-,.5e-43,trUE,_true,<EOF>",172))
    def test_keywords_false(self):
        self.assertTrue(TestLexer.test("false FALSE 4false +-*/False //false","false,FALSE,4,false,+,-,*,/,False,<EOF>",173))
    def test_keywords_array(self):
        self.assertTrue(TestLexer.test("array i:array[1 .. 10] of boolean;","array,i,:,array,[,1,..,10,],of,boolean,;,<EOF>",174))
    def test_keywords_of(self):
        self.assertTrue(TestLexer.test("of OF 0F o f","of,OF,0,F,o,f,<EOF>",175))
    def test_keywords_int(self):
        self.assertTrue(TestLexer.test("integer var i:;j:inteGEr","integer,var,i,:,;,j,:,inteGEr,<EOF>",176))
    def test_keywords_string(self):
        self.assertTrue(TestLexer.test("strING5 5strINg","strING5,5,strINg,<EOF>",177))
    def test_keywords_not(self):
        self.assertTrue(TestLexer.test("NOT(A nOt B)","NOT,(,A,nOt,B,),<EOF>",178))
    def test_keywords_and(self):
        self.assertTrue(TestLexer.test("and A anD aND (not C)","and,A,anD,aND,(,not,C,),<EOF>",179))
    def test_keywords_or(self):
        self.assertTrue(TestLexer.test("or oR","or,oR,<EOF>",180))
    def test_keywords_real(self):
        self.assertTrue(TestLexer.test("\r \n REAL \b 34real","REAL,Error Token \b",181))
    def test_keywords_bool(self):
        self.assertTrue(TestLexer.test("BOOLean //Boolean \n bOOlean","BOOLean,bOOlean,<EOF>",182))
    def test_keywords_div(self):
        self.assertTrue(TestLexer.test("div 7dIV DIv","div,7,dIV,DIv,<EOF>",183))
    def test_keywords_mod(self):
        self.assertTrue(TestLexer.test("10 mOD div","10,mOD,div,<EOF>",184))
    def test_operators(self):
        self.assertTrue(TestLexer.test("a+-b-*a","a,+,-,b,-,*,a,<EOF>",185))
    def test_operators_1(self):
        self.assertTrue(TestLexer.test("a:=b >= 2 \n<=","a,:=,b,>=,2,<=,<EOF>",186))
    def test_operators_2(self):
        self.assertTrue(TestLexer.test("a>b<c=d+e+f","a,>,b,<,c,=,d,+,e,+,f,<EOF>",187))
    def test_operators_3(self):
        self.assertTrue(TestLexer.test("a<>b :=c {asc <5}","a,<>,b,:=,c,<EOF>",188))
    def test_operators_fina(self):
        self.assertTrue(TestLexer.test("5*13:=a+5/2>=4","5,*,13,:=,a,+,5,/,2,>=,4,<EOF>",189))
    def test_token_set_0(self):
        self.assertTrue(TestLexer.test("\t\n\r","<EOF>",190))
    def test_token_set_1(self):
        self.assertTrue(TestLexer.test("\r\t.2222e10\t",".2222e10,<EOF>",191))
    def test_token_set_2(self):
        self.assertTrue(TestLexer.test("\n\n\n\t\t\r\r","<EOF>",192))
    def test_token_set_3(self):
        self.assertTrue(TestLexer.test("bc\t\tcXd","bc,cXd,<EOF>",193))
    def test_token_set_4(self):
        self.assertTrue(TestLexer.test("\ttungking\t","tungking,<EOF>",194))
    def test_seq_real(self):
        self.assertTrue(TestLexer.test("1.01e01","1.01e01,<EOF>",195))
    def test_sep_cmt_0(self):
        self.assertTrue(TestLexer.test("(*(()))[5894555[*)]]","],],<EOF>",196))
    def test_int_sign(self):
        self.assertTrue(TestLexer.test("+111","+,111,<EOF>",197))
    def test_char_error_token(self):
        self.assertTrue(TestLexer.test("c#@@$@#$##$$$ 10$ $100","c,Error Token #",198))
    def test_num_error(self):
        self.assertTrue(TestLexer.test("10@4001###","10,Error Token @",199))
    def test_neg_int(self):
        self.assertTrue(TestLexer.test("123----321","123,-,-,-,-,321,<EOF>",200))