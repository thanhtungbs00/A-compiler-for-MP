import unittest
from TestUtils import TestChecker
from AST import *
from StaticCheck import *
from StaticError import *

class CheckerSuite(unittest.TestCase):
    
    def test_simple_var_decl(self):
        input = Program([
                VarDecl(Id('a'),FloatType()),
                VarDecl(Id('a'),IntType()),
                FuncDecl(Id("main"),[],[],[])])

        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,401))
    
    def test_simple(self):
        input = Program([
                VarDecl(Id('main'),FloatType()),
                VarDecl(Id('b'),IntType()),
                FuncDecl(Id("main"),[],[],[])])

        expect = "Redeclared Procedure: main"
                
        self.assertTrue(TestChecker.test(input,expect,402))

    def test_simple_func_return_int(self):
        input = """function main():integer;
                begin
                end"""
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input,expect,403))

    def test_question_procedure(self):
        input = Program([
                VarDecl(Id('a'),FloatType()),
                FuncDecl(Id("main"),[],[],[]),
                VarDecl(Id('a'),IntType())])

        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,404))

    def test_simple_program111(self):
        input = Program([
                VarDecl(Id('a'),IntType()),
                FuncDecl(Id("a"),[],[],[]),
                VarDecl(Id('b'),FloatType())])

        expect = "No entry point"
        self.assertTrue(TestChecker.test(input,expect,405))
    
    def test_noerror_function(self):
        input = Program([
                VarDecl(Id('a'), IntType()),
                VarDecl(Id('foo'), FloatType()),
                FuncDecl(Id('foo'),[VarDecl(Id('a'), IntType()), VarDecl(Id('b'), FloatType())],[],[],IntType()),
                FuncDecl(Id("main"),[],[],[])])

        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,406))

    def test_redec_global(self):
        input = Program([
                VarDecl(Id('a'), IntType()),
                FuncDecl(Id('foo'),[VarDecl(Id('a'), IntType()), VarDecl(Id('b'), FloatType())],[],[],IntType()),
                VarDecl(Id('a'), FloatType()),
                FuncDecl(Id("main"),[],[],[])])

        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,407))

    def test_var_fuc_checkredecl_in_body(self):
        input = Program([
                VarDecl(Id('a'), IntType()),
                FuncDecl(Id("main"),[],[],
                    [
                        CallStmt(Id("foo"),[IntLiteral(1)])
                    ]),
                ])

        expect = "Undeclared Procedure: foo"
        self.assertTrue(TestChecker.test(input,expect,408))

    def test_callrandom__fuc_checkredecl(self):
        input = Program([
                VarDecl(Id('a'), IntType()),
                FuncDecl(Id("main"),[],[],
                    [
                        CallStmt(Id("foo"),[IntLiteral(1)])
                    ]),
                FuncDecl(Id('aa'),[VarDecl(Id('a'), IntType())],[],[],IntType()),
                ])

        expect = "Undeclared Procedure: foo"
        self.assertTrue(TestChecker.test(input,expect,409))

    def test_Redeclared_Variable_1(self):
        input = Program([
                VarDecl(Id('a'), IntType()),
                FuncDecl(Id("main"),[],[],
                    [
                        CallStmt(Id("foo"),[IntLiteral(1)])
                    ]),
                FuncDecl(Id('foo'),[VarDecl(Id('a'), IntType())],[],[],IntType()),
                VarDecl(Id('a'), FloatType()),
                ])

        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,410))

    def test_Redeclared_Procedure_1(self):
        input = Program([
                VarDecl(Id('a'), IntType()),
                FuncDecl(Id("main"),[],[],
                    [
                        CallStmt(Id("foo"),[IntLiteral(1)])
                    ]),
                FuncDecl(Id('foo'),[VarDecl(Id('a'), IntType())],[],[],IntType()),
                VarDecl(Id('b'), FloatType()),
                FuncDecl(Id("main"),[],[],[]),
                ])

        expect = "Redeclared Procedure: main"
        self.assertTrue(TestChecker.test(input,expect,411))
    
    def test_Redeclared_function_1(self):
        input = Program([
                VarDecl(Id('a'), IntType()),
                FuncDecl(Id("main"),[],[],[CallStmt(Id("foo"),[IntLiteral(1)])],IntType()),
                FuncDecl(Id('main'),[VarDecl(Id('a'), IntType())],[],[],IntType()),
                VarDecl(Id('b'), FloatType()),
                FuncDecl(Id("main"),[],[],[]),
                ])

        expect = "Redeclared Function: main"
        self.assertTrue(TestChecker.test(input,expect,412))

    def test_redeclare_diff_type__var(self):
        input = Program([
                VarDecl(Id('a'), IntType()),
                FuncDecl(Id("main"),[],[],
                    [
                        CallStmt(Id("foo"),[IntLiteral(1)])
                    ]),
                FuncDecl(Id('foo'),[VarDecl(Id('a'), IntType())],[],[],IntType()),
                VarDecl(Id('b'), FloatType()),
                FuncDecl(Id("a"),[],[],[])
                ])

        expect = "Redeclared Procedure: a"
        self.assertTrue(TestChecker.test(input,expect,413))

    def test_redeclare_diff_type__func(self):
        input = Program([
                VarDecl(Id('a'), IntType()),
                FuncDecl(Id("main"),[],[],
                    [
                        CallStmt(Id("foo"),[IntLiteral(1)])
                    ]),
                FuncDecl(Id('foo'),[VarDecl(Id('a'), IntType())],[],[],IntType()),
                VarDecl(Id('main'), FloatType())
                ])

        expect = "Redeclared Variable: main"
        self.assertTrue(TestChecker.test(input,expect,414))

    def test_redeclare_in_param(self):
        input = Program([
                VarDecl(Id('i'),IntType()),
                FuncDecl(Id("f"),[VarDecl(Id('a'), IntType()),VarDecl(Id('a'), FloatType())],[],[],IntType()),
                FuncDecl(Id("foo"),[],[VarDecl(Id("main"),IntType())],[]),
                VarDecl(Id('g'),FloatType()),
                FuncDecl(Id("main"),[],[],[]),
                ])

        expect = "Redeclared Parameter: a"
        self.assertTrue(TestChecker.test(input,expect,415))

    def test_redeclare_in_param_pass(self):
        input = Program([
                VarDecl(Id('i'),IntType()),
                FuncDecl(Id("f"),[VarDecl(Id('a'), IntType()),VarDecl(Id('b'), FloatType())],[],[],IntType()),
                FuncDecl(Id("foo"),[],[VarDecl(Id("main"),IntType())],[]),
                VarDecl(Id('foo'),FloatType()),
                FuncDecl(Id("main"),[],[],[]),
                ])

        expect = "Redeclared Variable: foo"
        self.assertTrue(TestChecker.test(input,expect,416))
    
    def test_redeclare_in_local(self):
        input = Program([
                VarDecl(Id('i'),IntType()),
                FuncDecl(Id("f"),
                    [VarDecl(Id('a'), IntType()),VarDecl(Id('b'), FloatType())],
                    [VarDecl(Id('c'), IntType()),VarDecl(Id('c'), IntType())],
                    [],
                    IntType()),
                FuncDecl(Id("foo"),[],[VarDecl(Id("main"),IntType())],[]),
                VarDecl(Id('g'),FloatType()),
                FuncDecl(Id("main"),[],[],[]),
                ])

        expect = "Redeclared Variable: c"
        self.assertTrue(TestChecker.test(input,expect,417))

    def test_redeclare_in_local_and_param(self):
        input = Program([
                VarDecl(Id('i'),IntType()),
                FuncDecl(Id("f"),
                    [VarDecl(Id('a'), IntType()),VarDecl(Id('b'), FloatType())],
                    [VarDecl(Id('b'), IntType()),VarDecl(Id('c'), IntType())],
                    [],
                    IntType()),
                FuncDecl(Id("main"),[],[VarDecl(Id("main"),VoidType())],[]),
                VarDecl(Id('g'),FloatType())
                ])

        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input,expect,418))
    
    def test_redeclare_in_local_and_param_pass(self):
        input = Program([
                VarDecl(Id('i'),IntType()),
                FuncDecl(Id("f"),
                    [VarDecl(Id('a'), IntType()),VarDecl(Id('b'), FloatType())],
                    [VarDecl(Id('a'), IntType())],
                    [],
                    IntType()),
                FuncDecl(Id("main"),[],[],[])
                ])

        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,419))
    
    def test_un_entry_point(self):
        input = Program([
                VarDecl(Id('i'),IntType()),
                VarDecl(Id('g'),FloatType())
                ])

        expect = "No entry point"
        self.assertTrue(TestChecker.test(input,expect,420))

    def test_un_entry_point_priority(self):
        input = Program([
                VarDecl(Id('i'),IntType()),
                FuncDecl(Id("foo"),
                    [VarDecl(Id("a"),IntType())],
                    [VarDecl(Id("a"),IntType())],
                    []),
                VarDecl(Id('g'),FloatType())
                ])

        expect = "No entry point"
        self.assertTrue(TestChecker.test(input,expect,421))

    def test_un_entry_point_priority_fun(self):
        input = Program([
                VarDecl(Id('i'),IntType()),
                FuncDecl(Id("a"),
                    [VarDecl(Id("i"),IntType())],
                    [VarDecl(Id("a"),IntType())],
                    []),
                VarDecl(Id('g'),FloatType())
                ])

        expect = "No entry point"
        self.assertTrue(TestChecker.test(input,expect,422))
    
    def test_undefine(self):
        input = """
            var b:integer;
            procedure main();
            var c:integer;
            begin 
                foo(foo);
            end
            procedure foo();begin end
            """
        expect = "Undeclared Identifier: foo"
        self.assertTrue(TestChecker.test(input,expect,423))

    def test_mis_type_assign_array(self):
        input = """
            procedure main();
            var a: array [0 .. 15] of integer;
            begin
                a:= 5;
            end
            """

        expect = "Type Mismatch In Statement: AssignStmt(Id(a),IntLiteral(5))"
        self.assertTrue(TestChecker.test(input,expect,424))

    def test_mis_type_assign_string(self):
        input = """
            procedure main();
            var a: string;
            begin
                a:= 5;
            end
            """

        expect = "Type Mismatch In Statement: AssignStmt(Id(a),IntLiteral(5))"
        self.assertTrue(TestChecker.test(input,expect,425))

    def test_mis_type_assign_real_int(self):
        input = """
            procedure main();
            var a: real;
                b: integer;
            begin
                a:= b:= a;
            end
            """

        expect = "Type Mismatch In Statement: AssignStmt(Id(b),Id(a))"
        self.assertTrue(TestChecker.test(input,expect,426))
    
    def test_boolean_condition_if(self):
        input = """
            procedure main();
            var a: boolean;
                b: integer;
            begin
                if(b) then  b := 1; 
            end
            """

        expect = "Type Mismatch In Statement: If(Id(b),[AssignStmt(Id(b),IntLiteral(1))],[])"
        self.assertTrue(TestChecker.test(input,expect,427))
    
    def test_indexx_in_array_cell(self):
        input = """
            procedure main();
            var a: array[1 .. 2] of integer;
                b: real;
            begin
                a[b] := 5;
            end
            """

        expect = "Type Mismatch In Expression: ArrayCell(Id(a),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,428))
    
    def test_type_ele_in_array_cell(self):
        input = """
            procedure main();
            var a: array[1 .. 2] of integer;
                b: real;
            begin
                a[5] := 5.5;
            end
            """

        expect = "Type Mismatch In Statement: AssignStmt(ArrayCell(Id(a),IntLiteral(5)),FloatLiteral(5.5))"
        self.assertTrue(TestChecker.test(input,expect,429))

    def test_type_in_array_cell(self):
        input = """
            procedure main();
            var a: array[1 .. 2] of integer;
                b: real;
            begin
                b := a[5] := b;
            end
            """

        expect = "Type Mismatch In Statement: AssignStmt(ArrayCell(Id(a),IntLiteral(5)),Id(b))"
        self.assertTrue(TestChecker.test(input,expect,430))

    def test_type_assign_boolean(self):
        input = """
            procedure main();
            var a: array[1 .. 2] of integer;
                b: boolean;
            begin
                b := foo();
            end
            function foo():integer;begin end
            """

        expect = "Type Mismatch In Statement: AssignStmt(Id(b),CallExpr(Id(foo),[]))"
        self.assertTrue(TestChecker.test(input,expect,431))
    
    def test_miss_param_call_expr(self):
        input = """
            procedure main();
            var a: array[1 .. 2] of integer;
                b: real;
            begin
                b := foo(5);
            end
            function foo(a:integer;b:integer):integer;begin end
            """

        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[IntLiteral(5)])"
        self.assertTrue(TestChecker.test(input,expect,432))

    def test_misstake_para_type(self):
        input = """
            procedure main();
            var a: array[1 .. 2] of integer;
                b: real;
            begin
                b := foo(5,6.5);
            end
            function foo(a:real;b:integer):integer;begin end
            """

        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[IntLiteral(5),FloatLiteral(6.5)])"
        self.assertTrue(TestChecker.test(input,expect,433))
    
    def test_type_miss_ifstmt_1(self):
        input = """ procedure main();
                        begin
                            if (a+b) then 
                                begin
                                end
                        end
                    var a:real;
                    var b:integer;
                    """
        expect = "Type Mismatch In Statement: If(BinaryOp(+,Id(a),Id(b)),[],[])"
        self.assertTrue(TestChecker.test(input,expect,434))
    
    def test_type_miss_if_3(self):
        input = """procedure main();
                        begin
                            if a>b then
                            if b>c then
                            if x and y or z or t then
                            if not x then
                            if a + b then
                                a:=b;
                        end
                        var a,b,c:integer;
                        var x,z,y,t:boolean; """
        expect = "Type Mismatch In Statement: If(BinaryOp(+,Id(a),Id(b)),[AssignStmt(Id(a),Id(b))],[])"
        self.assertTrue(TestChecker.test(input,expect,435))

    def test_____(self):
        input = """procedure main();
                        var i:integer;
                        begin
                            if i>5 then
                            if i>3 then
                            if i>7 then
                                begin
                                for i:=5 to 10 do
                                    if i=3 then
                                    begin
                                        
                                        i:=2;
                                    end
                                continue;
                                end
                            with a:integer; do
                            begin
                                
                            end
                        end
                        var a,b,c,d,i:integer; """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,436))

    def test__break__(self):
        input = """procedure main();
                        var i:integer;
                        begin
                            if i>5 then
                            if i>3 then
                            if i>7 then
                                begin
                                for i:=5 to 10 do
                                    if i=3 then
                                    begin
                                        
                                        i:=2;
                                    end
                                
                                end
                            with a:integer; do
                            begin
                                break;
                            end
                        end
                        var a,b,c,d,i:integer; """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,437))
   
    def test_case_sentitive(self):
        input = """
        Procedure foo(numbers : Array[1 .. 100] of Integer; size : Integer);
        Var
            i, j, temp : Integer;
        Begin End
        procedure main();begin end
        Var j : Boolean;
        Var Main : Integer;
        """
        expect = "Redeclared Variable: Main"
        self.assertTrue(TestChecker.test(input,expect,438))

    def test_break(self):
        input = """
        Procedure FoO(numbers : Array[1 .. 100] of Integer; size : Integer);
        Var
            i, j, temp : Integer;
        Begin
            For i := size-1 DownTo 1 do
                For j := 2 to i do
                    If (numbers[j-1] > numbers[j]) Then
                    Begin
                        temp := numbers[j-1];
                        numbers[j-1] := numbers[j];
                        numbers[j] := temp;
                        break;
                    End
            break;
        End
        procedure main();begin end
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,439))

    def test_miss_statement(self):
        """Simple program: int main() {} """
        input = Program([VarDecl(Id("c"),BoolType()),VarDecl(Id("b"),IntType()),
                        FuncDecl(Id("main"),
                        [],[VarDecl(Id("a"),BoolType())],
                        [

                            If(Id("a"),[Assign(Id("a"),BooleanLiteral(True))],[Assign(Id("c"),BooleanLiteral(False))]),
                            If(Id("b"),
                            [
                                Assign(Id("c"),BooleanLiteral(True)),Assign(Id("a"),BooleanLiteral(False))
                            ],
                            [
                                Assign(Id("c"),BooleanLiteral(False))
                            ])
                        ],VoidType())])
        expect = "Type Mismatch In Statement: If(Id(b),[AssignStmt(Id(c),BooleanLiteral(True)),AssignStmt(Id(a),BooleanLiteral(False))],[AssignStmt(Id(c),BooleanLiteral(False))])"
        self.assertTrue(TestChecker.test(input,expect,440))
    
    def test_param_arraytype(self):
        input = """Procedure foo(numbers : Array[1 .. 100] of Integer; size : Integer);
                    Var i:integer;
                    Begin
	                    For i := 2 to size-1 do
	                    Begin
		                    i := 5;
		                    While ((i > 1) AND (5 > size)) do
		                    Begin
			                    numbers[i] := numbers[i-1];
			                    i := i - 1;
		                    End
	                    End
                    End
                    procedure main();
                    var a:Array[2 .. 5] of integer;
                    begin
                        foo(a,5);
                    end
                """

        expect = "Type Mismatch In Statement: CallStmt(Id(foo),[Id(a),IntLiteral(5)])"
        self.assertTrue(TestChecker.test(input,expect,441))
    
    def test_misstake_para_type1(self):
        input = """
            procedure main();
            var a: array[1 .. 2] of integer;
                b: real;
            begin
                b := foo(5.5,5,6);
            end
            function foo(a:integer;b:integer;c:real):integer;begin end
            """

        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[FloatLiteral(5.5),IntLiteral(5),IntLiteral(6)])"
        self.assertTrue(TestChecker.test(input,expect,442))

    def test_misstake_para_type3(self):
        input = """
            procedure main();
            var a: array[1 .. 2] of integer;
                b: real;
            begin
                b := foo(55,5,6);
            end
            procedure foo(a:integer;b:integer;c:real);begin end
            """

        expect = "Undeclared Function: foo"
        self.assertTrue(TestChecker.test(input,expect,443))

    def test_call_stmt1(self):
        input = """
            procedure main();
            var a: array[1 .. 2] of integer;
                b: real;
            begin
                foo(55,5,6);
            end
            function foo(a:integer;b:integer;c:real):integer;begin end
            """

        expect = "Undeclared Procedure: foo"
        self.assertTrue(TestChecker.test(input,expect,444))
    
    def test_call_stmt2(self):
        input = """
            procedure main();
            var a: array[1 .. 2] of integer;
                b: real;
            begin
                foo(55,5.5,6);
            end
            procedure foo(a:integer;b:integer;c:real);begin end
            """

        expect = "Type Mismatch In Statement: CallStmt(Id(foo),[IntLiteral(55),FloatLiteral(5.5),IntLiteral(6)])"
        self.assertTrue(TestChecker.test(input,expect,445))
    
    def test_rhs_is_array(self):
        input = """
            var a: array[1 .. 5] of integer;

            function foo(a: array[1 .. 5] of integer): integer;
            begin
                return 5;
            end

            procedure main(); 
            var x: integer;
            begin
                x := foo(a);
                x := a[1];
                x := a;
                return;
            end
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(x),Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 446))
    
    def test_break_not_inloop__andtype_binaryop(self):
        input = """
        function foo(index: Integer): Integer; 
        var c1:integer;
            c2:real;
        begin
            while c2 > c1 do
            begin
                for index := 1 to 10 do
                    continue;
                while index < 10 do
                    continue;
                if index > 1 then break;
                continue;
            end
            break;
            return 10;
        end
        Var a :Integer;
        procedure main();
        begin
            a := a + foo(a);
        end
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,447))
    
    def test_miss_param(self):
        input = Program([
                FuncDecl(Id("main"),[],[],
                    [
                        CallStmt(Id("putLn"),[IntLiteral(1)])
                    ])
                ])

        expect = "Type Mismatch In Statement: CallStmt(Id(putLn),[IntLiteral(1)])"
        self.assertTrue(TestChecker.test(input,expect,448))
    
    def test_diff_type_of_param_float(self):
        input = Program([
                FuncDecl(Id("main"),[],[],
                    [
                        CallStmt(Id("putIntLn"),[IntLiteral(1)]),
                        CallStmt(Id("putIntLn"), [FloatLiteral(1.4)])
                    ])
                ])

        expect = "Type Mismatch In Statement: CallStmt(Id(putIntLn),[FloatLiteral(1.4)])"
        self.assertTrue(TestChecker.test(input,expect,449))

    def test_call_stmt_undec_id(self):
        input = Program([
                FuncDecl(Id("main"),[],[],
                    [
                        CallStmt(Id("putLn"),[Id("a")]),
                        CallStmt(Id("putIntLn"),[IntLiteral(1)]),
                        CallStmt(Id("putIntLn"), [FloatLiteral(1.4)])
                    ])
                ])

        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input,expect,450))
    
    def test_param_arraytype(self):
        input = """Procedure foo(numbers : Array[1 .. 100] of Integer; size : Integer);
                    Var i:integer;
                    Begin
	                    For i := 2 to size-1 do
	                    Begin
		                    i := 5;
		                    While ((i > 1) AND (5 > size)) do
		                    Begin
			                    numbers[i] := numbers[i-1];
			                    i := i - 1;
		                    End
	                    End
                    End
                    procedure main();
                    var a:Array[2 .. 5] of integer;
                    begin
                        foo(a,5);
                    end
                """

        expect = "Type Mismatch In Statement: CallStmt(Id(foo),[Id(a),IntLiteral(5)])"
        self.assertTrue(TestChecker.test(input,expect,451))
    
    def test_function_return_array(self):
        input = """
            var a: array[1 .. 5] of integer;

            function foo(a:real):  array[1 .. 5] of integer;
            begin
                return 5;
            end

            procedure main(); 
            var x: integer;
            begin
                x := foo(a);
                x := a[1];
                return;
            end
        """
        expect = "Type Mismatch In Statement: Return(Some(IntLiteral(5)))"
        self.assertTrue(TestChecker.test(input, expect, 452))
    
    def test_function_return_array1(self):
        input = """
            var a: array[1 .. 5] of integer;

            function foo(b:real):  array[1 .. 5] of integer;
            begin
                return a;
            end

            procedure main(); 
            var x: integer;
            begin
                x := a[1];
                return 1;
            end
        """
        expect = "Type Mismatch In Statement: Return(Some(IntLiteral(1)))"
        self.assertTrue(TestChecker.test(input, expect, 453))
    
    def test_function_return_array2(self):
        input = """
            var a: array[1 .. 5] of integer;

            function foo(b:real):  array[1 .. 5] of integer;
            begin
                return ;
            end

            procedure main(); 
            var x: integer;
            begin
                x := a[1];
                return ;
            end
        """
        expect = "Type Mismatch In Statement: Return(None)"
        self.assertTrue(TestChecker.test(input, expect, 454))
    
    def test___1(self):
        input = """var b,c,a : integer ;
                    var a: integer;

                    procedure main(); begin
	                    return;
                    end
                """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,455))
    
    def test___2(self):
        input = """
                var  a,b,c:integer;
                var d,b:integer;
                procedure main(); begin
                    return;
                end
                """
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input,expect,456))
    
    def test___3(self):
        input = """
                var a, b:integer;
                var d: real;
                procedure m(); var n:integer; begin end 
                procedure n(); var c:integer; begin end
                function  c(a,b:integer):real; begin return 1.0; end
                procedure d(); begin end
                procedure main(); begin 
                    m();n();c(1,2);d();
                    return ;
                end
                """
        expect = "Redeclared Procedure: d"
        self.assertTrue(TestChecker.test(input,expect,457))

    def test___4(self):
        input = """
                var c: integer;
                var  d:real;
                var  e:boolean;
                function foo(b, a : integer;  m:array[1 .. 3] of integer):integer; begin 
                    
                    with a: array[1 .. 5] of integer; do begin 
                        
                    end
                    return 0;
                end
                function foo1(b, c:integer; m:array [1 .. 3] of integer):integer; 
                var c:array[1 .. 5] of integer;
                begin 

                    return 0;
                end
                procedure main(); var a:array[1 .. 3] of integer;begin  

                a[3] := foo(1,foo1(1,2,a),a);
                return ;
                end
                """
        expect = "Redeclared Variable: c"
        self.assertTrue(TestChecker.test(input,expect,458))

    def test___5(self):
        input = """
                var a:integer;
                procedure funcA();
                var b:integer; 
                begin 
                    
                    a := 7;
                    b := a;
                end
                function sum(b:integer):integer; 
                var d:integer;
                begin 
                    
                    d := 7;
                    return a + b + d;
                end
                procedure main(); 
                var m:array[1 .. 10] of integer;
                begin 

                    m[1] := sum(3);
                    funcA();
                    a := 1 + n[1];
                    return ;
                end
                """
        expect = "Undeclared Identifier: n"
        self.assertTrue(TestChecker.test(input,expect,459))

    def test___6(self):
        input = """
                var a:integer;
                function foo(a, b:integer):integer; 
                begin 
                    if (a > b) then a := 1 + b;
                    else a := b + 2;
                    return a;
                end
                function foo1(a:integer):integer;
                var b, c, d:integer;
                begin 
                    b := 2;
                    c := 3;
                    if (a > b) then d := a + c;
                    else d := b + foo2(1);
                    return d;
                end
                var b:integer;
                function foo2(a:integer):integer;
                begin 
                    while (a > 5) do a := a + 1;
                    
                    return a;
                end
                procedure main(); begin 
                    a := foo(foo1(1),foo2(2));
                    funy(4);
                    return ;
                end
                """
        expect = "Undeclared Procedure: funy"
        self.assertTrue(TestChecker.test(input,expect,460))

    def test___7(self):
        input = """
                var a, b, c:integer;
                var d:boolean;
                var e:real;
                var m: array [1 .. 100] of integer;
                function foo():integer; begin  return 0; end
                procedure main(); begin 
                    b := foo();
                    d := true;
                    a := m[0] + 1;
                    c := m[d] + 1;
                    return ;
                end
                """
        expect = "Type Mismatch In Expression: ArrayCell(Id(m),Id(d))"
        self.assertTrue(TestChecker.test(input,expect,461))

    def test___8(self):
        input = """
                var a, b, c:integer;
                procedure main(); var  d:boolean; begin 
                    
                    d := (a > b) and true;
                    d := (a > b) and 1.0;
                    return ;
                end
                """
        expect = "Type Mismatch In Expression: BinaryOp(and,BinaryOp(>,Id(a),Id(b)),FloatLiteral(1.0))"
        self.assertTrue(TestChecker.test(input,expect,462))

    def test___9(self):
        input = """
                var a, b, c:integer;
                procedure foo(); begin 
                    while (a < 100) do begin
                        a := a + 1;
                        break;
                    end
                    return ;
                end
                procedure main(); begin 
                    while (a < 100) do begin
                        a := a + 1;
                        break;
                    end
                        foo();
                    if(a = 100) then break;
                    return ;
                end
                """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,463))

    def test___10(self):
        input = """
                function foo():integer;
                var a:integer;
                begin  
                    a := 4;
                    if (a = 10) then begin 
                        return 1; 
                    end
                    return 10;
                end

                procedure main(); 
                var a:integer;
                begin 
                    a := 0;
                
                    if (foo() > 1) then begin 
                        if(foo2() <= 100) then

                            return ; 
                        else
                            return ;  
                    end 
                    else begin 
                        a := 2;
                        return ;
                    end
                end
                """
        expect = "Undeclared Function: foo2"
        self.assertTrue(TestChecker.test(input,expect,464))
    
    def test___11(self):
        input = """
                procedure main();
                var  a, i, j:integer; 
                begin 
                        
                    for i := 1 to 10 do begin 
                        j := 2;
                    end	
                    for a := 0 to  5 = 3 do begin 
                        j := 1;
                    end
                    return ;
                end
                """
        expect = "Type Mismatch In Statement: For(Id(a),IntLiteral(0),BinaryOp(=,IntLiteral(5),IntLiteral(3)),True,[AssignStmt(Id(j),IntLiteral(1))])"
        self.assertTrue(TestChecker.test(input,expect,465))
    
    def test___12(self):
        input = """
                function foo():integer; begin  return 1; end
                function foo1():integer; begin  return 1.0; end
                procedure main(); begin 
                foo();
                foo1();
                return ;
                end
                """
        expect = "Type Mismatch In Statement: Return(Some(FloatLiteral(1.0)))"
        self.assertTrue(TestChecker.test(input,expect,466))

    def test___13(self):
        input = """
                function foo():boolean; begin  return 2 > 1; end
                function foo1(a:integer):boolean; begin  return a = 1; end
                function foo2(a:integer):boolean; begin  return a; end
                procedure main(); begin 
                foo();
                foo1(1);
                foo2(2);
                return ;
                end
                """
        expect = "Type Mismatch In Statement: Return(Some(Id(a)))"
        self.assertTrue(TestChecker.test(input,expect,467))
    
    def test___14(self):
        input = """
                var a:integer;
                var m:array[1 .. 100] of real;
                procedure foo(); begin 
                    a := - -(a - -1);
                end
                procedure main(); begin 
                        foo();
                    a := -(m[1] + -1 > 1.2);
                    return ;
                end
                """
        expect = "Type Mismatch In Expression: UnaryOp(-,BinaryOp(>,BinaryOp(+,ArrayCell(Id(m),IntLiteral(1)),UnaryOp(-,IntLiteral(1))),FloatLiteral(1.2)))"
        self.assertTrue(TestChecker.test(input,expect,468))

    def test___15(self):
        input = """
                var a:integer;
                var b:real;
                var m:array[1 .. 10] of integer;
                procedure main(); begin 
                    b := m[1] + -1;
                    b := b * (1.0 + 1);
                    b := not (m[1] = 1);
                    return ;
                end
                """
        expect = "Type Mismatch In Statement: AssignStmt(Id(b),UnaryOp(not,BinaryOp(=,ArrayCell(Id(m),IntLiteral(1)),IntLiteral(1))))"
        self.assertTrue(TestChecker.test(input,expect,469))

    def test_string_binary(self):
        input = """
                var a:integer;
                var b:real;
                var m:array[1 .. 10] of integer;
                var c:boolean;
                var q :string;
                procedure main(); begin 
                    a := q +1;
                    b := m[1] + -1;
                    b := b * (1.0 + 1);
                    c := not (m[1] = 1);
                    return ;
                end
                """
        expect = "Type Mismatch In Expression: BinaryOp(+,Id(q),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,470))
    
    def test_string_unary(self):
        input = """
                var a:integer;
                var b:real;
                var m:array[1 .. 10] of integer;
                var c:boolean;
                var q :string;
                procedure main(); begin 
                    a := -m +1;
                    b := m[1] + -1;
                    b := b * (1.0 + 1);
                    c := not (m[1] = 1);
                    return ;
                end
                """
        expect = "Type Mismatch In Expression: UnaryOp(-,Id(m))"
        self.assertTrue(TestChecker.test(input,expect,471))

    def test_binary__1(self):
        input = """
                var a:integer;
                var b:real;
                var m:array[1 .. 10] of integer;
                var c:boolean;
                var q :string;
                procedure main(); begin 
                    a := b div 1;
                    b := m[1] + -1;
                    b := b * (1.0 + 1);
                    c := not (m[1] = 1);
                    return ;
                end
                """
        expect = "Type Mismatch In Expression: BinaryOp(div,Id(b),IntLiteral(1))"
        self.assertTrue(TestChecker.test(input,expect,472))

    def test_binary__2(self):
        input = """
                var a:integer;
                var b:real;
                var m:array[1 .. 10] of integer;
                var c:boolean;
                var q :string;
                procedure main(); begin 
                    a := c + c;
                    b := m[1] + -1;
                    b := b * (1.0 + 1);
                    c := not (m[1] = 1);
                    return ;
                end
                """
        expect = "Type Mismatch In Expression: BinaryOp(+,Id(c),Id(c))"
        self.assertTrue(TestChecker.test(input,expect,473))

    def test_indexExpr_11(self):
        input = """ procedure foo(m: real; n: boolean);
                    var B, k: integer; arrReal : array [1 ..10] of real; arrInt : array [1 .. 5] of integer; r: real;
                    begin
                        arrReal[arrInt[b]] := b/k;
                    end
                    procedure maiN();
                    var a : integer; b: real; c: boolean;
                    begin
                        if true then b:= b /5;
                        for a:= 5 to 10 do
                        begin
                            if (a>5) and false then break;
                            else continue;
                        end
                        with a, b: real;
                        do continue;
                    end
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,474))
    
    #########################################

    
    
    def test_function_not_return_1(self):
        input = """
                var a: real;
                procedure main();
                begin
                end

                function foo(a:integer):integer;
                begin 
                if false then return 4;
                else return 3;
                end

                function bar(a:integer):integer;
                begin 
                if false then return 4;
                end
            """
        expect = "Function bar Not Return"
        self.assertTrue(TestChecker.test(input, expect, 475))
    
    def test_function_not_return_2(self):
        input = """
                var a: real;
                procedure main();
                begin
                end

                function foo(a:integer):integer;
                begin 
                if false then begin end
                else return 3;
                end

                function bar(a:integer):integer;
                begin 
                return 4;
                end
            """
        expect = "Function foo Not Return"
        self.assertTrue(TestChecker.test(input, expect, 476))

    def test_function_not_return_3(self):
        input = """
                var a: real;
                procedure main();
                begin
                end

                function foo(a:integer):integer;
                begin 
                if false then begin end
                else begin end
                end

                function bar(a:integer):integer;
                begin 
                return 4;
                end
            """
        expect = "Function foo Not Return"
        self.assertTrue(TestChecker.test(input, expect, 477))
    
    def test_function_not_return_4(self):
        input = """
                var a: real;
                procedure main();
                begin
                end

                function foo(a:integer):integer;
                begin 
                if false then 
                if true then
                if 1>2 then a:=1;
                else begin return 5; end
                end

                function bar(a:integer):integer;
                begin 
                return 4;
                end
            """
        expect = "Function foo Not Return"
        self.assertTrue(TestChecker.test(input, expect, 478))

    def test_function_not_return_5(self):
        input = """
                var a: real;
                procedure main();
                begin
                end

                function foo(a:integer):integer;
                begin 
                if false then 
                if true then return 4;
                else a:= 1;
                else return 5;
                end

                function bar(a:integer):integer;
                begin 
                return 4;
                end
            """
        expect = "Function foo Not Return"
        self.assertTrue(TestChecker.test(input, expect, 479))

    def test_function_not_return_4(self):
        input = """
                var a: real;
                procedure main();
                begin
                end

                function foo(a:integer):integer;
                begin 
                if false 
                    then 
                        if true 
                            then
                                if 1>2 
                                    then return 1;
                                else  return 5; 
                else 
                    if 5<2 
                        then 
                            return 5;
                    else
                        return 3;
                end

                function bar(a:integer):integer;
                begin 
                return 4;
                end
            """
        expect = "Function foo Not Return"
        self.assertTrue(TestChecker.test(input, expect, 480))

    def test_no_entry111(self):
        input = """
                var a:integer;
                procedure funcA();
                var b:integer; 
                begin 
                    a := 7;
                    b := a;
                end
                procedure main(a:integer); 
                var m:array[1 .. 10] of integer;
                begin 

                    m[1] := sum(3);
                    funcA();
                    a := 1 + n[1];
                    return ;
                end
                """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input,expect,481))
    
    def test_no_entry11221(self):
        input = """
                var a:integer;
                procedure funcA();
                var b:integer; 
                begin 
                    a := 7;
                    b := a;
                end
                function main():integer; 
                var m:array[1 .. 10] of integer;
                begin 

                    m[1] := sum(3);
                    funcA();
                    a := 1 + n[1];
                    return ;
                end
                """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input,expect,481))

    def test_redecleraaa(self):
        input = """
                var funca:integer;
                procedure funcA(funca:integer);
                var b:integer; 
                begin 
                    a := 7;
                    b := a;
                end
                procedure main(); 
                var m:array[1 .. 10] of integer;
                begin 
                end
                """
        expect = "Redeclared Procedure: funcA"
        self.assertTrue(TestChecker.test(input,expect,482))

    def test_undec(self):
        input = """
                var a:integer;
                procedure funcA(funca:integer);
                var b:integer; 
                begin 
                    aaa := 7;
                    b := a;
                end
                procedure main(); 
                var m:array[1 .. 10] of integer;
                begin 
                end
                """
        expect = "Undeclared Identifier: aaa"
        self.assertTrue(TestChecker.test(input,expect,483))
    
    def test_undecmis(self):
        input = """
                var a:integer;
                procedure funcA(funca:integer);
                var b:integer; 
                begin 
                    a := 7.5;
                    b := a;
                end
                procedure main(); 
                var m:array[1 .. 10] of integer;
                begin 
                end
                """
        expect = "Type Mismatch In Statement: AssignStmt(Id(a),FloatLiteral(7.5))"
        self.assertTrue(TestChecker.test(input,expect,484))

    def test_undec(self):
        input = """
                var a:string;
                procedure funcA(funca:integer);
                var b:integer; 
                begin 
                    a := 7.5;
                end
                procedure main(); 
                var m:array[1 .. 10] of integer;
                begin 
                end
                """
        expect = "Type Mismatch In Statement: AssignStmt(Id(a),FloatLiteral(7.5))"
        self.assertTrue(TestChecker.test(input,expect,485))

    
    def test_undzssssssec(self):
        input = """
                var a:string;
                procedure funcA(funca:integer);
                var b:integer; 
                begin 
                    //a := 7.5;
                end
                procedure main(); 
                var m:array[1 .. 10] of integer;
                begin 
                m := 5;
                end
                """
        expect = "Type Mismatch In Statement: AssignStmt(Id(m),IntLiteral(5))"
        self.assertTrue(TestChecker.test(input,expect,486))

    def test_unde_biaad1a123naryc(self):
        input = """
                var a:real;
                procedure funcA(funca:integer);
                var b:integer; 
                begin 
                    a := (7.5 + 5 /4 *9) + not(5.6>6+2);
                end
                procedure main(); 
                var m:array[1 .. 10] of integer;
                begin 
                
                end
                """
        expect = "Type Mismatch In Expression: BinaryOp(+,BinaryOp(+,FloatLiteral(7.5),BinaryOp(*,BinaryOp(/,IntLiteral(5),IntLiteral(4)),IntLiteral(9))),UnaryOp(not,BinaryOp(>,FloatLiteral(5.6),BinaryOp(+,IntLiteral(6),IntLiteral(2)))))"
        self.assertTrue(TestChecker.test(input,expect,487))

    def tes1112t_type_misssss_while_2(self):
        input = """ function foo(x:integer):array[1 .. 10] of boolean;
                                var a: array[1 .. 10] of boolean;
                                begin
                                        return a;
                                end
                                
                        procedure foo1(a:array[1 .. 10] of boolean);
                        begin
                                with x:integer; do
                                begin
                                        return;
                                end
                        end
                        
                        procedure main();
                        begin
                                foo1(foo(x));
                                while foo(x)[3] do 
                                begin
                                        while 1+2+3 do begin end
                                end
                        end
                        var x:integer;
                        var y:array[1 .. 10] of boolean;
                         """
        expect = "Type Mismatch In Statement: While(BinaryOp(+,BinaryOp(+,IntLiteral(1),IntLiteral(2)),IntLiteral(3)),[])"
        self.assertTrue(TestChecker.test(input,expect,488))

    def test_type_mis_asaaaaaasign_1(self):
        input = """ procedure main();
                            begin
                                a:=1;
                                b:=2;
                                c:=a+b;
                                d:=a+b+c;
                        end
                        var a,b,c:real;d:integer;"""
        expect = "Type Mismatch In Statement: AssignStmt(Id(d),BinaryOp(+,BinaryOp(+,Id(a),Id(b)),Id(c)))"
        self.assertTrue(TestChecker.test(input,expect,489))

    def test_type_mis_aaaassign_2(self):
        input = """procedure main();
                        begin
                                a:=1;
                                b:=2;
                                c:=foo(a);
                                d:= c + foo(c);
                        end
                        function foo(a:integer):real;
                        var x:real;
                        begin return x; end
                        var a,b,c,d:integer; """
        expect = "Type Mismatch In Statement: AssignStmt(Id(c),CallExpr(Id(foo),[Id(a)]))"
        self.assertTrue(TestChecker.test(input,expect,490))

    def test_ind22222exExpr_11(self):
        input = """ procedure maiN();
                    var a : integer; b: real; c: boolean;
                    begin
                        if true then b:= b /5;
                        else begin end
                        return ;
                    end
                function foo():integer;
                var a : integer;c: boolean;
                begin
                    
                    if true then a:= 5; else begin  end
                    if true then begin  end
                    
                end
                    
        """
        expect = "Function foo Not Return"
        self.assertTrue(TestChecker.test(input,expect,491))

    def test_misstakaaes_para_type2(self):
        input = """
            procedure main();
            var a: array[1 .. 2] of integer;
                b: real;
            begin
                b := foo(5.5,5);
            end
            function foo(a:integer;b:integer;c:real):integer;begin end
            """

        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[FloatLiteral(5.5),IntLiteral(5)])"
        self.assertTrue(TestChecker.test(input,expect,492))
    
    def test_no_eaaanwtry11221(self):
        input = """
                var a:integer;
                procedure funcA();
                var b:integer; 
                begin 
                    a := 7;
                    b := a;
                end
                function main():integer; 
                var m:array[1 .. 10] of integer;
                begin 

                    m[1] := sum(3);
                    funcA();
                    a := 1 + n[1];
                    return ;
                end
                """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input,expect,493))
    
    def test_break_not_inloop_30000(self):
        input = """
        function foo(index: Integer): Integer; 
        var c1:integer;
            c2:real;
        begin
            while c2 > c1 do
            begin
                for index := 1 to 10 do
                    continue;
                while index < 10 do
                    continue;
                if index > 1 then break;
                continue;
            end
            break;
            return 10;
        end
        Var a :Integer;
        procedure main();
        begin
            a := a + foo(a);
        end
        """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,494))

    def test_undeclare1111d_var_5(self):
        input = """
            var a: string;
            
            procedure foo(); 
            begin
            end

            function foo2(var1: string): array[0 .. 100] of integer;
            var a: array[0 .. 100] of integer;
            begin
                return a;
            end

            procedure main(); 
            var var1: real;
                var2: string;
            begin
                foo();
                foo2(var2)[0] := b;
            end
        """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input, expect, 495))

    def test_redeclared_builtInFunc_1(self):
        input = """
        procedure Main();
        begin
            PUtString();
        end
        procedure PUtString(); 
        var c1:integer;
            c2:real;
        begin
        end
        var FOO: Boolean;
        """
        expect = "Redeclared Procedure: PUtString"
        self.assertTrue(TestChecker.test(input,expect,496))

    def test_redeclared_local_var_1(self):
        input = """
        procedure main();
        var putLN: real;
            c2: integer;
            FOO: Boolean;
        begin
            PUtString123(FOO);
        end
        procedure PUtString123(c3: boolean); 
        var putLn: real;
            c2: string;
            c3:real;
        begin
        end
        var FOO: Boolean;
        """
        expect = "Redeclared Variable: c3"
        self.assertTrue(TestChecker.test(input,expect,497))

    def test_redeclared_with_1(self):
        input = """
        procedure main();
        var putLN: real;
            c2: integer;
            FOO: Boolean;
        begin
            PUtString123(FOO);
        end
        procedure PUtString123(c3: boolean); 
        var putLn: real;
            c2: string;
        begin
            WITH
                    c2 : string;
                    a: integer;
                    a: real;
                DO
                    begin
                        a := a + 1;
                        break;
                    end
        end
        var FOO: Boolean;
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input,expect,498))

    def test_redeclared_var3(self):
        """Unreachable FUnction\Procedure """
        input = """
        FUNCTION foo1():integer;
            BEGIN
                RETURN 10;
            END
        FUNCTION foo2():real;
            BEGIN
                RETURN foo2();
            END
        FUNCTION foo3():Boolean;
            BEGIN
                RETURN true;
            END
        PROCEDURE proc2();
            BEGIN
            END
        PROCEDURE main();
            VAR arr1 : ARRAY [1 .. 5] OF INTEGER;
                b : Integer;
                main : real;
            BEGIN
                WITH 
                    aWith :string;
                    b : integer;
                    aWith: real;
                DO
                    BEGIN
                        IF foo3() THEN
                            b := -arr1[foo1()];
                        else proc2();
                    END
            END
        """
        expect = "Redeclared Variable: aWith"
        self.assertTrue(TestChecker.test(input, expect, 499))

    def test_undeclared_var_1(self):
        input = """
        procedure main();
        begin
        end
        function foo(): Integer; 
        var c1:integer;
            c2:real;
        begin
            return c3;
        end
        var FOO3: Boolean;
        """
        expect = "Undeclared Identifier: c3"
        self.assertTrue(TestChecker.test(input,expect,500))

    def test_undeclared_proc_1(self):
        input = """
        procedure main();
        begin
        end
        function foo(): Integer; 
        var c1:integer;
            c2:real;
        begin
            foo();
            return 5;
        end
        var FOO3: Boolean;
        """
        expect = "Undeclared Procedure: foo"
        self.assertTrue(TestChecker.test(input,expect,501))

    def test_undeclared_func_1(self):
        input = """
        procedure main();
        begin
        end
        function foo():real; 
        var c1:integer;
            c2:real;
        begin
            c2 := c1 + foo();
            with  a: integer;
            do begin with  a:real; do begin  end end
            
        end
        var FOO3: Boolean;
        """
        expect = "Function foo Not Return"
        self.assertTrue(TestChecker.test(input,expect,502))
    
    def test_function_not_return(self):
        input = """
        procedure main();
        begin
        end
        function foo():integer; 
        var c1:integer;
            c:boolean;
        begin
            with a:integer; do 
                begin  
                if c then return 3;
                else  a:=1;
                
                
                end
            if c then c1:=2;
            else return 2;
            with a:integer; do 
                begin  
                if c then return 3;
                else  a:=1;
                
                end

        end
        var FOO3: Boolean;
        """
        expect = "Function foo Not Return"
        self.assertTrue(TestChecker.test(input,expect,503))