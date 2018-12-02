'''
Cao Thanh Tung -1613989
'''
from Utils import *
from StaticCheck import *
from StaticError import *
from Emitter import Emitter
from Frame import Frame
from abc import ABC, abstractmethod

class CodeGenerator(Utils):
    def __init__(self):
        self.libName = "io"

    def init(self):
        return [Symbol("getInt", MType(list(), IntType()), CName(self.libName)),
                Symbol("putInt", MType([IntType()], VoidType()), CName(self.libName)),
                Symbol("putIntLn", MType([IntType()], VoidType()), CName(self.libName)),
                Symbol("getFloat", MType([], FloatType()), CName(self.libName)),
                Symbol("putFloat", MType([FloatType()], VoidType()), CName(self.libName)),
                Symbol("putFloatLn", MType([FloatType()], VoidType()), CName(self.libName)),
                Symbol("putBool", MType([BoolType()], VoidType()), CName(self.libName)),
                Symbol("putBoolLn", MType([BoolType()], VoidType()), CName(self.libName)),
                Symbol("putString", MType([StringType()], VoidType()), CName(self.libName)),
                Symbol("putStringLn", MType([StringType()], VoidType()), CName(self.libName)),
                Symbol("putLn", MType([], VoidType()), CName(self.libName))
                ]

    def gen(self, ast, dir_):
        #ast: AST
        #dir_: String

        gl = self.init()
        gc = CodeGenVisitor(ast, gl, dir_)
        gc.visit(ast, None)

# class StringType(Type):
    
#     def __str__(self):
#         return "StringType"

#     def accept(self, v, param):
#         return None

class ArrayPointerType(Type):
    def __init__(self, ctype):
        #cname: String
        self.eleType = ctype

    def __str__(self):
        return "ArrayPointerType({0})".format(str(self.eleType))

    def accept(self, v, param):
        return None
class ClassType(Type):
    def __init__(self,cname):
        self.cname = cname
    def __str__(self):
        return "Class({0})".format(str(self.cname))
    def accept(self, v, param):
        return None
        
class SubBody():
    def __init__(self, frame, sym, rettype = None):
        #frame: Frame
        #sym: List[Symbol]

        self.frame = frame
        self.sym = sym
        self.rettype = rettype

class Access():
    def __init__(self, frame, sym, isLeft, isFirst):
        #frame: Frame
        #sym: List[Symbol]
        #isLeft: Boolean
        #isFirst: Boolean

        self.frame = frame
        self.sym = sym
        self.isLeft = isLeft
        self.isFirst = isFirst

class Val(ABC):
    pass

class Index(Val):
    def __init__(self, value):
        #value: Int

        self.value = value

class CName(Val):
    def __init__(self, value):
        #value: String

        self.value = value

class CodeGenVisitor(BaseVisitor, Utils):
    def __init__(self, astTree, env, dir_):
        #astTree: AST
        #env: List[Symbol]
        #dir_: File
        self.astTree = astTree
        self.env = env
        self.className = "MPClass"
        self.path = dir_
        self.emit = Emitter(self.path + "/" + self.className + ".j")

    def genMETHOD(self, consdecl, o, frame):
        #consdecl: FuncDecl   -- ast
        #o: Any -- list symbol
        #frame: Frame
        isInit = consdecl.returnType is None    # True -> init
        isMain = consdecl.name.name.lower() == "main" and len(consdecl.param) == 0 and type(consdecl.returnType) is VoidType
        returnType = VoidType() if isInit else consdecl.returnType
        #methodName = "<init>" if isInit else consdecl.name.name
        if isInit:
            methodName = "<init>"
        elif isMain:
            methodName = "main"
        else:
            methodName = consdecl.name.name
        param = consdecl.param
        lst = list()
        for x in param:
            lst.append(x.varType)
        intype = [ArrayPointerType(StringType())] if isMain else lst
        mtype = MType(intype, returnType)

        self.emit.printout(self.emit.emitMETHOD(methodName, mtype, not isInit, frame))

        frame.enterScope(True)

        glenv = o
        localenv = list()
        # Generate code for parameter declarations
        if isInit:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(self.className), frame.getStartLabel(), frame.getEndLabel(), frame))
        elif isMain:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayPointerType(StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))
        else:## Generate code for param decl of procedure and function
            for x in param:
                localenv = [Symbol(x.variable.name, x.varType, Index(frame.getCurrIndex()))] + localenv
                self.emit.printout(self.emit.emitVAR(frame.getNewIndex(),x.variable.name,x.varType,frame.getStartLabel(),frame.getEndLabel(),frame))
        for x in consdecl.local:
            localenv = [Symbol(x.variable.name, x.varType, Index(frame.getCurrIndex()))] + localenv
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(),x.variable.name,x.varType,frame.getStartLabel(),frame.getEndLabel(),frame))
            
        glenv = localenv + glenv
        body = consdecl.body
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        # Generate code for statements
        if isInit:
            self.emit.printout(self.emit.emitREADVAR("this", ClassType(self.className), 0, frame))
            self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
        
        list(map(lambda x: self.visit(x, SubBody(frame, glenv, consdecl.returnType)), body))

        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        if type(returnType) is VoidType:
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope();

    def visitProgram(self, ast, c):
        #ast: Program
        #c: Any - None
        c = self.env
        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))
        for item in ast.decl:
            if isinstance(item,VarDecl):
                self.emit.printout(self.emit.emitATTRIBUTE(str(item.variable.name), item.varType, False, ""))
                c = [Symbol(item.variable.name, item.varType, CName(self.className))] + c
            elif isinstance(item,FuncDecl):
                c = [Symbol(item.name.name, MType([i.varType for i in item.param], item.returnType), CName(self.className))] + c
        e = SubBody(None, c)
        for x in ast.decl:
            self.visit(x, e)
        # generate default constructor
        self.genMETHOD(FuncDecl(Id("<init>"), list(), list(), list(),None), c, Frame("<init>", VoidType))
        self.emit.emitEPILOG()
        return e.sym

    # Decl
    # FuncDecl - VarDecl
    def visitFuncDecl(self, ast, o):
        #ast: FuncDecl
        #o: Any -- list ( frame (none) - sym (listsym) )
        frame = Frame(ast.name, ast.returnType)
        self.genMETHOD(ast, o.sym, frame)
        return SubBody(None, [Symbol(ast.name, MType(list(), ast.returnType), CName(self.className))] + o.sym)
    
    def visitVarDecl(self, ast, o):
        #self.emit.printout(self.emit.emitATTRIBUTE(str(ast.variable.name), ast.varType, False, ""))
        pass
    
    # stmt
    # Assign - If - While - For - Break - Continue - Return - With - CallStmt 
    # o -- subbody - frame , glenv, return type
    def visitAssign(self, ast, o):
        #lhs:Expr -- except string and array type
        #exp:Expr
        # print(ast)
        rc,rt = self.visit(ast.exp, Access(o.frame, o.sym, False, True))
        lc,lt = self.visit(ast.lhs, Access(o.frame, o.sym, True, False))
        self.emit.printout(rc)
        if isinstance(lt,FloatType) and isinstance(rt,IntType):
            self.emit.printout(self.emit.emitI2F(o.frame))
        self.emit.printout(lc)
        return 0 #Don't have return

    def visitIf(self, ast, o):
        #expr:Expr
        #thenStmt:list(Stmt)
        #elseStmt:list(Stmt)
        #o Subody- frame, sym, rettype
        frame = o.frame
        nenv = o.sym
        check_br_conti = 0
        check_return = 0
        exp, texp = self.visit(ast.expr, Access(frame, nenv, False, False))
        self.emit.printout(exp)
        label1 = frame.getNewLabel()
        label2 = frame.getNewLabel()
        self.emit.printout(self.emit.emitIFEQ(label1, frame))
        for x in ast.thenStmt:
            if isinstance(x, Break) or isinstance(x, Continue) or isinstance(x, Return):
                check_br_conti = self.visit(x, o)
                check_br_conti = 1
                break
            check_return = self.visit(x, o)
        if len(ast.elseStmt) != 0 and check_br_conti == 0 :
            self.emit.printout(self.emit.emitGOTO(label2, frame))
        self.emit.printout(self.emit.emitLABEL(label1, frame))
        for x in ast.elseStmt:
            if isinstance(x, Break) or isinstance(x, Continue) or isinstance(x, Return):
                self.visit(x, o)
                check_br_conti = 1
                break
            self.visit(x, o)
        if len(ast.elseStmt) != 0 :
            self.emit.printout(self.emit.emitLABEL(label2, frame))

        return check_br_conti

    def visitWhile(self, ast, o):
        #sl:list(Stmt)
        #exp: Expr
        check_br_conti = 0
        frame = o.frame
        frame.enterLoop()
        label1 = frame.getContinueLabel()
        label2 = frame.getBreakLabel()
        self.emit.printout(self.emit.emitLABEL(label1, frame))
        str, typ = self.visit(ast.exp, Access(frame, o.sym, False, False))
        self.emit.printout(str)
        self.emit.printout(self.emit.emitIFEQ(label2, frame))
        
        for x in ast.sl:
            if isinstance(x,Break) or isinstance(x, Continue) or isinstance(x, Return):
                self.visit(x, o)
                check_br_conti = 1
                break
            self.visit(x, o)
        if check_br_conti == 0:
            self.emit.printout(self.emit.emitGOTO(label1, frame))
        self.emit.printout(self.emit.emitLABEL(label2, frame))
        frame.exitLoop()

        return 0

    def visitFor(self, ast, o):
        #id:Id
        #expr1,expr2:Expr
        #loop:list(Stmt)
        #up:Boolean #True => increase; False => decrease
        check_br_conti = 0
        up = str(ast.up).lower()
        frame = o.frame
        nenv = o.sym
        label_tmp = frame.getNewLabel()
        frame.enterLoop()
        label1 = frame.getContinueLabel()
        label2 = frame.getBreakLabel()
        rc,rt = self.visit(ast.expr1, Access(frame, nenv, False, True))    #exp
        lc,lt = self.visit(ast.id, Access(frame, nenv, True, False))    # id
        self.emit.printout(rc + lc)
        self.emit.printout(self.emit.emitLABEL(label_tmp, frame))
        # check condition in for
        lid,rid = self.visit(ast.id, Access(frame, nenv, False, True))    # load id
        r_exp2, r_type2 = self.visit(ast.expr2, Access(frame, nenv, False, True))
        self.emit.printout(lid + r_exp2)
        if up == "true":
            self.emit.printout(self.emit.emitREOP('<=', IntType(), frame))
            up_exp = self.emit.emitADDOP('+',IntType(),frame)
        else:
            self.emit.printout(self.emit.emitREOP('>=', IntType(), frame))
            up_exp = self.emit.emitADDOP('-',IntType(),frame)
        self.emit.printout(self.emit.emitIFEQ(label2, frame))
        for x in ast.loop:
            if isinstance(x,Break) or isinstance(x, Continue) or isinstance(x, Return):
                self.visit(x, o)
                check_br_conti = 1
                break
            self.visit(x, o)
        # x = x +/- 1
        self.emit.printout(self.emit.emitLABEL(label1, frame))
        self.emit.printout(lid + self.emit.emitPUSHICONST(1, frame))
        self.emit.printout(up_exp + lc)
        self.emit.printout(self.emit.emitGOTO(label_tmp, frame))
        self.emit.printout(self.emit.emitLABEL(label2, frame))
        frame.exitLoop()

        return 0

    def visitBreak(self, ast, o):
        frame = o.frame
        self.emit.printout(self.emit.emitGOTO(frame.getBreakLabel(), frame))

        return 0

    def visitContinue(self, ast, o):
        frame = o.frame
        self.emit.printout(self.emit.emitGOTO(frame.getContinueLabel(), frame))

        return 0

    def visitReturn(self, ast, o):
        frame = o.frame
        sym = o.sym
        if ast.expr:
            code, type = self.visit(ast.expr, Access(frame,sym,False,True))
            self.emit.printout(code)
            if isinstance(o.rettype, FloatType) and isinstance(type,IntType):
                self.emit.printout(self.emit.emitI2F(frame))
            self.emit.printout(self.emit.emitRETURN(o.rettype, frame))
        else:
            self.emit.printout(self.emit.emitRETURN(VoidType(),frame))
        return 0

    def visitWith(self, ast, o):
        #decl:list(VarDecl)
        #stmt:list(Stmt)
        check_br_conti = 0
        nenv = o.sym
        frame = o.frame
        frame.enterScope(False)
        localenv = []
        for x in ast.decl:
            localenv = [Symbol(x.variable.name, x.varType,Index(frame.getCurrIndex()))] + localenv
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(),x.variable.name,x.varType,frame.getStartLabel(),frame.getEndLabel(),frame))
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        nenv = localenv + nenv
        for x in ast.stmt:
            if isinstance(x, Break) or isinstance(x, Continue) or isinstance(x, Return):
                self.visit(x, SubBody(frame, nenv, o.rettype))
                check_br_conti = 1
                break
            self.visit(x, SubBody(frame, nenv, o.rettype))
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        frame.exitScope()

        return check_br_conti

    def visitCallStmt(self, ast, o):
        #ast: CallStmt
        #o: Any         -- arg 1 -> frame , arg 2 -> list symbol
        frame = o.frame
        nenv = o.sym         # list symbol
        sym = self.lookup(ast.method.name.lower(), nenv, lambda x: x.name.lower())
        cname = sym.value.value
        ctype = sym.mtype
        ltype = list()
        lstr = ""
        for x,y in zip(ast.param,sym.mtype.partype):
            str1, typ1 = self.visit(x, Access(frame, nenv, False, True)) #frame, sym, isLeft, isFirst 
            ltype.append(typ1)
            lstr = lstr + str1 
            if isinstance(y,FloatType) and isinstance(typ1,IntType):
                lstr = lstr + self.emit.emitI2F(frame)

        self.emit.printout(lstr)
        self.emit.printout(self.emit.emitINVOKESTATIC(cname + "/" + sym.name, ctype, frame))

        return 0
    # Expr
    # BinaryOp - UnaryOp - CallExpr 
     #o : Access(Frame, Sym,False,Fasle)
    def visitBinaryOp(self, ast, o):
        #op:string
        #left:Expr
        #right:Expr
        frame = o.frame
        nenv = o.sym
        l_code, l_type = self.visit(ast.left, o)
        r_code, r_type = self.visit(ast.right, o)
        op = ast.op.lower()
        if op in ['=','<=','>=','>','<','<>']:
            if type(l_type) == type(r_type): # -- int or floar
                if isinstance(l_type,IntType):
                    return l_code + r_code + self.emit.emitREOP(op, IntType(), frame), BoolType()
                else:
                    return l_code + r_code + self.emit.emitREOP(op, FloatType(), frame), BoolType()
            elif isinstance(l_type,FloatType) and isinstance(r_type,IntType):# float op int
                return l_code + r_code + self.emit.emitI2F(frame) + self.emit.emitREOP(op, FloatType(), frame), BoolType()
            else: # int op float
                return l_code + self.emit.emitI2F(frame) + r_code + self.emit.emitREOP(op, FloatType(), frame), BoolType()
        elif op in ['+','-']:
            if type(l_type) == type(r_type): # -- int or floar
                if isinstance(l_type,IntType):
                    return l_code + r_code + self.emit.emitADDOP(str(op),IntType(),frame), IntType()
                else:
                    return l_code + r_code + self.emit.emitADDOP(str(op),FloatType(),frame), FloatType()
            elif isinstance(l_type,FloatType) and isinstance(r_type,IntType): # float op int
                return l_code + r_code + self.emit.emitI2F(frame) + self.emit.emitADDOP(str(op),FloatType(),frame), FloatType()
            else: # int op float
                return l_code + self.emit.emitI2F(frame) + r_code + self.emit.emitADDOP(str(op),FloatType(),frame), FloatType()
        elif op in ['*','/']:
            if type(l_type) == type(r_type): # -- int or floar
                if isinstance(l_type,IntType):
                    if op == '/':
                        return l_code + self.emit.emitI2F(frame) + r_code + self.emit.emitI2F(frame) + self.emit.emitMULOP(str(op),FloatType(),frame), FloatType()
                    return l_code + r_code + self.emit.emitMULOP(str(op),IntType(),frame), IntType()
                else:
                    return l_code + r_code + self.emit.emitMULOP(str(op),FloatType(),frame), FloatType()
            elif isinstance(l_type,FloatType) and isinstance(r_type,IntType): # float op int
                return l_code + r_code + self.emit.emitI2F(frame) + self.emit.emitMULOP(str(op),FloatType(),frame), FloatType()
            else: # int op float
                return l_code + self.emit.emitI2F(frame) + r_code + self.emit.emitMULOP(str(op),FloatType(),frame), FloatType()
        elif op in ['div','mod']:
            if op == 'div':
                return l_code + r_code + self.emit.emitDIV(frame), IntType()
            else:
                return l_code + r_code + self.emit.emitMOD(frame), IntType()
        # ['and', 'or', 'andthen', 'orelse']:
        if op == 'and':
            return l_code + r_code + self.emit.emitANDOP(frame), BoolType()
        elif op == 'or':
            return l_code + r_code + self.emit.emitOROP(frame), BoolType()
        
        label1 = frame.getNewLabel()
        label2 = frame.getNewLabel()
        label3 = frame.getNewLabel()
        label4 = frame.getNewLabel()
        
        if op == 'andthen':
            code = l_code + self.emit.emitIFEQ(label1, frame)
            code = code + r_code + self.emit.emitIFEQ(label1, frame) + self.emit.emitPUSHICONST(1, frame) 
            code = code + self.emit.emitGOTO(label2, frame) + self.emit.emitLABEL(label1, frame)
            code = code + self.emit.emitPUSHICONST(0, frame) + self.emit.emitLABEL(label2, frame)
            return code, BoolType()
        elif op == 'orelse':
            code = l_code + self.emit.emitIFEQ(label4, frame)+ self.emit.emitGOTO(label2, frame)
            code = code + self.emit.emitLABEL(label4, frame) + r_code + self.emit.emitIFEQ(label1, frame) + self.emit.emitGOTO(label2, frame)
            code = code + self.emit.emitLABEL(label1, frame) + self.emit.emitPUSHICONST(0, frame) + self.emit.emitGOTO(label3, frame)
            code = code + self.emit.emitLABEL(label2, frame) + self.emit.emitPUSHICONST(1, frame) 
            code = code + self.emit.emitLABEL(label3, frame)
            return code, BoolType()
        

    def visitUnaryOp(self, ast, o):
        #op:string
        #body:Expr
        #print(ast.body)
        lc, rt = self.visit(ast.body, Access(o.frame, o.sym, False, False))
        if str(ast.op).lower() == "not":
            return lc + self.emit.emitNOT(BoolType(), o.frame), BoolType()
        else:
            return lc + self.emit.emitNEGOP(rt, o.frame), rt   
    
    def visitCallExpr(self, ast, o):
        #method:Id
        #param:list(Expr)
        sym = self.lookup(ast.method.name.lower(), o.sym, lambda x: x.name.lower())
        mtype = sym.mtype
        cname = sym.value.value
        code =""
        for x,y in zip(ast.param, mtype.partype):
            lc, lt = self.visit(x, Access(o.frame, o.sym, False, False))
            code = code + lc
            if isinstance(y, FloatType) and isinstance(lt, IntType):
                code = code + self.emit.emitI2F(o.frame)
        code = code + self.emit.emitINVOKESTATIC(cname + "/" + sym.name, mtype, o.frame)
        return code, mtype.rettype

    #LHS
    #Id - ArrayCell 
    def visitId(self, ast, o):
        #ast - name 
        #o: Any ---frame, sym, isLeft, isFirst 
        sym = self.lookup(ast.name.lower(), o.sym, lambda x: x.name.lower())
        if o.isLeft:
            if type(sym.value) is CName:# it is a global variable
                return self.emit.emitPUTSTATIC(sym.value.value + "/" + sym.name, sym.mtype, o.frame), sym.mtype
            else:#it is a param or local variable
                return self.emit.emitWRITEVAR(sym.name, sym.mtype, sym.value.value, o.frame), sym.mtype
        else:
            if type(sym.value) is CName:# it is a global variable
                return self.emit.emitGETSTATIC(sym.value.value + "/" + sym.name, sym.mtype, o.frame), sym.mtype
            else:#it is a param or local variable
                return self.emit.emitREADVAR(sym.name, sym.mtype, sym.value.value, o.frame), sym.mtype

    def visitArrayCell(self, ast, o):
        pass

    #Literal
    #IntLiteral - FloatLiteral - StringLiteral - BooleanLiteral
    def visitIntLiteral(self, ast, o):
        #ast: IntLiteral
        #o: Any ---frame, sym, isLeft, isFirst
        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHICONST(int(str(ast.value)), frame), IntType()

    def visitFloatLiteral(self, ast, o):
        #ast: FloatLiteral
        #o: Any ---frame, sym, isLeft, isFirst 
        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHFCONST(str(ast.value), frame) , FloatType()
    
    def visitStringLiteral(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHCONST('"' + str(ast.value) + '"', StringType(), frame) , StringType()
    
    def visitBooleanLiteral(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHICONST(str(ast.value).lower(), frame), BoolType()