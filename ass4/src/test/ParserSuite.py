import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_main(self):
        input = """procedure main(); begin end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))
    def test_main_error(self):
        input = """procedure main(; begin end"""
        expect = "Error on line 1 col 15: ;"
        self.assertTrue(TestParser.test(input,expect,202))
    def test_declare_simple(self):
        input = """procedure main(); \n var a ,b: real; \n begin \n  \n end\n"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,203))
    def test_procedure1(self):
        input = """procedure main();begin end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,204))
    def test_var_declaration(self):
        input = """var i : integer ;\n function f (): integer ; \n begin \n return 200; \n end \n procedure main();begin end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,205))
    def test_var_array(self):
        input = """var a : arraY [5 .. 6] of integer;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,206))
    def test_var(self):
        input = """var a,b,c : real;
        d :array [2 .. 6] of integer;
        function main(): integer;
        begin
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,207))
    def test_assignment_simple(self):
        input = """var a : real;\nfunction main():integer;\nbegin\na := b;\nend\n"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,208))
    def test_assignment_indexexp(self):
        input = """var a : real;\nfunction main():integer;\nbegin\na := b[5]:=;\nend\n"""
        expect = "Error on line 4 col 11: ;"
        self.assertTrue(TestParser.test(input,expect,209)) 
    def test_assignment_indexexp_sample(self):
        input = """procedure main();\nbegin\na := b[10] := foo()[3] := x :=  ;\nend"""
        expect = "Error on line 3 col 32: ;"
        self.assertTrue(TestParser.test(input,expect,210)) 
    def test_var_dec(self):
        input = """var i : array [1 .. 2,3 .. 4] of integer ;"""
        expect = "Error on line 1 col 21: ,"
        self.assertTrue(TestParser.test(input,expect,211)) 
    def test_var_dec_array(self):
        input = """var i : array [3 .. 4] of integer ;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,212)) 
    def test_index_exp(self):
        input = """var i:integer ;\nprocedure main();\nbegin\nfoo(2)[3+x] := a[b[2]] +3;\nend"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,213)) 
    def test_assignment_array(self):
        input = """procedure main();\nbegin\na[b[2]] :=1  ;\nend"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,214)) 
    def test_assignment_funccall(self):
        input = """procedure main();\nbegin\nfoo(2)[3+x] :=1  ;\nend"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,215)) 
    def test_procedure(self):
        input = """procedure foo ( a : array [ 1 .. 2 ] of  real);begin end
        procedure goo ( x : array [ 1 .. 2 ] of  real);
        var
        y : array [2 .. 3] of  real;
        z : array [1 .. 2] of  integer;
        begin
        foo(x);
        foo1(y)
        foo2(z) ; 
        end"""
        expect = "Error on line 9 col 8: foo2"
        self.assertTrue(TestParser.test(input,expect,216)) 
    def test_function(self):
        input = """function foo (b : array [ 1 .. 2 ] of integer ) : array [2 .. 3] of real ;\nbegin\nend"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,217)) 
    def test_string_assign(self):
        input = """function foo (b : array [ 1 .. 2 ] of integer ) : real ;\nbegin\n a := "abc"; \nend"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,218))
    def test_with_do(self):
        input = """function foo (b :integer ):real ;\nbegin\n with a , b : integer; c : array [1 .. 2] of real ; do d := c [a] + b; \nend"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,219))
    def test_assign_error(self):
        input = """function foo (b :integer ):real ;\nbegin\nx :=:= 2; \nend"""
        expect = "Error on line 3 col 4: :="
        self.assertTrue(TestParser.test(input,expect,220))
    def test_listvar_dec(self):
        input = """var a,b,c : integer ;\nd : array [1 .. 5] of integer ;\ne,f : real ;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,221))
    def test_array_index(self):
        input = """ var i : array [-1 .. 1] of integer; """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,222))
    def test_full_pro(self):
        input = """ procedure foo(a:integer; b:real);
        var a: real;
        begin
        for i := 1 to 10 do 
        a := a +1;
        break;
        end """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,223))
    def test_callfunc(self):
        input = """function foo (b :integer ):real ;\nbegin\nfoo (3, a+1, m(2)); \nend\n"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,224))
    def test_var_dec_listid(self):
        input = """var i:integer;
		j,:real;
	    procedure main();
	    begin
	    end"""
        expect = "Error on line 2 col 4: :"
        self.assertTrue(TestParser.test(input,expect,225))
    def test_var_dec_array_type(self):
        input = """var i:array [-3 .. -2] of integer;
		j,x:array [-1 .. -2] of;
		procedure main();
		begin
		end"""
        expect = "Error on line 2 col 25: ;"
        self.assertTrue(TestParser.test(input,expect,226))
    def test_structure_procedure_end(self):
        input = """procedure main();
		begin
		end
		procedure foo();
		begin
        """
        expect = "Error on line 6 col 8: <EOF>"
        self.assertTrue(TestParser.test(input,expect,227))
    def test_func_dec_return_type(self):
        input = """function main(a,b:real):integer;
		begin
		end
		function foo():;
		begin
		end"""
        expect = "Error on line 4 col 17: ;"
        self.assertTrue(TestParser.test(input,expect,228))
    def test_noindentify_type(self):
        input = """var a:integer;
		procedure main(); 
			a,d:integer;
				b,c real;
			begin 
			end"""
        expect = "Error on line 3 col 3: a"
        self.assertTrue(TestParser.test(input,expect,229))
    def test_with_do_statement(self):
        input = """procedure main(); 
	    begin
		with a,c:REAl;b,d,y:INTeger;m:BOOLean; do with a:integer; do a := 1; 
		with a:integer; do with b:integer do a := 1;
	    end"""
        expect = "Error on line 4 col 36: do"
        self.assertTrue(TestParser.test(input,expect,230))
    def test_error_assign(self):
        input = """procedure main(); 
	    begin
        a := b[2]  := foo();
        a := b := c : 1;
        end"""
        expect = "Error on line 4 col 20: :"
        self.assertTrue(TestParser.test(input,expect,231))
    def test_end_compound_statement(self):
        input = """procedure main(); 
        begin
        with a:integer; do begin a:= 1; while a > 1 do while a < 1 do a := 1; end
        while a >= 1 do 
        end"""
        expect = "Error on line 5 col 8: end"
        self.assertTrue(TestParser.test(input,expect,232))
    def test_to_for_statement(self):
        input = """procedure main(); 
        begin
        for a := 1 to 3 do with a:integer; do for a := 1 downto 1 do a := a + 1;
        for a := 1 to 10 do for b := to 10 do a:= 1;
        end"""
        expect = "Error on line 4 col 37: to"
        self.assertTrue(TestParser.test(input,expect,233))
    def test_error_SEMI(self):
        input = """procedure main(); 
        begin
        foo(5,foo(),a[3+a]);
        foo(5,a;b);
        end"""
        expect = "Error on line 4 col 15: ;"
        self.assertTrue(TestParser.test(input,expect,234))
    def test_array_assign(self):
        input = """procedure main(); 
        begin
        foo(5,foo(),a[3+a]);
        1[3]:= "this is string" + 100;
        end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,235))
    def test_nest_func_pro(self):
        input = """function main():integer;
        procedure a(a:real); 
        begin
        foo(5,foo(),a[3+a]);
        a[3]:= "this is string" + 100;
        end
        begin
        end"""
        expect = "Error on line 2 col 8: procedure"
        self.assertTrue(TestParser.test(input,expect,236))
    def test_return_func(self):
        input = """function main():integer;
        begin
        a[3]:= "this is string" + 100;
        return 2*3;
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,237))
    def test_do_while(self):
        input = """function main():integer;
        begin
        while 1 do
        begin 
        a:=a+1;
        end
        return 2*3;
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,238))
    def test_for_statement(self):
        input = """function main():integer;
        begin
        for a:= a*2 to a=false do return;
        return 2*3;
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,239))
    def test_for_statement_expression(self):
        input = """function main():integer;
        begin
        for a:= a*2 to ((a=1) AND (x=5)) do i:=a[x]:=false*true;
        return 2*3;
        end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,240))
    def test_fill_program(self):
        input = """ var i: integer;
                        j:real;
                        g:array[1 .. 100] of string;
                    function tong(a,b:integer):integer;
                        begin
                            return a+b;
                        end
                    procedURE MaIn();
                    begin
                        j:= tong(i,i);
                        for i:=10 to 100 do g[i] := tong(i,i);
                    end
                    """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,241))
    def test_var_miss_semi(self):
        input = """ var i:integer
                        j:real;
                        g:boolean;
                    """
        expect ="Error on line 2 col 24: j"
        self.assertTrue(TestParser.test(input,expect,242))
    def test_variable_arr(self):
        input = """var a,b,c,gh : array [1 .. 23] of integer;
		d,e: array [1 .. 10] of real;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,243))
    def test_miss_kw_fucntion(self):
        input = """ food(a:integer;b:real):integer;
                    begin
                    end"""
        expect ="Error on line 1 col 1: food"
        self.assertTrue(TestParser.test(input,expect,244))
    def test_miss_proc_name(self):
        input = """ procedure ();
                    begin
                    end
                    """
        expect ="Error on line 1 col 11: ("
        self.assertTrue(TestParser.test(input,expect,245))
    def test_miss_begin(self):
        input = """ var i:integer;
                    
                        i:=i+1;
                    end
                    """
        expect ="Error on line 3 col 25: :="
        self.assertTrue(TestParser.test(input,expect,246))
    def test_func_lost_body(self):
        input = """fucntion func1():integer;
                    fucntion func2():real;
                    begin
                    end"""
        expect="Error on line 1 col 0: fucntion"
        self.assertTrue(TestParser.test(input,expect,247))
    def test_func_in_func(self):
        input = """function func1():integer;
                    begin
                        function func2():real;
                    end"""
        expect ="Error on line 3 col 24: function"
        self.assertTrue(TestParser.test(input,expect,248))
    def test_var_real(self):
        input = """ var i: real;  """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,249))
    def test_var_int(self):
        input = """ var i: integer;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,250))
    def test_vardec(self):
        input = """ var i: integer; """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,251))
    def test_func_nest_func(self):
        input = """function func1():integer;
                    begin
                        function func2():real;
                    end"""
        expect ="Error on line 3 col 24: function"
        self.assertTrue(TestParser.test(input,expect,252))
    def test_proc_nest_proc(self):
        input = """procedure func1();
                    begin
                        procedure func2();
                    end"""
        expect ="Error on line 3 col 24: procedure"
        self.assertTrue(TestParser.test(input,expect,253))
    def test_func_lost_compound(self):
        input = """function func1():integer;
                    function func2():real;
                    """
        expect="Error on line 2 col 20: function"
        self.assertTrue(TestParser.test(input,expect,254))
    def test_proc_lost_compound(self):
        input = """procedure func1();
                    procedure func2();
                    begin
                    end"""
        expect="Error on line 2 col 20: procedure"
        self.assertTrue(TestParser.test(input,expect,255))
    def test_lost_key_fucntion(self):
        input = """ foo(a:integer):integer;
                    begin
                    end"""
        expect ="Error on line 1 col 1: foo"
        self.assertTrue(TestParser.test(input,expect,256))
    def test_lost_key_procedure(self):
        input = """ foo(a:integer):integer;
                    begin
                    end"""
        expect ="Error on line 1 col 1: foo"
        self.assertTrue(TestParser.test(input,expect,257))
    def test_lost_end(self):
        input = """function foo(a:integer):integer;
                    begin
                        i:=i+1;
                    """
        expect ="Error on line 4 col 20: <EOF>"
        self.assertTrue(TestParser.test(input,expect,258))
    def test_lost_begin(self):
        input = """function foo(a:integer):integer;
                        i:=i+1;
                    end
                    """
        expect ="Error on line 2 col 24: i"
        self.assertTrue(TestParser.test(input,expect,259))
    def test_var_dec_real(self):
        input = """ var i,h,k,j: real; """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,260))
    def test_var_bool(self):
        input = """var i : boolean; """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,261))
    def test_var_str(self):
        input = """ var i: string; """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,262))
    def test_var_arr(self):
        input = """ var i,j,k: array [1 .. 5] of real; """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,263))
    def test_assistmt(self):
        input = """procedure main(); begin for i :=5 to 10 do a:=foo()[5]:=b:=c:=d:=a+i; end """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,264))
    def test_return_proc(self):
        input = """ procedure rt();
                    begin
                        return;
                    end
                """
        expect = "successful";
        self.assertTrue(TestParser.test(input,expect,265))
    
    def test_return_fucn(self):
        input = """
                    function rt():integer;
                    begin
                        return 5+6+5+4*100;
                    end
                    """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,266))
    def test_func_proc_program(self):
        input = """ var i: integer;
                        g:array[1 .. 100] of string;
                    function tong(a,b:integer):integer;
                        begin
                            return a+b;
                        end
                    procedURE MaIn();
                    begin
                        j:= tong(i,i);
                        for i:=10 to 100 do g[i] := tong(i,i);
                    end
                    """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,267))
    def test_error_array_dec(self):
        input = """ var i: array[1 .. 1, 1 .. 2] of integer;"""
        expect ="Error on line 1 col 20: ," 
        self.assertTrue(TestParser.test(input,expect,268))
    def test_vardec_lost_colon(self):
        input = """var a real;"""
        expect = "Error on line 1 col 6: real"
        self.assertTrue(TestParser.test(input,expect,269))
    def test_program(self):
        input ="""program main(a:integer):integer;
                    begin
                    end"""
        expect = "Error on line 1 col 0: program"
        self.assertTrue(TestParser.test(input, expect,270))
    def test_error_type_return_function(self):
        input ="""function (a:integer):{comment};"""
        expect ="Error on line 1 col 9: ("
        self.assertTrue(TestParser.test(input, expect,271))
    def test_error_lost_var_func_proc_declare(self):
        input = """(*var i:integer; procedure main(); begin end *)"""
        expect = "Error on line 1 col 47: <EOF>"
        self.assertTrue(TestParser.test(input,expect,272))
    def test_error_func_lost_type_array(self):
        input = """function foo():array[1 .. 80] of;
                    begin
                    end
                    """
        expect ="Error on line 1 col 32: ;"
        self.assertTrue(TestParser.test(input,expect,273))
    def test_error_proc_declare_proc(self):
        input = """
                    procedure proc1();
                    procedure proc2();
                    procedure proc();
                    begin end
                    begin end
                    """
        expect = "Error on line 3 col 20: procedure"
        self.assertTrue(TestParser.test(input,expect,274))
    def test_continue_compounment(self):
        input = """ procedure main();
                    var i,j: integer;
                    begin
                        for i:=1 to 1000 do
                            begin
                                i:=i+1;
                                if (i>10) then  break;
                                if ((i<= 10) or (i>=5)) then continue;
                            end
                    end
                    """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,275))
    def test_comment_in_program(self):
        input = """function fun1():integer;
                    //begin
                    begin
                    end
                    """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,276))
    def test_break_compoundment(self):
        input = """ procedure main();
                    var i,j: integer;
                    begin
                        for i:=10 to 100 do 
                            begin
                                i:=i+1;
                                if (i>50) then  break;
                            end
                    end
                    """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,277))
    def test_expression_compounment(self):
        input = """ procedure main();
                    var i,j: integer;
                    begin
                        for i:=10 to (i<>20) OR (a MOD 5) <> 2 do 
                            begin
                                i:=i+1;
                                if (i>50) then  break;
                            end
                    end
                    """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,278))
    def test_semi_error(self):
        input = """
                    function foo():integer;
                    begin
                        return 4*100;
                    end;
                    """
        expect = "Error on line 5 col 23: ;"
        self.assertTrue(TestParser.test(input,expect,279))
    def test_assign_in_expression(self):
        input = """ procedure main();
                    begin 
                            for i:=1 to i:=2 do
                                a:=5
                    end"""
        expect = "Error on line 3 col 41: :="
        self.assertTrue(TestParser.test(input, expect,280))
    def test_if_false(self):
        input = """function max (a,b: integer): real;
		var max: integer; 
		begin
		if a b then 
			max := a ;
		else
			max := b ;
		end""" 			
        expect = "Error on line 4 col 7: b"
        self.assertTrue(TestParser.test(input,expect,281))
    def test_if_true(self):
        input = """function tim_min (a,b: integer): real;
		var min: integer; 
		begin
		if a < b then 
			begin
				min := a ;
			end
		else
			begin
				min := b ;
			end
		end""" 			
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,282))
    def test_if_nest(self):
        input = """function tim_min (a,b: integer): real;
		var min: integer; 
		begin
		if a < b then 
			begin
				if a =1 then return 1;
			end
		else
			begin
				min := b ;
			end
		end""" 			
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,283))
    def test_error_var_dec(self):
        input = """procedure foo();
		var
		begin
		end""" 			
        expect = "Error on line 3 col 2: begin"
        self.assertTrue(TestParser.test(input,expect,284))
    def test_arr_false4(self):
        input = """var a,b : real;
		c,d: array [1 .. 5 .. 9] of string ;"""
        expect = "Error on line 2 col 21: .." 	
        self.assertTrue(TestParser.test(input,expect,285))
    def test_lost_name_proc(self):
        input = """ procedure ();
                    begin
                    """
        expect ="Error on line 1 col 11: ("
        self.assertTrue(TestParser.test(input,expect,286))
    def test_param_error(self):
        input = """procedure proc1(a,b: real,c: boolean);
		var e,f: integer; 		
		end""" 			
        expect = "Error on line 1 col 25: ,"
        self.assertTrue(TestParser.test(input,expect,287))
    def test_error_parram(self):
        input = """function now (a: integer str: string): real;
		begin 
		end""" 			
        expect = "Error on line 1 col 25: str"
        self.assertTrue(TestParser.test(input,expect,288))
    def test_assi_stmt(self):
        input = """ procedure main();
                    begin
                        a:=b:=c:= food()[2]:= x[6]:= x[t[4]]:=food();
                    end"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,289))
    def test_error_SEMI_dec(self):
        input = """function now (a: real): integer
		var str : string;
		begin 
		end""" 			
        expect = "Error on line 2 col 2: var"
        self.assertTrue(TestParser.test(input,expect,290))
    def test_error_LB(self):
        input = """function now a: real): integer;
		var str : string;
		begin 
		end""" 			
        expect = "Error on line 1 col 13: a"
        self.assertTrue(TestParser.test(input,expect,291))
    def test_error_COLON(self):
        input = """function now (a: real): integer;
		var str  string;
		begin 
		end""" 			
        expect = "Error on line 2 col 11: string"
        self.assertTrue(TestParser.test(input,expect,292))
    def test_while_do(self):
        input = """ procedure maiN();
                    begin
                        while i=3 do
                            while ((i = 5) AND (i = 6)) do
                                begin
                                    i:=i*i;
                                end
                    end
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,293))
    def test_while_nest_for(self):
        input = """ procedure maiN();
                    begin
                        while i=3 do
                            for i := i+2 to i<>10 do
                                begin
                                    i:=i*i;
                                end
                    end
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,294))
    def test_if_nest_while_nest_for(self):
        input = """ procedure maiN();
                    begin
                        if(1=1) then
                        while i=3 do
                            for i:=i+2 to i<>10 do
                                begin
                                    i:=i*i;
                                end
                    end
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,295))
    def test_if_no_else(self):
        input = """ procedure maiN();
                    begin
                        if(0-0)=5 then i:=i+1;
                        no else 
                            break;
                    end
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,296))
    def test_error_exp_for(self):
        input = """
                    function forl():integer;
                    begin
                        for i=1 to n do n:=n+1;
                    end
                """
        expect = "Error on line 4 col 29: ="
        self.assertTrue(TestParser.test(input,expect,297))
    def test_arr_index_error(self):
        input = """var i,j : array [12] of string ;""" 			
        expect = "Error on line 1 col 19: ]"
        self.assertTrue(TestParser.test(input,expect,298))
    def test_array_error(self):
        input = """var x,y : [25 .. 28] of string ;""" 			
        expect = "Error on line 1 col 10: ["
        self.assertTrue(TestParser.test(input,expect,299))
    def test_array_error_dot(self):
        input= """var x : array [12 .. 79] of real;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,300))
    def test_array_error_do1t(self):
        input= """
                      procedure main();
                 begin
                     Writeln("Ent");
                     end 
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,301))
    