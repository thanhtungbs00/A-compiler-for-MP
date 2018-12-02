# Generated from main/mp/parser/MP.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MPParser import MPParser
else:
    from MPParser import MPParser

# This class defines a complete generic visitor for a parse tree produced by MPParser.

class MPVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MPParser#program.
    def visitProgram(self, ctx:MPParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#declaration.
    def visitDeclaration(self, ctx:MPParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#ptypes.
    def visitPtypes(self, ctx:MPParser.PtypesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#ctypes.
    def visitCtypes(self, ctx:MPParser.CtypesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#index.
    def visitIndex(self, ctx:MPParser.IndexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#lower.
    def visitLower(self, ctx:MPParser.LowerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#varblock.
    def visitVarblock(self, ctx:MPParser.VarblockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#var_dec.
    def visitVar_dec(self, ctx:MPParser.Var_decContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#listid.
    def visitListid(self, ctx:MPParser.ListidContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#procblock.
    def visitProcblock(self, ctx:MPParser.ProcblockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#funcblock.
    def visitFuncblock(self, ctx:MPParser.FuncblockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#funcall.
    def visitFuncall(self, ctx:MPParser.FuncallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#list_exp.
    def visitList_exp(self, ctx:MPParser.List_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#para_call.
    def visitPara_call(self, ctx:MPParser.Para_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#listpara.
    def visitListpara(self, ctx:MPParser.ListparaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#return_type.
    def visitReturn_type(self, ctx:MPParser.Return_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#compound_stt.
    def visitCompound_stt(self, ctx:MPParser.Compound_sttContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#liststt.
    def visitListstt(self, ctx:MPParser.ListsttContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#funcall_stt.
    def visitFuncall_stt(self, ctx:MPParser.Funcall_sttContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#statements.
    def visitStatements(self, ctx:MPParser.StatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#breakstatement.
    def visitBreakstatement(self, ctx:MPParser.BreakstatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#continuestatement.
    def visitContinuestatement(self, ctx:MPParser.ContinuestatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#returnstatement.
    def visitReturnstatement(self, ctx:MPParser.ReturnstatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#assignment.
    def visitAssignment(self, ctx:MPParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#idassign.
    def visitIdassign(self, ctx:MPParser.IdassignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#ifstatement.
    def visitIfstatement(self, ctx:MPParser.IfstatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#ifnostatement.
    def visitIfnostatement(self, ctx:MPParser.IfnostatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#whilestatement.
    def visitWhilestatement(self, ctx:MPParser.WhilestatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#forstatement.
    def visitForstatement(self, ctx:MPParser.ForstatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#typefor.
    def visitTypefor(self, ctx:MPParser.TypeforContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#identifier.
    def visitIdentifier(self, ctx:MPParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#withstatement.
    def visitWithstatement(self, ctx:MPParser.WithstatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#list_var_dec.
    def visitList_var_dec(self, ctx:MPParser.List_var_decContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#orelse.
    def visitOrelse(self, ctx:MPParser.OrelseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#andthen.
    def visitAndthen(self, ctx:MPParser.AndthenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#exp.
    def visitExp(self, ctx:MPParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#exp1.
    def visitExp1(self, ctx:MPParser.Exp1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#op1.
    def visitOp1(self, ctx:MPParser.Op1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#exp2.
    def visitExp2(self, ctx:MPParser.Exp2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#exp3.
    def visitExp3(self, ctx:MPParser.Exp3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#exp4.
    def visitExp4(self, ctx:MPParser.Exp4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#unary.
    def visitUnary(self, ctx:MPParser.UnaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#indexexp.
    def visitIndexexp(self, ctx:MPParser.IndexexpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MPParser#literal.
    def visitLiteral(self, ctx:MPParser.LiteralContext):
        return self.visitChildren(ctx)



del MPParser