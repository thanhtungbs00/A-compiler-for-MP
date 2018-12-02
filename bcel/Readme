Check mã trong file jasmin(.j) được sinh ra từ code java
Các bước : 
+ Compile file JasminVisitor.java --> JasminVisitor.class:
  javac -cp bcel-5.2/bcel-5.2.jar  JasminVisitor.java 
+ Create a file A.java to check code in file .j from java
+ Compile file A.java --> A.class
  javac -cp bcel-5.2/bcel-5.2.jar A.java 
+ Sinh ra file jasmin:
  java -cp .:bcel-5.2/bcel-5.2.jar JasminVisitor A
