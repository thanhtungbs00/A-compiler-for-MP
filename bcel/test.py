export ANTLR_LIB=./Downloads/antlr-4.7.1-complete.jar

import os,sys,subprocess

ANTLR_JAR = os.environ.get('ANTLR_LIB')

print(ANTLR_JAR)

subprocess.run(["java","-jar",ANTLR_JAR,"-o","../target","-no-listener","-visitor","./Desktop/initial/initial/src/main/mp/parser/MP.g4"])

from antlr4 import *


sudo apt install virtualenv
javac -cp bcel-5.2/bcel-5.2.jar  JasminVisitor.java 

 javac -cp bcel-5.2/bcel-5.2.jar A.java 
java -cp .:bcel-5.2/bcel-5.2.jar JasminVisitor A

