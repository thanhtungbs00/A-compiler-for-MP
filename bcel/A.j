;; Produced by JasminVisitor (BCEL)
;; http://bcel.sourceforge.net/
;; Sat Dec 01 04:06:36 ICT 2018

.source A.java
.class public A
.super java/lang/Object

.field static x I
.field static a Z

.method public <init>()V
.limit stack 1
.limit locals 1
.var 0 is this LA; from Label0 to Label1

Label0:
.line 1
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return

.end method

.method public static main()V
.limit stack 2
.limit locals 0

.line 5
	iconst_1
	putstatic A.a Z
.line 6
	getstatic java.lang.System.out Ljava/io/PrintStream;
	getstatic A.a Z
	invokevirtual java/io/PrintStream/print(Z)V
.line 7
	return

.end method
