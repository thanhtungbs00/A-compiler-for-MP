from MPVisitor import MPVisitor
from MPParser import MPParser
from functools import reduce
from AST import *
from functools import *

class ASTGeneration(MPVisitor):
    def visitProgram(self,ctx:MPParser.ProgramContext):
        lst = [self.visit(x) for x in ctx.declaration()]
        retlst = []
        for item in lst:
            if(isinstance(item,list)):
                for subitem in item:
                    retlst.append(subitem)
            else:
                retlst.append(item)
        return Program(retlst)
    
    def visitVarblock(self,ctx:MPParser.VarblockContext):
        #return  [self.visit(x) for x in ctx.var_dec()]
        return [x for y in ctx.var_dec() for x in self.visit(y)]

    def visitVar_dec(self,ctx:MPParser.Var_decContext):
        if(ctx.ptypes()):
            varType = self.visit(ctx.ptypes())
        elif ctx.ctypes():
            varType = self.visit(ctx.ctypes())
        listID = self.visit(ctx.listid())
        return [VarDecl(x,varType) for x in listID]
        
    def visitListid(self,ctx:MPParser.ListidContext):
        if ctx.listid():
            return [Id(ctx.ID().getText())] + self.visit(ctx.listid())
        else:
            return [Id(ctx.ID().getText())]
        
    def visitPtypes(self,ctx:MPParser.PtypesContext):
        if ctx.INTTYPE():
            return IntType()
        elif ctx.BOOLEANTYPE():
            return BoolType()
        elif ctx.REALTYPE():
            return FloatType()
        elif ctx.STRINGTYPE():
            return StringType()

    def visitCtypes(self,ctx:MPParser.CtypesContext):
        lst=self.visit(ctx.index())
        return ArrayType(lst[0],lst[1],self.visit(ctx.ptypes()))
        
    def visitIndex(self,ctx:MPParser.IndexContext):
        lst=[]
        lst.append(self.visit(ctx.lower(0)))
        lst.append(self.visit(ctx.lower(1)))
        return lst
    
    def visitLower(self,ctx:MPParser.LowerContext):
        if ctx.SUBOP():
            return "-"+ctx.INTLIT().getText()
        else:
            return ctx.INTLIT()

    def visitProcblock(self,ctx:MPParser.ProcblockContext):
        lst = self.visit(ctx.listpara()) if ctx.listpara() else []
        lstparam=[]
        for item in lst:
            if isinstance(item,list):
                for subitem in item:
                    lstparam.append(subitem)
            else:
                lstparam.append(item)
        if ctx.varblock():
            local = [x for y in ctx.varblock() for x in self.visit(y)]
        else:
            local = []
        cpstmt = self.visit(ctx.compound_stt()) 
        return FuncDecl(Id(ctx.ID().getText()),
                        lstparam,
                        local,
                        cpstmt)

    def visitFuncblock(self,ctx:MPParser.FuncblockContext):
        lst = self.visit(ctx.listpara()) if ctx.listpara() else []
        lstparam=[]
        for item in lst:
            if isinstance(item,list):
                for subitem in item:
                    lstparam.append(subitem)
            else:
                lstparam.append(item)
        if ctx.varblock():
            local = [x for y in ctx.varblock() for x in self.visit(y)]
        else:
            local = []
        cpstmt = self.visit(ctx.compound_stt()) 
        
        funcType = self.visit(ctx.return_type())
        
        return FuncDecl(Id(ctx.ID().getText()),
                        lstparam,
                        local,
                        cpstmt,
                        funcType
                        )
    
    def visitReturn_type(self,ctx:MPParser.Return_typeContext):
        if ctx.ptypes():
            return self.visit(ctx.ptypes())
        elif ctx.ctypes():
            return self.visit(ctx.ctypes())

    def visitListpara(self,ctx:MPParser.ListparaContext):
        if ctx.listpara():
            return [self.visit(ctx.var_dec())] + self.visit(ctx.listpara())
        else:
            return [self.visit(ctx.var_dec())]

    def visitCompound_stt(self,ctx:MPParser.Compound_sttContext):
        return self.visit(ctx.liststt()) if ctx.liststt() else []

    def visitExp(self,ctx:MPParser.ExpContext):
        if ctx.exp():
            if ctx.andthen():
                return BinaryOp(self.visit(ctx.andthen()),self.visit(ctx.exp()),self.visit(ctx.exp1()))
            elif ctx.orelse():
                return BinaryOp(self.visit(ctx.orelse()),self.visit(ctx.exp()),self.visit(ctx.exp1()))
        
        else:
            return self.visit(ctx.exp1())

    def visitAndthen(self,ctx:MPParser.AndthenContext):
        return "andthen"

    def visitOrelse(self,ctx:MPParser.OrelseContext):
        return "orelse"

    def visitExp1(self,ctx:MPParser.Exp1Context):
        if ctx.op1():
            return BinaryOp(self.visit(ctx.op1()),self.visit(ctx.exp2(0)),self.visit(ctx.exp2(1)))
        else:
            return self.visit(ctx.exp2(0))

    def visitOp1(self,ctx:MPParser.Op1Context):
        if ctx.EQ():
            return ctx.EQ().getText()
        elif ctx.NEQ():
            return ctx.NEQ().getText()
        elif ctx.LT():
            return ctx.LT().getText()
        elif ctx.GT():
            return ctx.GT().getText()
        elif ctx.LTE():
            return ctx.LTE().getText()
        elif ctx.GTE():
            return ctx.GTE().getText()
    

    def visitExp2(self,ctx:MPParser.Exp2Context):
        if ctx.exp2():
            if ctx.ADDOP():
                return BinaryOp(ctx.ADDOP().getText(),self.visit(ctx.exp2()),self.visit(ctx.exp3()))
            elif ctx.SUBOP():
                return BinaryOp(ctx.SUBOP().getText(),self.visit(ctx.exp2()),self.visit(ctx.exp3()))
            elif ctx.OR():
                return BinaryOp(ctx.OR().getText(),self.visit(ctx.exp2()),self.visit(ctx.exp3()))
        else:
            return self.visit(ctx.exp3())

    def visitExp3(self,ctx:MPParser.Exp3Context):
        if ctx.exp3():
            if ctx.DIV():
                return BinaryOp(ctx.DIV().getText(),self.visit(ctx.exp3()),self.visit(ctx.exp4()))
            elif ctx.DIVOP():
                return BinaryOp(ctx.DIVOP().getText(),self.visit(ctx.exp3()),self.visit(ctx.exp4()))
            elif ctx.MULOP():
                return BinaryOp(ctx.MULOP().getText(),self.visit(ctx.exp3()),self.visit(ctx.exp4()))
            elif ctx.MOD():
                return BinaryOp(ctx.MOD().getText(),self.visit(ctx.exp3()),self.visit(ctx.exp4()))
            elif ctx.AND():
                return BinaryOp(ctx.AND().getText(),self.visit(ctx.exp3()),self.visit(ctx.exp4()))
        else:
            return self.visit(ctx.exp4())

    def visitExp4(self,ctx:MPParser.Exp4Context):
        if ctx.exp4():
            if ctx.SUBOP():
                return UnaryOp(ctx.SUBOP().getText(),self.visit(ctx.exp4()))
            elif ctx.NOT():
                return UnaryOp(ctx.NOT().getText(),self.visit(ctx.exp4()))
        else:
            return self.visit(ctx.unary())
            
    def visitUnary(self,ctx:MPParser.UnaryContext):
        if ctx.INTLIT():
            return IntLiteral(ctx.INTLIT())
        elif ctx.REALLIT():
            return FloatLiteral(ctx.REALLIT())
        elif ctx.STRINGLIT():
            return StringLiteral(ctx.STRINGLIT().getText())
        elif ctx.TRUE():
            return BooleanLiteral("True")
        elif ctx.FALSE():
            return BooleanLiteral("False")
        elif ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.indexexp(): 
            return self.visit(ctx.indexexp())
        elif ctx.funcall():
            return self.visit(ctx.funcall())
        elif ctx.exp():       
            return self.visit(ctx.exp())

    def visitIndexexp(self,ctx:MPParser.IndexexpContext):
        return ArrayCell(self.visit(ctx.literal()),self.visit(ctx.exp()))
    
    def visitLiteral(self,ctx:MPParser.LiteralContext):
        if ctx.INTLIT():
            return IntLiteral(ctx.INTLIT())
        elif ctx.REALLIT():
            return FloatLiteral(ctx.REALLIT())
        elif ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.funcall():
            return self.visit(ctx.funcall())
        elif ctx.exp():       
            return self.visit(ctx.exp())
    
        
    def visitListstt(self,ctx:MPParser.ListsttContext):
        if ctx.liststt():
            return self.visit(ctx.statements()) + self.visit(ctx.liststt())
        else:
            return self.visit(ctx.statements())

    def visitStatements(self,ctx:MPParser.StatementsContext):
        if ctx.assignment():
            return self.visit(ctx.assignment())
        elif ctx.ifstatement():
            return self.visit(ctx.ifstatement())
        elif ctx.ifnostatement():
            return self.visit(ctx.ifnostatement())
        elif ctx.whilestatement():
            return self.visit(ctx.whilestatement())
        elif ctx.forstatement():
            return self.visit(ctx.forstatement())
        elif ctx.breakstatement():
            return self.visit(ctx.breakstatement())
        elif ctx.continuestatement():
            return self.visit(ctx.continuestatement())
        elif ctx.returnstatement():
            return self.visit(ctx.returnstatement())
        elif ctx.compound_stt():
            return self.visit(ctx.compound_stt())
        elif ctx.withstatement():
            return self.visit(ctx.withstatement())
        elif ctx.funcall_stt():
            return self.visit(ctx.funcall_stt())
    
    def visitAssignment(self,ctx:MPParser.AssignmentContext):
        lhs = self.visit(ctx.idassign())
        exp = self.visit(ctx.exp())
        lhs.append(exp)
        lhs=lhs[::-1]
        ls=[]
        i = len(lhs)-1
        for x in range(0,i):
            ls.append(Assign(lhs[x+1],lhs[x]))
        return ls  

    def visitIdassign(self,ctx:MPParser.IdassignContext):
        if ctx.idassign():
            item = [Id(ctx.ID().getText())] if ctx.ID() else [self.visit(ctx.indexexp())]
            return item + self.visit(ctx.idassign())
        else:
            return [Id(ctx.ID().getText())] if ctx.ID() else [self.visit(ctx.indexexp())]


    def visitIfstatement(self,ctx:MPParser.IfstatementContext):
        exp = self.visit(ctx.exp())
        thenStmt = self.visit(ctx.statements(0))
        if ctx.ELSE():
            elseStmt = self.visit(ctx.statements(1))
            return [If(exp,thenStmt,elseStmt)]
        else:
            return [If(exp,thenStmt)]

    def visitIfnostatement(self,ctx:MPParser.IfnostatementContext):
        exp = self.visit(ctx.exp())
        thenStmt = self.visit(ctx.statements(0))
        if ctx.ELSE():
            elseStmt = self.visit(ctx.statements(1))
            return [If(exp,thenStmt,elseStmt)]
        else:
            return [If(exp,thenStmt)]

    def visitWhilestatement(self,ctx:MPParser.WhilestatementContext):
        return [While(self.visit(ctx.exp()),self.visit(ctx.statements()))]

    def visitForstatement(self,ctx:MPParser.ForstatementContext):
        ID = self.visit(ctx.identifier())
        expr1 = self.visit(ctx.exp(0))
        expr2 = self.visit(ctx.exp(1))
        up = self.visit(ctx.typefor())
        list_sttm = self.visit(ctx.statements())
        return [For(ID,expr1,expr2,up,list_sttm)]
    
    def visitIdentifier(self,ctx:MPParser.IdentifierContext):
        return Id(ctx.ID().getText())

    def visitTypefor(self,ctx:MPParser.TypeforContext):
        if ctx.TO():
            return "True"
        elif ctx.DOWNTO():
            return "False"

    def visitBreakstatement(self,ctx:MPParser.BreakstatementContext):
        return [Break()]

    def visitContinuestatement(self,ctx:MPParser.ContinuestatementContext):
        return [Continue()]

    def visitReturnstatement(self,ctx:MPParser.ReturnstatementContext):
        if ctx.exp():
            return [Return(self.visit(ctx.exp()))]
        else:
            return [Return()]

    def visitWithstatement(self,ctx:MPParser.WithstatementContext):
        list_var = self.visit(ctx.list_var_dec())
        lst=[]
        for item in list_var:
            if isinstance(item,list):
                for subitem in item:
                    lst.append(subitem)
            else:
                lst.append(item)
        stmt = self.visit(ctx.statements())
        return [With(lst,stmt)]

    def visitList_var_dec(self,ctx:MPParser.List_var_decContext):
        if ctx.list_var_dec():
            return [self.visit(ctx.var_dec())] + self.visit(ctx.list_var_dec())
        else:
            return [self.visit(ctx.var_dec())]
    #Call function haven't semi 
    def visitFuncall(self,ctx:MPParser.FuncallContext):
        ID = Id(ctx.ID().getText())
        lst_param = self.visit(ctx.list_exp()) if ctx.list_exp() else []
        return CallExpr(ID,lst_param)
    
    def visitList_exp(self,ctx:MPParser.List_expContext):
        if ctx.list_exp():
            return [self.visit(ctx.para_call())] + self.visit(ctx.list_exp())
        else: 
            return [self.visit(ctx.para_call())]

    def visitPara_call(self,ctx:MPParser.Para_callContext):
        if ctx.exp():
            return self.visit(ctx.exp())
        else: 
            return StringLiteral(ctx.STRINGLIT().getText())

    #Call function have semi -> statemnent
    def visitFuncall_stt(self,ctx:MPParser.Funcall_sttContext):
        ID = Id(ctx.ID().getText())
        lst_param = self.visit(ctx.list_exp()) if ctx.list_exp() else []
        return [CallStmt(ID,lst_param)]

    
        

