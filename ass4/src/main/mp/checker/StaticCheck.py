
"""
1613989- Cao Thanh Tung
"""
from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce


class MType:
    def __init__(self, partype, rettype):
        self.partype = partype
        self.rettype = rettype

    def __str__(self):
        return 'MPType([' + ','.join(str(i) for i in self.partype) + '],' + str(self.rettype) + ')'

class Symbol:
    def __init__(self, name, mtype, value=None):
        self.name = name
        self.mtype = mtype
        self.value = value

    def __str__(self):
        return 'Symbol(' + self.name + ','+str(self.mtype) + ')'

class StaticChecker(BaseVisitor, Utils):

    global_envi = [Symbol("getInt", MType([], IntType())),
                   Symbol("putInt", MType([IntType()], VoidType())),
                   Symbol("putIntLn", MType([IntType()], VoidType())),
                   Symbol("getFloat", MType([], IntType())),
                   Symbol("putFloat", MType([FloatType()], VoidType())),
                   Symbol("putFloatLn", MType([FloatType()], VoidType())),
                   Symbol("putBool", MType([BoolType()], VoidType())),
                   Symbol("putBoolLn", MType([BoolType()], VoidType())),
                   Symbol("putString", MType([StringType()], VoidType())),
                   Symbol("putStringLn", MType([StringType()], VoidType())),
                   Symbol("putLn", MType([], VoidType())),
                   ]

    def __init__(self, ast):
        self.ast = ast

    def checkRedeclared(self, sym, kind, env):
        # env : c
        # symbol : name - mtype
        # kind : Function - Procedure - Parameter - Variable - Identifier
        if self.lookup(sym.name.lower(), env, lambda x: x.name.lower()):
            raise Redeclared(kind, sym.name)
        else:
            return sym

    def checknoentrypoint(self,c):
        check = False
        for i in range(len(c)):
            if c[i].name.lower() == "main" and type(c[i].mtype) is MType:
                if (type(c[i].mtype.rettype) is VoidType) and c[i].mtype.partype == []:
                    check = True
        if check == False :
            raise NoEntryPoint

    def checkhaveif(self,lst,ast):
        #lst: list(ast)
        check = 0
        res = []
        for x in lst:
            if isinstance(x,If) and check == 0:
                res.append(x)
            if isinstance(x,Return):
                check = 1
        if check == 0:
            if res == []:
                raise FunctionNotReturn(ast.name.name) 
            else:
                a = False
                for x in res[::-1]:
                    a = self.visit(x,(a,ast))
                if a == False:
                    raise FunctionNotReturn(ast.name.name) 
        
        return True

    def check(self):
        return self.visit(self.ast, StaticChecker.global_envi)

    # AST
    # Program
    def visitProgram(self, ast, c):
        #add all symbol is declared inside the full program
        for item in ast.decl:
            if isinstance(item,VarDecl):
                c = c + [Symbol(item.variable.name, item.varType)]
            elif isinstance(item,FuncDecl):
                c = c + [Symbol(item.name.name, MType([i.varType for i in item.param], item.returnType))]
        #check no entry point   
        self.checknoentrypoint(c)
        #check redeclare
        for i in range(len(c)):
            for j in range(i+1,len(c)):
                if c[i].name.lower() == c[j].name.lower() :
                    if type(c[j].mtype) is MType :
                        kind = Procedure() if type(c[j].mtype.rettype) is VoidType else Function()
                        raise Redeclared(kind,c[j].name)
                    else:
                        kind = Variable()
                        raise Redeclared(kind,c[j].name)
        
        return [self.visit(x,c) for x in ast.decl]
       
    # Decl
    # FuncDecl - VarDecl 
    def visitFuncDecl(self, ast, c):
        #name: Id
        #param: list(VarDecl)
        #returnType: Type => VoidType for Procedure
        #local:list(VarDecl)
        #body: list(Stmt)
        kind = Procedure() if type(ast.returnType) is VoidType else Function()
        env = []
        #check redeclare in param and add to env of fundecl
        parameter = [Symbol(x.variable.name, x.varType) for x in ast.param]
        for x in parameter:
            env.append(self.checkRedeclared(x,Parameter(),env))
        #check redeclare in local and add to env of fundecl
        local = [Symbol(x.variable.name, x.varType) for x in ast.local] 
        for x in local:
            env.append(self.checkRedeclared(x,Variable(),env))
        #check in body pass ast de check function hay procedure
        body = list(map(lambda x: self.visit(x, (c,env,ast)), ast.body))
        check_ret = [] # consist of list if statement
        check = 0
        for x in body:
            if isinstance(x,Break):
                raise BreakNotInLoop
            elif isinstance(x,Continue):
                raise ContinueNotInLoop
            if isinstance(x,If) and isinstance(kind,Function) and check == 0:
                check_ret.append(x)
            if isinstance(x,With) and isinstance(kind,Function) and check == 0:
                check_ret.append(x)
            if isinstance(x,Return) and isinstance(kind,Function):
                check = 1
        
        #check return function
        if isinstance(kind,Function):
            if check == 0 :
                if check_ret == []:
                    raise FunctionNotReturn(ast.name.name)
                else:# list if statemnet different []
                    a = False
                    for x in check_ret[::-1]:
                        a = self.visit(x,(a,ast))
                    if a == False:
                        raise FunctionNotReturn(ast.name.name)
            else:# check == 1 
                pass
                    
        return None

    def visitVarDecl(self, ast, c):
        #variable:Id("a") -- Id -> name
        #varType: Type
        return None

    # stmt
    # Assign - If - While - For - Break - Continue - Return - With - CallStmt 
    def visitAssign(self, ast, c):
        #lhs:Expr -- except string and array type
        #exp:Expr
        type_lhs = self.visit(ast.lhs, c)
        type_rhs = self.visit(ast.exp, c)
        if type(type_lhs) is StringType or type(type_lhs) is ArrayType or type(type_rhs) is ArrayType:
            raise TypeMismatchInStatement(ast)
        if type(type_lhs) is FloatType and type(type_rhs) is IntType:
            return type_lhs
        elif type(type_lhs) != type(type_rhs):
            raise TypeMismatchInStatement(ast)
        else:
            return type_lhs

    def visitIf(self, ast, c):
        #expr:Expr --boolean
        #thenStmt:list(Stmt)
        #elseStmt:list(Stmt)

        #check return in function
        if isinstance(c[0],bool): #c[0] : bool c[1]:ast
            if c[0] == False:
                if (ast.elseStmt == [] and ast.thenStmt == []):
                    raise FunctionNotReturn(c[1].name.name) 
                elif (ast.elseStmt != [] and ast.thenStmt == []):
                    raise FunctionNotReturn(c[1].name.name) 
                elif (ast.elseStmt == [] and ast.thenStmt != []):
                    raise FunctionNotReturn(c[1].name.name) 
                else:
                    #checkhaveif ->return [list(if) , check] check : 1 : have return , 0 not return
                    tt = self.checkhaveif(ast.thenStmt,c[1])
                    el = self.checkhaveif(ast.elseStmt,c[1])
                    #print(tt)
                    #print(el)
                    if tt == True and el == True:
                        return True
                    raise FunctionNotReturn(c[1].name.name)
            else:
                if ast.elseStmt == []:
                    return True
                else:
                    el = self.checkhaveif(ast.elseStmt,c[1])
                    if el == True:
                        return True
                    raise FunctionNotReturn(c[1].name.name)
        
        else:
            condition = self.visit(ast.expr, c)
            if not type(condition) is BoolType :
                raise TypeMismatchInStatement(ast)

            thenStmt = [self.visit(x, c) for x in ast.thenStmt]
            elseStmt = [self.visit(x, c) for x in ast.elseStmt]
            
            lst = thenStmt + elseStmt
            if len(c) == 3 : # len(c) == 4 if it in loop
                for x in lst:
                    if isinstance(x,Break):
                        raise BreakNotInLoop
                    if isinstance(x,Continue):
                        raise ContinueNotInLoop 
            return ast

    def visitWhile(self, ast, c):
        #sl:list(Stmt)
        #exp: Expr
        exp = self.visit(ast.exp, c)
        #c[0] is global , c[1] is local , c[2] determine kind func, True is determine break , continue
        if not isinstance(exp,BoolType):
            raise TypeMismatchInStatement(ast)
        loop = [self.visit(x, (c[0], c[1], c[2], True)) for x in ast.sl]
        
        return ast

    def visitFor(self, ast, c):
        #id:Id
        #expr1,expr2:Expr
        #loop:list(Stmt)
        #up:Boolean #True => increase; False => decrease
        
        type_id = self.visit(ast.id, c)
        type_expr1 = self.visit(ast.expr1, c)
        type_expr2 = self.visit(ast.expr2, c)
        #c[0] is global , c[1] is local , c[2] determine kind func , True is determine break , continue
        loop = [self.visit(x, (c[0], c[1], c[2], True)) for x in ast.loop]
        if not isinstance(type_id,IntType) or not isinstance(type_expr1,IntType) or not isinstance(type_expr2,IntType):
            raise TypeMismatchInStatement(ast)
        
        return ast

    def visitBreak(self, ast, c):
        return ast

    def visitContinue(self, ast, c):
        return ast

    def visitReturn(self, ast, c):
        #check function return 
        if not isinstance(c[0],list):
            return None
        else:
            type = c[2].returnType
            if isinstance(type,VoidType): #procedure
                if not ast.expr is None:
                    raise TypeMismatchInStatement(ast)
            else: # function
                if ast.expr is None:
                    raise TypeMismatchInStatement(ast)
                type_exp = self.visit(ast.expr,c)
                if isinstance(type,ArrayType) and isinstance(type_exp,ArrayType):
                    if int(str(type.lower)) != int(str(type_exp.lower)):
                        raise TypeMismatchInStatement(ast)
                    if int(str(type.upper)) != int(str(type_exp.upper)):
                        raise TypeMismatchInStatement(ast)
                    if str(type.eleType) != str(type_exp.eleType):
                        raise TypeMismatchInStatement(ast)
                elif isinstance(type,FloatType) and isinstance(type_exp,IntType):
                    return ast
                elif not str(type) == str(type_exp):
                    raise TypeMismatchInStatement(ast)         
            return ast 
        
        

    def visitWith(self, ast, c):
        #decl:list(VarDecl)
        #stmt:list(Stmt)
        if isinstance(c[0],bool): #c[0] : bool c[1]:ast
            if c[0] == False:
                if ast.stmt == []:
                    raise FunctionNotReturn(c[1].name.name) 
                else:
                    #checkhaveif ->return [list(if) , check] check : 1 : have return , 0 not return
                    st = self.checkhaveif(ast.stmt,c[1])
                    
                    if st == True:
                        return True
                    raise FunctionNotReturn(c[1].name.name)
        else:
            decl = [Symbol(x.variable.name, x.varType) for x in ast.decl] 
            env=[]
            for item in decl:
                env.append(self.checkRedeclared(item, Variable(), env))
            
            if len(c) == 3 : # len(c)==3 if it in loop
                stmt = [self.visit(x, (c[0],env + c[1],c[2])) for x in ast.stmt]
                for x in stmt:
                    if isinstance(x,Break):
                        raise BreakNotInLoop
                    elif isinstance(x,Continue):
                        raise ContinueNotInLoop
            else:
                stmt = [self.visit(x, (c[0],env + c[1],c[2],c[3])) for x in ast.stmt]
            return ast

    def visitCallStmt(self, ast, c):    
        #c: consist of all decl in program and param and local of funtion
        #method:Id
        #param:list(Expr)
        #at is a list consist of type of param is declared in scope -ast
        at = [self.visit(x,c) for x in ast.param]
        #check declare procedure
        res = self.lookup(ast.method.name.lower(), c[1], lambda x: x.name.lower())
        if not res is None:
            raise Undeclared(Procedure(), ast.method.name)
        res = self.lookup(ast.method.name.lower(), c[0], lambda x: x.name.lower())
        if res is None :
            raise Undeclared(Procedure(), ast.method.name)
        elif not type(res.mtype) is MType :
            raise Undeclared(Procedure(), ast.method.name)
        elif not type(res.mtype.rettype) is VoidType:
            raise Undeclared(Procedure(), ast.method.name)
        # Case res not null
        if len(res.mtype.partype) != len(at):
            raise TypeMismatchInStatement(ast)
        if len(at) == 0:
            return res.mtype.rettype  
        #check parram in call exp have like with function declared before .
        lst = zip(at,res.mtype.partype)
        for a,b in lst:
            if type(a) == type(b) and isinstance(a,ArrayType):
                if int(str(a.lower)) != int(str(b.lower)):
                    raise TypeMismatchInStatement(ast)
                if int(str(a.upper)) != int(str(b.upper)):
                    raise TypeMismatchInStatement(ast)
                if str(a.eleType) != str(b.eleType):
                    raise TypeMismatchInStatement(ast)
            elif type(a) == type(b) or (isinstance(a,IntType) and isinstance(b,FloatType)):
                pass
            else:
                raise TypeMismatchInStatement(ast)
        
        return res.mtype.rettype


    # Expr
    # BinaryOp - UnaryOp - CallExpr 
    def visitBinaryOp(self, ast, c):
        #op:string: AND THEN => andthen; OR ELSE => orelse; other => keep it
        #left:Expr
        #right:Expr
        lefttype = self.visit(ast.left, c)
        righttype = self.visit(ast.right, c)
        if isinstance(lefttype,StringType) or isinstance(righttype,StringType):
            raise TypeMismatchInExpression(ast)
        if isinstance(lefttype,ArrayType) or isinstance(righttype,ArrayType):
            raise TypeMismatchInExpression(ast)
        if type(lefttype) == type(righttype):
            if isinstance(lefttype,BoolType):
                if ast.op.lower() in ['andthen','orelse','and','or']:
                    return BoolType()
                else:
                    raise TypeMismatchInExpression(ast)
            if isinstance(lefttype,IntType):
                if ast.op.lower() in ['+','-','*','div','mod']:
                    return IntType()
                elif ast.op in ['<','<=','>','>=','<>','=']:
                    return BoolType()
                elif ast.op in ['/']:
                    return FloatType()
                else:
                    raise TypeMismatchInExpression(ast)
            elif isinstance(lefttype,FloatType):
                if ast.op in ['+','-','*','/']:
                    return FloatType()
                elif ast.op in ['<','<=','>','>=','<>','=']:
                    return BoolType()
                else:
                    raise TypeMismatchInExpression(ast)  
        else:
            if type(lefttype) == type(IntType()) and type(righttype) == type(FloatType()):
                if ast.op in ['+','-','*','/']:
                    return FloatType()
                elif ast.op in ['<','<=','>','>=','<>','=']:
                    return BoolType()
                else:
                    raise TypeMismatchInExpression(ast)
            elif type(lefttype) == type(FloatType()) and type(righttype) == type(IntType()):
                if ast.op in ['+','-','*','/']:
                    return FloatType()
                elif ast.op in ['<','<=','>','>=','<>','=']:
                    return BoolType()
                else:
                    raise TypeMismatchInExpression(ast)
            else:
                raise TypeMismatchInExpression(ast)
    
    def visitUnaryOp(self, ast, c):
        #op:string
        #body:Expr
        body = self.visit(ast.body, c)
        if ast.op == '-':
            if not (isinstance(body,IntType) or isinstance(body,FloatType)):
                raise TypeMismatchInExpression(ast)
            return body
        elif ast.op.lower() == 'not':
            if isinstance(body,BoolType):
                return BoolType()
            raise TypeMismatchInExpression(ast)
        else:
            raise TypeMismatchInExpression(ast)

    def visitCallExpr(self, ast, c):
        #method:Id
        #param:list(Expr)
        #Symbol(foo,MPType([],IntType))
        para_lst = [self.visit(x, c) for x in ast.param]
        res = self.lookup(ast.method.name.lower(), c[1], lambda x: x.name.lower())
        if not res is None:
            raise Undeclared(Function(),ast.method.name)
        res = self.lookup(ast.method.name.lower(), c[0], lambda x: x.name.lower())
        if res is None:
            raise Undeclared(Function(),ast.method.name) 
        elif not type(res.mtype) is MType :
            raise Undeclared(Function(), ast.method.name)
        elif type(res.mtype.rettype) is VoidType:
            raise Undeclared(Function(), ast.method.name)

        #check like number of param
        if len(res.mtype.partype) != len(para_lst):
            raise TypeMismatchInExpression(ast)
        
        if len(para_lst) == 0:
            return res.mtype.rettype
        #check parram in call exp have like with function declared before .
        lst = zip(para_lst,res.mtype.partype)
        for a,b in lst:
            if type(a) == type(b) and isinstance(a,ArrayType):
                if int(str(a.lower)) != int(str(b.lower)):
                    raise TypeMismatchInExpression(ast)
                if int(str(a.upper)) != int(str(b.upper)):
                    raise TypeMismatchInExpression(ast)
                if str(a.eleType) != str(b.eleType):
                    raise TypeMismatchInExpression(ast)
            elif type(a) == type(b) or (isinstance(a,IntType) and isinstance(b,FloatType)):
                pass
            else:
                raise TypeMismatchInExpression(ast)
        
        return res.mtype.rettype
        

    #LHS
    #Id - ArrayCell 
    def visitId(self, ast, c):
        res = self.lookup(ast.name.lower(), c[1], lambda x: x.name.lower())
        if res is None:
            res = self.lookup(ast.name.lower(), c[0], lambda x: x.name.lower())
        if res:
            if not isinstance(res.mtype,MType):
                return res.mtype
            else:
                raise Undeclared(Identifier(), ast.name) 
        else:
            raise Undeclared(Identifier(), ast.name)

    def visitArrayCell(self,ast,c):
        #arr:Expr -> ArrayType(lower,upper,eleType)
        #idx:Expr
        type_arr = self.visit(ast.arr, c)
        type_idx = self.visit(ast.idx, c)
        if not isinstance(type_arr, ArrayType):
            raise TypeMismatchInExpression(ast)
        if not isinstance(type_idx, IntType):
            raise TypeMismatchInExpression(ast)
        return type_arr.eleType

    #Literal
    #IntLiteral - FloatLiteral - StringLiteral - BooleanLiteral
    
    def visitIntLiteral(self, ast, c):
        return IntType()

    def visitBooleanLiteral(self, ast, c):
        return BoolType()

    def visitFloatLiteral(self, ast, c):
        return FloatType()
    
    def visitStringLiteral(self, ast, c):
        return StringType()
        
