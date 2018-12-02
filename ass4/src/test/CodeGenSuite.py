import unittest
from TestUtils import TestCodeGen
from AST import *
from StaticCheck import *
from CodeGenerator import *

class CheckCodeGenSuite(unittest.TestCase):
	
	def test_1(self):
		input = """
				var a: real;
				var b: integer;
				procedure foo(c:real);
					var d : real;
					begin  
						d :=c;
						putFloat(d); 
					end
				procedure main();
					var e : integer;
					begin 
						a := 5;
						putFloatLn(6+9.5);
						foo(a);
					end
				"""
		expect = "15.5\n5.0"
		self.assertTrue(TestCodeGen.test(input,expect,500))
	
	def test_int_assign_call(self):
		input = """
				var a: real;
				procedure foo(c:integer);
					var d : real;
					begin  
						d :=c;
						putFloat(d); 
					end
				procedure main();
					var e : integer;
					begin 
						e := 5;
						foo(e);
					end
				"""
		expect = "5.0"
		self.assertTrue(TestCodeGen.test(input,expect,501))
	
	def test_int_assign_call2(self):
		input = """
				var a: real;
				procedure foo(c:integer; d:integer);
					begin  
						d :=c;
						putFloat(c); 
					end
				procedure main();
					var e : integer;
					begin 
						e := 5;
						foo(e,5);
					end
				"""
		expect = "5.0"
		self.assertTrue(TestCodeGen.test(input,expect,502))
	
	def test_int_assign_call3(self):
		input = """
				var a: real;
				procedure foo(c:integer; d:real);
					begin  
						d :=c;
						putFloat(c); 
					end
				procedure main();
					var e : integer;
					begin 
						a := e:= 5;
						foo(e,a);
					end
				"""
		expect = "5.0"
		self.assertTrue(TestCodeGen.test(input,expect,503))

	def test_int_assign_call4(self):
		input = """
				var a: real;
				procedure foo(c:integer; d:real);
					begin  
						putInt(c); 
						putFloat(d);
					end
				procedure main();
					var e : integer;
					begin 
						e:= 5 + 8 +6;
						a:= e + 5.66;
						foo(e,a);
					end
				"""
		expect = "1924.66"
		self.assertTrue(TestCodeGen.test(input,expect,504))
	
	def test_int_assign_call5(self):
		input = """
				var a: real;
				procedure foo(c:integer; d:real ; e:integer);
					begin  
						putFloat(d+c+e);
					end
				procedure main();
					var e : integer;
					begin 
						e:= 5 ;
						a:= e + 5.66;
						foo(e,a,5);
					end
				"""
		expect = "20.66"
		self.assertTrue(TestCodeGen.test(input,expect,505))
	
	def test_if_else_1(self):
		input = """
				var a: real;
				procedure foo(c:integer; d:real ; e:integer);
					begin  
						if false then
							putInt(c);
						else
							putFloatLn(d);
					end
				procedure main();
					var e : integer;
					begin 
						e:= 5 ;
						a:= e + 5.66;
						foo(e,a,5);
					end
				"""
		expect = "10.66\n"
		self.assertTrue(TestCodeGen.test(input,expect,506))
	
	def test_if_else_2(self):
		input = """
				var a: real;
				procedure foo(c:integer; d:real ; e:integer);
					begin  
						if true then
							putInt(c);
						else
							putFloatLn(d);
					end
				procedure main();
					var e : integer;
					begin 
						e:= 5 ;
						a:= e + 5.66;
						foo(e,a,5);
					end
				"""
		expect = "5"
		self.assertTrue(TestCodeGen.test(input,expect,507))

	def test_if_then_1(self):
		input = """
				var a: real;
				procedure foo(c:integer; d:real ; e:integer);
					begin  
						if false then
							putInt(c);
					end
				procedure main();
					var e : integer;
					begin 
						e:= 5 ;
						a:= e + 5.66;
						foo(e,a,5);
					end
				"""
		expect = ""
		self.assertTrue(TestCodeGen.test(input,expect,508))

	def test_if_else_string_2(self):
		input = """
				var a: real;
				procedure foo(c:integer; d:integer;e:string);
					begin 
						if (false) then
							putInt(1);
						else 
							putString(e);
					end
				procedure main();
					var str : String;
					begin 
						str := "cao thanh tung";
						foo(5,6,str);
					end
				"""
		expect = "cao thanh tung"
		self.assertTrue(TestCodeGen.test(input,expect,509))

	def test_binary1(self):
		input = """
				var a: real;
				procedure foo();
					begin 
						
					end
				procedure main();
					var b : integer;
					begin 
						a := 5 + 6.5;
						putFloat(a);
						a := a*2;
						putFloat(a);
						a := a/5;
						putFloat(a);
						b := 5 div 2;
						putInt(b);
						b := 5 mod 2;
						putInt(b);
					end
				"""
		expect = "11.523.04.621"
		self.assertTrue(TestCodeGen.test(input,expect,510))
	
	def test_binary2(self):
		input = """
				var a: real;
				procedure foo();
					begin 
						
					end
				procedure main();
					var b : boolean;
					begin 
						b := 6 >= 6;
						putBool(b);
						b := 5 < 6.5;
						putBool(b);
						b := 5 > 6.5;
						putBool(b);
						b := 5.5 <> 5.5;
						putBool(b);
						b := 6 = 8;
						putBool(b);
						b := 6 = 6;
						putBool(b);
						b := 6.5 > 8;
						putBool(b);
					end
				"""
		expect = "truetruefalsefalsefalsetruefalse"
		self.assertTrue(TestCodeGen.test(input,expect,511))

	def test_binary3(self):
		input = """
				var a: boolean;
				procedure foo();
					begin 
						
					end
				procedure main();
					var b : boolean;
					begin 
						b := true;
						a := b and False;
						putBool(a);
						a := b or False;
						putBool(a);
					end
				"""
		expect = "falsetrue"
		self.assertTrue(TestCodeGen.test(input,expect,512))
	
	def test_while1(self):
		input = """
				var a: integer;
				procedure foo();
					begin 
						
					end
				procedure main();
					var b : boolean;
					begin 
						a:=10;
						while (a < 15) do
						begin 
							a := a +1;
							putInt(5);
						end
					end
				"""
		expect = "55555"
		self.assertTrue(TestCodeGen.test(input,expect,513))

	def test_with1(self):
		input = """
				var a: integer;
				procedure foo();
					begin 
						
					end
				procedure main();
					var b : boolean;
					begin 
						a:=10;
						with a,b:integer;c:real;
                        do begin
							a:=5;
							putInt(a);
						end
					end
				"""
		expect = "5"
		self.assertTrue(TestCodeGen.test(input,expect,514))

	def test_with_while1(self):
		input = """
				var a: integer;
				procedure foo();
					begin 
						
					end
				procedure main();
					var b : boolean;
					begin 
						a:=10;
						with a,b:integer;c:real;
                        do begin
							a:=5;
							while(a< 10) do begin
								if (a=5) then a:=7;
								else a:= a+1;
								putInt(a);
							end
						end
					end
				"""
		expect = "78910"
		self.assertTrue(TestCodeGen.test(input,expect,515))

	def test_break_continue(self):
		input = """
				var a: integer;
				procedure foo();
					begin 
						
					end
				procedure main();
					var b : boolean;
						a : integer;
					begin 
						a:=1;
						while(a<10)do
						begin
							if (a=2) then 
							begin 
								a:=a+2;
								continue;
							end
							else putInt(a);
							if a= 7 then break;
							a:=a+1;
						end
					end
				"""
		expect = "14567"
		self.assertTrue(TestCodeGen.test(input,expect,516))
	
	def test_for_break_continue(self):
		input = """
				procedure main();
					var x : integer;
					begin 
						for x:= 1 to 5+5 do
							if x = 5 then continue;
							else 
							begin 
								putInt(x);
								if x = 8 then break;
							end
					end
				"""
		expect = "1234678"
		self.assertTrue(TestCodeGen.test(input,expect,517))
	
	def test_fuentionsimple(self):
		input = """
				function foo(a :integer):boolean;
				begin
					return true;
				end
				procedure main();
					var x : boolean;
					begin 
						x := foo(5);
						putBool(x);
					end
				"""
		expect = "true"
		self.assertTrue(TestCodeGen.test(input,expect,518))
	
	def test_fuentionsimple_real(self):
		input = """
				function foo(a :integer):real;
				begin
					return a/6;
				end
				procedure main();
					var x : real;
					begin 
						x := foo(5);
						putFloat(x);
					end
				"""
		expect = "0.8333333"
		self.assertTrue(TestCodeGen.test(input,expect,519))

	def test_fuentionsimple_returnreal(self):
		input = """
				function foo(i :integer):real;
				begin
					while (i <10) do
					begin
						if i = 4 then return 3.0;
						else i:=i+1;
					end
					return 6.0;
				end
				procedure main();
					var x : real;
					begin 
						x := foo(1);
						putFloat(x);
					end
				"""
		expect = "3.0"
		self.assertTrue(TestCodeGen.test(input,expect,520))

	def test_unary1(self):
		input = """
				procedure main();
					var x : integer;
						y : boolean;
					begin 
						x := -5;
						putInt(x);
						y := not true;
						putBool(y);
					end
				"""
		expect = "-5false"
		self.assertTrue(TestCodeGen.test(input,expect,521))
	
	def test_unary2(self):
		input = """
				procedure main();
					var x : integer;
						y : boolean;
					begin 
						x := -5 +1;
						putInt(x);
						y := not true;
						putBool(y);
					end
				"""
		expect = "-4false"
		self.assertTrue(TestCodeGen.test(input,expect,522))

	def test__andthen(self):
		input = """
				procedure main();
					var x : integer;
						y : boolean;
					begin 
						y := false and then true;
						putBool(y);
						y := true and then true;
						putBool(y);
						y := true and then false;
						putBool(y);
					end
				"""
		expect = "falsetruefalse"
		self.assertTrue(TestCodeGen.test(input,expect,523))

	def test__orelse(self):
		input = """
				procedure main();
					var x : integer;
						y : boolean;
					begin 
						y := false or else false;
						putBool(y);
						y := true or else true;
						putBool(y);
						y := true or else false;
						pUTBool(y);
					end
				"""
		expect = "falsetruetrue"
		self.assertTrue(TestCodeGen.test(input,expect,524))
	
	def test__7(self):
		input = """
				procedure main();
					var i,j : integer;
					begin 
						for i:= 1 to 5*2 do
							with k :integer; do
							begin 
								k:=i*2;
								if (i>3) then
								begin
									for j:=1 to k do
										putInt(j);
								end
							end 
					end
				"""
		expect = "12345678123456789101234567891011121234567891011121314123456789101112131415161234567891011121314151617181234567891011121314151617181920"
		self.assertTrue(TestCodeGen.test(input,expect,525))

	def test__7(self):
		input = """
				var a,b,c :integer;
				procedure main();
					begin 
						a:=1;
						if a = 1 then
							begin
								with a:integer; do
									begin 
										for a:= 2 to 3 do 
											begin
											with b:integer; do begin putIntLn(a); end
											end
									end
								with a:integer; do
									begin 
										for a:=7 to 8 do
											begin
											with b:integer; do begin putIntLn(a); end
											end
									end
								with c:integer; do
									begin
										putInt(a);
									end
								return;
							end
					end
				"""
		expect = "2\n3\n7\n8\n1"
		self.assertTrue(TestCodeGen.test(input,expect,526))

	def test__mp(self):
		input = """
				var i : integer ;
				function f(): integer;
				begin
					return 200;
				end
				procedure main();
				var main : integer ;
				begin
					main := f();
					putIntLn(main);
					with
						i : integer ;
						main : integer ;
						f : integer ;
					do begin
						main := f := i := 100;
						putIntLn(i);
						putIntLn(main);
						putIntLn(f);
					end
					putIntLn(main);
					end
					var g:real;
				"""
		expect = "200\n100\n100\n100\n200\n"
		self.assertTrue(TestCodeGen.test(input,expect,527))

	def test__mpreturn_if(self):
		input = """
				var i : integer ;
				function f(a:integer): integer;
				begin
					if a > 1 then return 5;
					else begin
					return 200;
					return 4; end
				end
				procedure main();
				var a : integer ;
				begin
					putInt(f(5));
				end
				"""
		expect = "5"
		self.assertTrue(TestCodeGen.test(input,expect,528))

	def test__mpreturn_i_procedure(self):
		input = """
				var i : integer ;
				procedure f(a:integer);
				begin
					if a > 1 then return ;
					putInt(a);
				end
				procedure main();
				var a : integer ;
				begin
					F(5);
					F(0);
				end
				"""
		expect = "0"
		self.assertTrue(TestCodeGen.test(input,expect,529))
	def test__mpreturn_stri_procedure(self):
		input = """
				var i : integer ;
				procedure f(a:integer);
				begin
					if a > 1 then 
					putInt(a);

					PuTSTring("hehe");
				end
				procedure main();
				var a : integer ;
				begin
					F(5);
					F(0);
				end
				"""
		expect = "5hehehehe"
		self.assertTrue(TestCodeGen.test(input,expect,530))

	def test____31(self):
		input = """
        var a ,b,c: real; out:boolean;
		function foo(c:real): real;
        begin if c<0 then return 1.2; else return 1.3; end
        procedure main();
		begin
                c:=1;
                if c<>3 then 
                    if c<0 then 
                    putfloatln(c/2);
                    else c:=foo(0);
                putfloatln(c);
        end
		
		"""
    	
		expect = """1.3\n"""
		self.assertTrue(TestCodeGen.test(input,expect,531)) 
    
	def test____32(self):
		input = """
        var a ,b,c: real; out:boolean;
		function foo(c:real): real;
        begin if c<0 then return 1.2; else return 1.3; end
        procedure main();
		begin c:=0;
               while true do begin c:=3; if c=3 then break; else continue; end
                if c<>3 then begin end
                else while c=3 do begin putfloat(c);c:=c-1; break; end
        end
		
		"""
    	
		expect = """3.0"""
		self.assertTrue(TestCodeGen.test(input,expect,532)) 
    
	def test_33(self):
		input = """
        var a ,b,c: real; out:boolean;
		function foo(c:real): real;
        begin if c<0 then return 1.2; else return 1.3; end
        procedure main();
		begin   c:=foo(1------------------------------------3);
               putfloatLN(c/c); 
                return;

        end
		
		"""
    	
		expect = """1.0\n"""
		self.assertTrue(TestCodeGen.test(input,expect,533)) 
    
	def test_34(self):
		input = """
        var a ,b,c: real; out:boolean;
		function foo(c:integer): boolean;
        begin if c mod 2 =0 then return TRUE; else return FaLSE; end
        procedure main();
		begin   out:=foo(1024);
               if out then putstring("so chan");

            else putstring("so 0 chan");
        end
		
		"""
    	
		expect = """so chan"""
		self.assertTrue(TestCodeGen.test(input,expect,534)) 
    
	def test___35(self):
		input = """
        var a ,b,c: real; out:boolean;
		
        procedure main();
		begin  
                putfloat(1/2/2);
        end
		
		"""
    	
		expect = """0.25"""
		self.assertTrue(TestCodeGen.test(input,expect,535)) 
    
	def test_____36(self):
    	
		input = """
        var a ,b,c: real; out:boolean;
		
        procedure main();
		begin  
                c:=1.2/2.4; 
                b:=1;
                while true do
                begin putfloat(c+0.5); b:=b+1; if b=4 then break; end
        end
		
		"""
    	
		expect = """1.01.01.0"""
		self.assertTrue(TestCodeGen.test(input,expect,536)) 
    
	def test____37(self):
    	
		input = """
        var a ,b,c: real; out:boolean;
		
        procedure MAIN();
		begin  
               putstring("test");
                     return;
        end   
		
		"""
    	
		expect = """test"""
		self.assertTrue(TestCodeGen.test(input,expect,537)) 
    
	def test___38_(self):
    	
		input = """
        var a ,b,c: real; out:boolean;
		
        procedure main();
		begin  
                 main1();
                 main2();
                     return;
        end   
		procedure main1();
		begin  
                 putint(123);
                     return;
        end
        procedure main2();
		begin  
                 putint(1234);
                     return;
        end
		"""
    	
		expect = """1231234"""
		self.assertTrue(TestCodeGen.test(input,expect,538)) 

    
	def test___39_(self):
    	
		input = """
        var a ,b,c: real; out:boolean;
		
        procedure main();
		begin  
                 main1();
                 main2();
                 putint(1);
                     return;
        end   
		procedure main1();
		begin  
                 while false do
                     return;
        end
        procedure main2();
		begin  
                
                     return;
        end
		"""
    	
		expect = """1"""
		self.assertTrue(TestCodeGen.test(input,expect,539)) 

    
	def test____40(self):
    	
		input = """
        var a ,b,c: real; out:boolean;
		
        procedure main();
		begin  
                 main1();
                 main2();
                 putbool(true);
                     return;
        end   
		procedure main1();
        var i:integer;
		begin  
                for i:=1 to 10 do
                     return;
        end
        procedure main2();
		begin  
                 
                     return;
        end
		"""
    	
		expect = """true"""
		self.assertTrue(TestCodeGen.test(input,expect,540)) 

    
	def test____41(self):
		input = """
        var a ,b,c: real; out:boolean;
		
        procedure main();
		begin  
               if true then
                     return;
        end   
	
		"""
		expect = """"""
		self.assertTrue(TestCodeGen.test(input,expect,541)) 

    
	def test____42(self):
		input = """
        var a ,b,c: real; out:boolean;
		
        procedure main();
		begin  
        c:=400;
                if c=400/1 then putstring("chia het cho 4");
                  else if c = 200 then    return;
        end   
		
		"""
    	
		expect = """chia het cho 4"""
		self.assertTrue(TestCodeGen.test(input,expect,542)) 
    
	def test_____43(self):
		input = """
        var a ,b,c: real; out:boolean;
		
        procedure main();
		begin  
                 main1();
                 main2();
                     return;
        end   
		procedure main1();
		begin  
                 putint(123);
                     return;
        end
        procedure main2();
		begin  
                 putint(1234);
                     return;
        end
		"""
		expect = """1231234"""
		self.assertTrue(TestCodeGen.test(input,expect,543)) 

    
	def test_____44(self):
    
		input = """
        
		function foo(a:real):boolean;
        begin putint(2); return true; end
        function foo1():boolean;
        begin putfloat(2/0); return true; end
        procedure MAIN();
		begin  
        
             if true or  foo(1) then begin   end
             if true or else  foo(1) then begin   end
             if false and  foo(1) then begin   end
             if false and then   foo(1) then begin   end

            if false and then foo1()  then begin   end
            if 1>2 then putstring("xong");
             if 1.0>2.3 then putstring("roi");
              if 1>2.8 then putstring("nha");
               if 1.21>2 then putstring("may");
                if 1.212122>1.2121223 then putstring("may");
               putstring("xong");
        end   
		
		"""
    
		expect = "22xong"
		self.assertTrue(TestCodeGen.test(input,expect,544)) 
    
	def test___45(self):
    
		input = """procedure main();
        var a,b,c:integer;
        begin 
          c := foo();    
          putInt(c); 
        end
         function foo():integer;
          var a,b:integer;
         begin
            a := 5;
            b := 6;
            if (a > b) then return 5;
            else return 6;
        end
		"""
    
		expect = "6"
		self.assertTrue(TestCodeGen.test(input,expect,545)) 
	
	def test_for_dowto(self):
		input = """
				procedure main();
				var a ,b: integer;
				begin
					a:= 5-1;
					for a:=10 downto 1 do
						putInt(a);
				end
				"""
		expect = "10987654321"
		self.assertTrue(TestCodeGen.test(input,expect,546))
	
	def test_for_dowt2o(self):
		input = """
				procedure main();
				var a ,b: integer;
				begin
					a:= 5-1;
					for a:=10 downto 1 do
						putInt(a);
				end
				"""
		expect = "10987654321"
		self.assertTrue(TestCodeGen.test(input,expect,547))
	
	def test_if_548(self):
        
		input = """

        procedure main();
        begin
            if 10 <> 10 then
            begin end
            else
                putString("10 <> 10");
        end
        """
		expect = "10 <> 10"
		self.assertTrue(TestCodeGen.test(input, expect, 548))

	def test_if_549(self):
		input = """
        procedure main();
        begin
            if 1.0 >= -1.0 then
                putStringLn("1.0 >= -1.0");
            putString("Hi");
        end
        """
        
		expect = "1.0 >= -1.0\nHi"
		self.assertTrue(TestCodeGen.test(input, expect, 549))

    
	def test_assign_550(self):
		input = """
        var globalInt:integer;
        globalFloat:real;
        globalBool:boolean;

        procedure main();
        var localInt:integer;
        localFloat:real;
        localBool:boolean;
        begin
            globalInt := localInt := 0;
            globalFloat := localFloat := 1;
            localBool := globalBool := not not not true;
            putIntLn(globalInt);
            putIntLn(localInt);
            putFloatLn(globalFloat);
            putFloatLn(localFloat);
            putBoolLn(localBool);
            putBoolLn(globalBool);
        end
        """
        
		expect = "0\n0\n1.0\n1.0\nfalse\nfalse\n"
		self.assertTrue(TestCodeGen.test(input, expect, 550))

	def test_551(self):
        
		input = """
        var x:integer;
        procedure main();
        begin
            x := 1;
            foo(x, 1.0);
            putInt(x);
        end

        procedure foo(i: integer; f: real);
        var bar:boolean;
        begin
            bar := true;
            putBool(bar);
            i := 2;
            putInt(i);
        end
        """
        
		expect = "true21"
		self.assertTrue(TestCodeGen.test(input, expect, 551))

    
	def test_with_552(self):
        
		input = """
        var i:integer;
        procedure main();
        begin
            i := 1;
            with i:integer; do
            begin
                i := 2;
                putInt(i);
            end
            putInt(i);
        end
        """
        
		expect = "21"
		self.assertTrue(TestCodeGen.test(input, expect, 552))

    
	def test_if_553(self):
        
		input = """
        procedure main();
        begin
            if true then
                putBool(true);
            else
                putBool(false);
        end
        """
        
		expect = "true"
		self.assertTrue(TestCodeGen.test(input, expect, 553))

	def test_if_554(self):
        
		input = """
        procedure main();
        begin
            if false then
                putBool(true);
            else
                putBool(false);
        end
        """
        
		expect = "false"
        
		self.assertTrue(TestCodeGen.test(input, expect, 554))

    
	def test_for_555(self):    
		input = """
        var i:integer;
        procedure main();
        var x:integer;
        begin
            x := 0;
            for x:=1 to 3 do
            begin
                putInt(x);
            end
        end
        """
        
		expect = "123"
        
		self.assertTrue(TestCodeGen.test(input, expect, 555))

    
	def test_for_556(self):   
		input = """
        var i:integer;
        procedure main();
        var x:integer;
        begin
            x := 0;
            for x:=1 to 3 do
            begin
                putInt(x);
            end
        end
        """
        
		expect = "123"
        
		self.assertTrue(TestCodeGen.test(input, expect, 556))

	def test_for_557(self):   
		input = """
        var i:integer;
        procedure main();
        var x:integer;
        begin
            x := 0;
            for x:=1 to 3 do
            begin
                putInt(x);
            end
        end
        """
        
		expect = "123"
        
		self.assertTrue(TestCodeGen.test(input, expect, 557))

	def test_while_558(self):
        
		input = """
        procedure main();
        var i : integer;
        begin
            while FALSE do
                putString("false");
            while -256 > -1 do
            begin
                putString("-256 > -1");
            end
        end
        """
        
		expect = ""
        
		self.assertTrue(TestCodeGen.test(input, expect, 558))

	def test_while_559(self):
        
		input = """
        procedure main();
        var b : boolean;
        begin
            b := true;
            while B do
            begin
                b := not b;
                putBool(b);
            end
        end
        """

		expect = "false"
        
		self.assertTrue(TestCodeGen.test(input, expect, 559))

	def test_while_560(self):
        
		input = """
        procedure main();
        var i : integer;
        begin
            i := 10;
            while i = 10 do
            begin
                putIntLn(i);
                i := 11;
            end
            putIntLn(i);
        end
        """

		expect = "10\n11\n"
        
		self.assertTrue(TestCodeGen.test(input, expect, 560))

	def test_while_561(self):
        
		input = """
        procedure main();
        var a, b : real;
        begin
            a := 100;
            b := -100;
            while a <> b do
            begin
                a := -1 + a;
                b := 1 + b;
            end
            putFloat(a - b);
        end
        """

		expect = "0.0"
        
		self.assertTrue(TestCodeGen.test(input, expect, 561))

	def test_while_562(self):
		input = """
        procedure main();
        var i : integer;
        begin
            i := 0;
            while i mod 3 = 0 do
            begin
                i := i + 3;
                if i = 99 then i := i + 1;
            end
            putInt(i);
        end
        """
        
		expect = "100"
        
		self.assertTrue(TestCodeGen.test(input, expect, 562))

	def test_while_563(self):
        
		input = """
        function isPositive(i:integer):boolean;
        begin
            return i >= 0;
        end

        function getMaxInt():integer;
        var i: integer;
        begin
            i := 0;
            while isPositive(i) and isPositive(i + 1) do
            begin
                i := i + 1;
            end
            return i;
        end

        procedure main();
        var i : integer;
        begin
            putInt(getMaxInt());
        end
        """
        
		expect = "2147483647"
        
		self.assertTrue(TestCodeGen.test(input, expect, 563))

	def test_while_564(self):
        
		input = """
        procedure main();
        var i,j,counter : integer;
        begin
            i := counter := 0;
            while i < 3 do
            begin
                j := 0;
                while j < 4 do
                begin
                    j := j + 1;
                    counter := counter + 1;
                end
                i := i + 1;
            end
            putInt(counter);
        end
        """
        
		expect = "12"
        
		self.assertTrue(TestCodeGen.test(input, expect, 564))

	def test_while_565(self):
		input = """
        procedure main();
        var i,j,k,counter : integer;
        begin
            i := counter := 0;
            while i < 3 do
            begin
                j := 0;
                while j < 4 do
                begin
                    k := 0;
                    while k < 5 do
                    begin
                        k := k + 1;
                        counter := counter + 1;
                    end
                    j := j + 1;
                end
                i := i + 1;
            end
            putInt(counter);
        end
        """
		expect = "60"
        
		self.assertTrue(TestCodeGen.test(input, expect, 565))

	def test_while_566(self):
		input = """
        procedure main();
        begin
            while not true do
                while not false do
                    while true do
                        WHILE TRUE and TRUE do
                            putInt(-999);
        end
        """
		expect = ""
		self.assertTrue(TestCodeGen.test(input, expect, 566))

	def test_for_567(self):
		input = """
        procedure main();
        var i : integer;
        begin
            for i := 1 to 9 do
                putInt(i);
        end
        """
		expect = "123456789"
		self.assertTrue(TestCodeGen.test(input, expect, 567))

	def test_for_568(self):
		input = """
        procedure main();
        var i : integer;
        begin
            for i := -5 to -1 do
                putInt(i);
        end
        """
		expect = "-5-4-3-2-1"
		self.assertTrue(TestCodeGen.test(input, expect, 568))

	def test_for_569(self):
        
		input = """
        procedure main();
        var i : integer;
        begin
            for i := 1 to 3 do
            begin end
            putInt(i);
        end
        """
        
		expect = "4"
        
		self.assertTrue(TestCodeGen.test(input, expect, 569))

	def test_for_570(self):
		input = """
        procedure main();
        var i : integer;
        begin
            for i := 9 downto 1 do
            begin
                putInt(i);
            end
        end
        """
        
		expect = "987654321"
        
		self.assertTrue(TestCodeGen.test(input, expect, 570))
	
	def test_for_571(self):
	    input = """
        procedure main();
        var i : integer;
        begin
            for i := -1 downto -4 do
            begin
                putInt(i);
            end
            putInt(i);
        end
        """
	    expect = "-1-2-3-4-5"
	    self.assertTrue(TestCodeGen.test(input, expect, 571))

	def test_for_572(self):
	    input = """
        procedure main();
        var i : integer;
        begin
            for i := 0 to 10 do
            begin
                if i mod 2 = 0 then
                    putInt(i);
            end
        end
        """
	    expect = "0246810"
	    self.assertTrue(TestCodeGen.test(input, expect, 572))

	def test_for_573(self):
	    input = """
        procedure main();
        var i,j,counter : integer;
        begin
            counter := 0;
            for i := 0 to 10 do
                for j := 0 to 10 do
                    counter := counter + 1;
            putInt(counter);
        end
        """
	    expect = "121"
	    self.assertTrue(TestCodeGen.test(input, expect, 573))

	def test_for_574(self):
	    input = """
        procedure main();
        var i,j,k,counter : integer;
        begin
            counter := 0;
            for i := 9 downto 1 do
                for j := 8 downto 1 do
                    for k:= 7 downto 1 do
                        counter := counter + 1;
            putBool(counter = 7*8*9);
        end
        """
	    expect = "true"
	    self.assertTrue(TestCodeGen.test(input, expect, 574))

	def test_for_575(self):
	    input = """
        procedure main();
        var i : integer;
        begin
            for i:= 10 div 10 to 9 * 19 div 10 do
                while 5 > i do
                begin
                    putInt(i);
                    i := i + 1;
                end
            putStringLn("");
            putInt(i);
        end
        """
	    expect = "1234\n18"
	    self.assertTrue(TestCodeGen.test(input, expect, 575))

	def test_for_576(self):
	    input = """
        procedure main();
        var i,j,counter : integer;
        begin
            counter := 0;
            for i:= 1 to 20000 do
                for j := 20000 downto 1 do
                    counter := counter - 1;
            putInt(counter);
        end
        """
	    expect = "-400000000"
	    self.assertTrue(TestCodeGen.test(input, expect, 576))

	def test_____577(self):
	    input = """
        var i:integer;
        procedure main();
        begin
            for i:=9 downto 5 do
                if i mod 3 = 0 then
                    putfloatln(i div 3);
        end
        """
	    expect = "3.0\n2.0\n"
	    self.assertTrue(TestCodeGen.test(input, expect, 577))

	def test___578(self):
		input = """
			procedure main();
			var a ,b: integer;
			begin
				for a:=10 downto 1 do
					putInt(a);
			end
			
			"""
		expect = """10987654321"""	
		self.assertTrue(TestCodeGen.test(input,expect,578))

	def test_for_579(self):
	    input = """
        var i:integer;
        procedure main();
        begin
            for i:=-100 to 100 do
                for i:= 0 to 100 do begin end
            putInt(i);
        end
        """
	    expect = "102"
	    self.assertTrue(TestCodeGen.test(input, expect, 579))

	def test_break_continue_580(self):
	    input = """
        var i:integer;
        procedure main();
        begin
            for i:= 0 to 10 do
                if i > 5 then break;
            putIntLn(i);

            for i:= 0 to 100 do
            begin
                if i >= 10 then continue;
                else putInt(i);
            end
        end
        """
	    expect = "6\n0123456789"
	    self.assertTrue(TestCodeGen.test(input, expect, 580))


	def test_break_continue_582(self):
	    input = """
        procedure main();
        var i : integer;
        begin
            for i := -10000 to 10000 do
            begin
                if i*i > 9 then continue;
                PUTINTln(i);
            end
        end
        """
	    expect = "-3\n-2\n-1\n0\n1\n2\n3\n"
	    self.assertTrue(TestCodeGen.test(input, expect, 582))

	def test_break_continue_583(self):
	    input = """
        procedure main();
        var i: integer;
        begin
            while True do
            begin
                while true do
                begin
                    while not false do
                        break;
                    break;
                end
                break;
            end
            for i := -10000 to 10000 do
            begin
                if i*i > 9 then continue;
                PUTINTln(i);
            end
        end
        """
	    expect = "-3\n-2\n-1\n0\n1\n2\n3\n"
	    self.assertTrue(TestCodeGen.test(input, expect, 583))

	def test_break_continue_584(self):
	    input = """
        var i : integer;
        procedure main();
        begin
            for i:=90 downto 0 do
                if i mod 10 <> 0 then continue;
                else
                    putFloatLn(i / 10);
        end
        """
	    expect = "9.0\n8.0\n7.0\n6.0\n5.0\n4.0\n3.0\n2.0\n1.0\n0.0\n"
	    self.assertTrue(TestCodeGen.test(input, expect, 584))

	def test_return_585(self):
	    input = """
        procedure main();
        begin
            if true then return;
            else putString("HUYTC");
        end
        """
	    expect = ""
	    self.assertTrue(TestCodeGen.test(input, expect, 585))

	def test_return_586(self):
	    input = """
        function fib(n:integer):integer; //calculate the nth Fibonacci number
        begin
            if n < 0 then return -1;
            else if n = 0 then return 0;
            else if n = 1 then return 1;
            else return fib(n - 1) + fib(n - 2);
        end

        procedure main();
        var i : integer;
        begin
            putIntLn(fib(-100));
            for i := 0 to 10 do
                putIntLn(fib(i));
        end
        """
	    expect = "-1\n0\n1\n1\n2\n3\n5\n8\n13\n21\n34\n55\n"
	    self.assertTrue(TestCodeGen.test(input, expect, 586))

	def test_81(self):
		input = """
        function fibonacy(n : integer):integer;
        begin
        
        if (n<=1)  then return n;
        else return fibonacy(n-1)+fibonacy(n-2);
        end
		procedure main();
		var a ,b: integer;
		begin
			
				putInt(fibonacy(21));
        end
		
		"""
		expect = """10946"""
		self.assertTrue(TestCodeGen.test(input,expect,587)) 

	def test_with_588(self):
	    input = """
        procedure main();
        var i : integer;
        begin
            i := 0;
            putIntLn(i);
            with i:integer; do
            begin
                i := 8;
                putIntLn(i);
            end
            putIntLn(i);
        end
        """
	    expect = "0\n8\n0\n"
	    self.assertTrue(TestCodeGen.test(input, expect, 588))

	def test_with_589(self):
	    input = """
        procedure main();
        var i : integer;
        begin
            i := 0;
            putIntLn(i);
            with i:real; do
            begin
                i := 8;
                putFloatLn(i);
            end
            putIntLn(i);
        end
        """
	    expect = "0\n8.0\n0\n"
	    self.assertTrue(TestCodeGen.test(input, expect, 589))

	def test_with_590(self):
	    input = """
        var i : integer;
				procedure foo();
				begin
					i := 0;
					putint(i);
					with i:integer; do
						with f,i:real; do
							with i:boolean; do
							begin
								i := 1 > -5;
								putBool(i);
							end
				end

				procedure main();
				var i : integer;
				begin
					i := -1;
					putint(i);
					foo();
					putint(i);
				end
        """
	    expect = "-10true-1"
	    self.assertTrue(TestCodeGen.test(input, expect, 590))
	
	def test_exp_520(self):
		input = """
        procedure main();
        begin
            putFloatLn(----------3.14e10);
            putIntLn(0 div 1);
            putFloat(-0 / -1);
        end
		"""
    	
		expect = "3.13999995E10\n0\n-0.0"
    	
		self.assertTrue(TestCodeGen.test(input, expect, 591))

	def test_if_543(self):
    	
		input = """
        	function abs(i:integer):integer;
        begin
            if i >= 0 then
                return i;
            else
                return -i;
        end

        procedure main();
        begin
            putIntLn(abs(167));
            putIntLn(abs(-167));
            putIntLn(abs(167)-abs(-167));
        end
        """
    	
		expect = "167\n167\n0\n"
    	
		self.assertTrue(TestCodeGen.test(input, expect, 592))
	
	def test_program_final1(self):
		input = """
				function foo():integer;
                var a:integer;
                begin
                    a := 1;
					while(a<10) do
					begin 
						if( a = 5 ) then return 4;
						else if (a >4) then return 3;
						a := a+1;
						if(a = 3) then break;
						else continue;
					end
					return 1;
                end
            procedure main();
                begin 
                    putInt(foo()); 
                end
        """
    	
		expect = "1"
    	
		self.assertTrue(TestCodeGen.test(input, expect, 593))

	def test_program_final12(self):
	    input = """
            function foo():integer;
                var a:integer;
                begin
                    a := 2;
                    if (a < 6) then 
                        begin
                            if (a>4) then 
                                return 10; 
                        end
                    else
                        begin
                            return 20;
                        end
                    return 10;
                end
            procedure main();
                begin 
                    putInt(foo()); 
                end
        """
	    expect = "10"
	    self.assertTrue(TestCodeGen.test(input, expect, 594))
    
	
	def test_program_final13(self):
	    input = """
            PROCEDURE main(); 
                VAR a : integer;
                BEGIN 
                    if (2 > 1) then
                        begin 
                        end
                    else
                        putString("tung");
                    putString("hello");
                END
            VAR b : real;
			"""
	    expect = "hello"
	    self.assertTrue(TestCodeGen.test(input, expect, 595))
        
	def test_program_final14(self):
	    input = """
            procedure main();
                begin
                    if 10 <> 10 then
                        begin
                        end
                    else
                        putString("10 <> 10");
                end
        """
	    expect = "10 <> 10"
	    self.assertTrue(TestCodeGen.test(input,expect,596))      
        
	def test_complex_9(self):
		input = """
            function gt(i : integer): integer;
                begin
                    if i <= 1 then return 1;
                    else
                        retuRn i*gt(i-1);
                end
            procedure main();
            var a:integer;
                Begin
                    a:=10;
                    putint(gt(a));
                end
        """
		expect = """3628800"""
		self.assertTrue(TestCodeGen.test(input,expect,597))

	def test_complex_10(self):
		input = """
            procedure main();
                var n : integer;
                    c : boolean;
                Begin
                    n := 7 ;
                    while (n >=7) and (n <= 9) do
                        begin
                            with 
                                n:integer; 
                            do 
                                begin
                                    n:=9;
                                    begin 
                                        putint(n); 
                                        n:=n+1; 
                                    end
                                end 
                            n:= n+ 1;
                        end
                end
        """
		expect = """999"""
        
		self.assertTrue(TestCodeGen.test(input,expect,598))  
    
    
	def test_complex_11(self):
        
		input = """
            function foo(a,b:real ; c:boolean):real;
                Begin
                    if c then
                        return (A - b);
                    else 
                        return a+B;
                end
            procedure main();
                Begin
                    putFloatLn(foo(1+1, 1.0+0.1, true));
                    putFloat(foo(1+1, 1.0+0.1, not true));
                    return;
                end
        """
        
		expect = """0.9\n3.1"""
        
		self.assertTrue(TestCodeGen.test(input, expect, 599))      

    
	def test_complex_12(self):
        
		input = """
            FUNCTION checkPositive(i:integer) : Boolean;
            begin
                if i >= 0 then
                begin
                    putInt(i);
                    putString("  : pos ");
                    return true;
                end
                putInt(i);
                putString(" : neg ");
                return false;
            end

            procedure main();
            begin
                putBoolLn(checkPositive(1));
                putBoolLn(checkPositive(2));
                putBoolLn(checkPositive(3));
                putBoolLn(checkPositive(-3));
                putBoolLn(checkPositive(-2));
                putBoolLn(checkPositive(0));
            end
        """
        
		expect = "1  : pos true\n2  : pos true\n3  : pos true\n-3 : neg false\n-2 : neg false\n0  : pos true\n"
        
		self.assertTrue(TestCodeGen.test(input, expect, 600))    

    
    
	def test_final(self):
        
		input = """
            var i : integer;
            procedure foo();
            begin
                i := 0;
                putInt(i);
                with i:integer; do
                    with f,i:real; do
                        with i:boolean; do
                        begin
                            i := 1 > -5;
                            putBool(i);
                        end
            end

            procedure main();
            var i : integer;
            begin
                i := -1;
                putInt(i);
                foo();
                putInt(i);
            end
        """
        
		expect = "-10true-1"
        
		self.assertTrue(TestCodeGen.test(input,expect,601))      
	
    	
		