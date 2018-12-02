# A-compiler-for-MP
assignment PPL
BTL xây dựng chương trình dịch cho ngôn ngữ MP:
+ Cách chạy
- Download antlr :https://www.antlr.org/
- Xét biến môi trường :
    + Mở terminal : nano ~/.bashrc
    + add vào cuối :  export ANTLR_LIB=/usr/local/lib/antlr-4.7.1-complete.jar
- Chạy chương trình :
    + python3 run.py gen
    + python3 run.py test LexerSuite
    + python3 run.py test ParserSuite
    + python3 run.py test CheckerSuite
    + python3 run.py test CodeGenSuite
