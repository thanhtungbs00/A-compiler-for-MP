# Generated from main/mp/parser/MP.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2@")
        buf.write("\u024c\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\4U\t")
        buf.write("U\4V\tV\4W\tW\4X\tX\4Y\tY\4Z\tZ\4[\t[\4\\\t\\\4]\t]\3")
        buf.write("\2\3\2\3\2\3\2\7\2\u00c0\n\2\f\2\16\2\u00c3\13\2\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\3\3\3\7\3\u00cc\n\3\f\3\16\3\u00cf\13")
        buf.write("\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\7\4\u00d9\n\4\f\4\16")
        buf.write("\4\u00dc\13\4\3\4\3\4\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\r\3\r")
        buf.write("\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3")
        buf.write("\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34")
        buf.write("\3\34\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\37\3\37\3\37")
        buf.write("\3\37\3 \3 \3 \3 \3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3#\3")
        buf.write("#\3#\3#\3#\3#\3$\3$\3%\3%\5%\u018a\n%\3&\3&\3&\7&\u018f")
        buf.write("\n&\f&\16&\u0192\13&\3&\5&\u0195\n&\3&\3&\3&\5&\u019a")
        buf.write("\n&\3&\3&\3&\5&\u019f\n&\3\'\6\'\u01a2\n\'\r\'\16\'\u01a3")
        buf.write("\3(\3(\5(\u01a8\n(\3(\6(\u01ab\n(\r(\16(\u01ac\3)\3)\3")
        buf.write(")\7)\u01b2\n)\f)\16)\u01b5\13)\3)\3)\3)\3*\3*\3+\3+\3")
        buf.write(",\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\61\3\62\6")
        buf.write("\62\u01cc\n\62\r\62\16\62\u01cd\3\62\3\62\3\63\3\63\3")
        buf.write("\63\3\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67\38\38\38\3")
        buf.write("9\39\3:\3:\3;\3;\3<\3<\3<\3=\3=\3=\3>\3>\7>\u01ee\n>\f")
        buf.write(">\16>\u01f1\13>\3?\3?\3@\3@\3A\3A\3B\3B\3C\3C\3D\3D\3")
        buf.write("E\3E\3F\3F\3G\3G\3H\3H\3I\3I\3J\3J\3K\3K\3L\3L\3M\3M\3")
        buf.write("N\3N\3O\3O\3P\3P\3Q\3Q\3R\3R\3S\3S\3T\3T\3U\3U\3V\3V\3")
        buf.write("W\3W\3X\3X\3Y\3Y\3Y\3Z\3Z\3Z\3[\3[\3[\3\\\3\\\3\\\7\\")
        buf.write("\u0233\n\\\f\\\16\\\u0236\13\\\3\\\3\\\3\\\3\\\3\\\3]")
        buf.write("\3]\3]\3]\3]\3]\7]\u0243\n]\f]\16]\u0246\13]\3]\5]\u0249")
        buf.write("\n]\3]\3]\5\u00c1\u00cd\u0234\2^\3\3\5\4\7\5\t\6\13\7")
        buf.write("\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21")
        buf.write("!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67")
        buf.write("\359\36;\37= ?!A\"C#E$G%I&K\'M\2O\2Q(S)U*W+Y,[-]._/a\60")
        buf.write("c\61e\62g\63i\64k\65m\66o\67q8s9u:w;y<{=}\2\177\2\u0081")
        buf.write("\2\u0083\2\u0085\2\u0087\2\u0089\2\u008b\2\u008d\2\u008f")
        buf.write("\2\u0091\2\u0093\2\u0095\2\u0097\2\u0099\2\u009b\2\u009d")
        buf.write("\2\u009f\2\u00a1\2\u00a3\2\u00a5\2\u00a7\2\u00a9\2\u00ab")
        buf.write("\2\u00ad\2\u00af\2\u00b1\2\u00b3\2\u00b5>\u00b7?\u00b9")
        buf.write("@\3\2\'\4\2\f\f\17\17\3\2\62;\4\2GGgg\b\2\f\f\17\17$$")
        buf.write("GHQQ^^\5\2\13\f\16\17\"\"\5\2C\\aac|\6\2\62;C\\aac|\4")
        buf.write("\2CCcc\4\2DDdd\4\2EEee\4\2FFff\4\2HHhh\4\2IIii\4\2JJj")
        buf.write("j\4\2KKkk\4\2LLll\4\2MMmm\4\2NNnn\4\2OOoo\4\2PPpp\4\2")
        buf.write("QQqq\4\2RRrr\4\2SSss\4\2TTtt\4\2UUuu\4\2VVvv\4\2WWww\4")
        buf.write("\2XXxx\4\2YYyy\4\2ZZzz\4\2[[{{\4\2\\\\||\n\2$$))^^ddh")
        buf.write("hppttvv\4\2$$^^\3\2^^\5\2\f\f\17\17$$\3\3\f\f\2\u0242")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2")
        buf.write("\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2")
        buf.write("%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2")
        buf.write("\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2")
        buf.write("\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3")
        buf.write("\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u")
        buf.write("\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2\u00b5\3\2")
        buf.write("\2\2\2\u00b7\3\2\2\2\2\u00b9\3\2\2\2\3\u00bb\3\2\2\2\5")
        buf.write("\u00c9\3\2\2\2\7\u00d4\3\2\2\2\t\u00df\3\2\2\2\13\u00e2")
        buf.write("\3\2\2\2\r\u00e8\3\2\2\2\17\u00ec\3\2\2\2\21\u00f6\3\2")
        buf.write("\2\2\23\u00ff\3\2\2\2\25\u0102\3\2\2\2\27\u0107\3\2\2")
        buf.write("\2\31\u010c\3\2\2\2\33\u0112\3\2\2\2\35\u0115\3\2\2\2")
        buf.write("\37\u0119\3\2\2\2!\u011c\3\2\2\2#\u0123\3\2\2\2%\u0129")
        buf.write("\3\2\2\2\'\u0132\3\2\2\2)\u0139\3\2\2\2+\u013e\3\2\2\2")
        buf.write("-\u0142\3\2\2\2/\u014a\3\2\2\2\61\u0152\3\2\2\2\63\u0157")
        buf.write("\3\2\2\2\65\u015e\3\2\2\2\67\u0164\3\2\2\29\u0167\3\2")
        buf.write("\2\2;\u016b\3\2\2\2=\u016e\3\2\2\2?\u0172\3\2\2\2A\u0176")
        buf.write("\3\2\2\2C\u017a\3\2\2\2E\u017f\3\2\2\2G\u0185\3\2\2\2")
        buf.write("I\u0189\3\2\2\2K\u019e\3\2\2\2M\u01a1\3\2\2\2O\u01a5\3")
        buf.write("\2\2\2Q\u01ae\3\2\2\2S\u01b9\3\2\2\2U\u01bb\3\2\2\2W\u01bd")
        buf.write("\3\2\2\2Y\u01bf\3\2\2\2[\u01c1\3\2\2\2]\u01c3\3\2\2\2")
        buf.write("_\u01c5\3\2\2\2a\u01c7\3\2\2\2c\u01cb\3\2\2\2e\u01d1\3")
        buf.write("\2\2\2g\u01d4\3\2\2\2i\u01d6\3\2\2\2k\u01d8\3\2\2\2m\u01da")
        buf.write("\3\2\2\2o\u01dc\3\2\2\2q\u01df\3\2\2\2s\u01e1\3\2\2\2")
        buf.write("u\u01e3\3\2\2\2w\u01e5\3\2\2\2y\u01e8\3\2\2\2{\u01eb\3")
        buf.write("\2\2\2}\u01f2\3\2\2\2\177\u01f4\3\2\2\2\u0081\u01f6\3")
        buf.write("\2\2\2\u0083\u01f8\3\2\2\2\u0085\u01fa\3\2\2\2\u0087\u01fc")
        buf.write("\3\2\2\2\u0089\u01fe\3\2\2\2\u008b\u0200\3\2\2\2\u008d")
        buf.write("\u0202\3\2\2\2\u008f\u0204\3\2\2\2\u0091\u0206\3\2\2\2")
        buf.write("\u0093\u0208\3\2\2\2\u0095\u020a\3\2\2\2\u0097\u020c\3")
        buf.write("\2\2\2\u0099\u020e\3\2\2\2\u009b\u0210\3\2\2\2\u009d\u0212")
        buf.write("\3\2\2\2\u009f\u0214\3\2\2\2\u00a1\u0216\3\2\2\2\u00a3")
        buf.write("\u0218\3\2\2\2\u00a5\u021a\3\2\2\2\u00a7\u021c\3\2\2\2")
        buf.write("\u00a9\u021e\3\2\2\2\u00ab\u0220\3\2\2\2\u00ad\u0222\3")
        buf.write("\2\2\2\u00af\u0224\3\2\2\2\u00b1\u0226\3\2\2\2\u00b3\u0229")
        buf.write("\3\2\2\2\u00b5\u022c\3\2\2\2\u00b7\u022f\3\2\2\2\u00b9")
        buf.write("\u023c\3\2\2\2\u00bb\u00bc\7*\2\2\u00bc\u00bd\7,\2\2\u00bd")
        buf.write("\u00c1\3\2\2\2\u00be\u00c0\13\2\2\2\u00bf\u00be\3\2\2")
        buf.write("\2\u00c0\u00c3\3\2\2\2\u00c1\u00c2\3\2\2\2\u00c1\u00bf")
        buf.write("\3\2\2\2\u00c2\u00c4\3\2\2\2\u00c3\u00c1\3\2\2\2\u00c4")
        buf.write("\u00c5\7,\2\2\u00c5\u00c6\7+\2\2\u00c6\u00c7\3\2\2\2\u00c7")
        buf.write("\u00c8\b\2\2\2\u00c8\4\3\2\2\2\u00c9\u00cd\7}\2\2\u00ca")
        buf.write("\u00cc\13\2\2\2\u00cb\u00ca\3\2\2\2\u00cc\u00cf\3\2\2")
        buf.write("\2\u00cd\u00ce\3\2\2\2\u00cd\u00cb\3\2\2\2\u00ce\u00d0")
        buf.write("\3\2\2\2\u00cf\u00cd\3\2\2\2\u00d0\u00d1\7\177\2\2\u00d1")
        buf.write("\u00d2\3\2\2\2\u00d2\u00d3\b\3\2\2\u00d3\6\3\2\2\2\u00d4")
        buf.write("\u00d5\7\61\2\2\u00d5\u00d6\7\61\2\2\u00d6\u00da\3\2\2")
        buf.write("\2\u00d7\u00d9\n\2\2\2\u00d8\u00d7\3\2\2\2\u00d9\u00dc")
        buf.write("\3\2\2\2\u00da\u00d8\3\2\2\2\u00da\u00db\3\2\2\2\u00db")
        buf.write("\u00dd\3\2\2\2\u00dc\u00da\3\2\2\2\u00dd\u00de\b\4\2\2")
        buf.write("\u00de\b\3\2\2\2\u00df\u00e0\5\u0097L\2\u00e0\u00e1\5")
        buf.write("\u0099M\2\u00e1\n\3\2\2\2\u00e2\u00e3\5\177@\2\u00e3\u00e4")
        buf.write("\5\u0085C\2\u00e4\u00e5\5\u0089E\2\u00e5\u00e6\5\u008d")
        buf.write("G\2\u00e6\u00e7\5\u0097L\2\u00e7\f\3\2\2\2\u00e8\u00e9")
        buf.write("\5\u0085C\2\u00e9\u00ea\5\u0097L\2\u00ea\u00eb\5\u0083")
        buf.write("B\2\u00eb\16\3\2\2\2\u00ec\u00ed\5\u009bN\2\u00ed\u00ee")
        buf.write("\5\u009fP\2\u00ee\u00ef\5\u0099M\2\u00ef\u00f0\5\u0081")
        buf.write("A\2\u00f0\u00f1\5\u0085C\2\u00f1\u00f2\5\u0083B\2\u00f2")
        buf.write("\u00f3\5\u00a5S\2\u00f3\u00f4\5\u009fP\2\u00f4\u00f5\5")
        buf.write("\u0085C\2\u00f5\20\3\2\2\2\u00f6\u00f7\5\u0087D\2\u00f7")
        buf.write("\u00f8\5\u00a5S\2\u00f8\u00f9\5\u0097L\2\u00f9\u00fa\5")
        buf.write("\u0081A\2\u00fa\u00fb\5\u00a3R\2\u00fb\u00fc\5\u008dG")
        buf.write("\2\u00fc\u00fd\5\u0099M\2\u00fd\u00fe\5\u0097L\2\u00fe")
        buf.write("\22\3\2\2\2\u00ff\u0100\5\u008dG\2\u0100\u0101\5\u0087")
        buf.write("D\2\u0101\24\3\2\2\2\u0102\u0103\5\u00a3R\2\u0103\u0104")
        buf.write("\5\u008bF\2\u0104\u0105\5\u0085C\2\u0105\u0106\5\u0097")
        buf.write("L\2\u0106\26\3\2\2\2\u0107\u0108\5\u0085C\2\u0108\u0109")
        buf.write("\5\u0093J\2\u0109\u010a\5\u00a1Q\2\u010a\u010b\5\u0085")
        buf.write("C\2\u010b\30\3\2\2\2\u010c\u010d\5\u00a9U\2\u010d\u010e")
        buf.write("\5\u008bF\2\u010e\u010f\5\u008dG\2\u010f\u0110\5\u0093")
        buf.write("J\2\u0110\u0111\5\u0085C\2\u0111\32\3\2\2\2\u0112\u0113")
        buf.write("\5\u0083B\2\u0113\u0114\5\u0099M\2\u0114\34\3\2\2\2\u0115")
        buf.write("\u0116\5\u0087D\2\u0116\u0117\5\u0099M\2\u0117\u0118\5")
        buf.write("\u009fP\2\u0118\36\3\2\2\2\u0119\u011a\5\u00a3R\2\u011a")
        buf.write("\u011b\5\u0099M\2\u011b \3\2\2\2\u011c\u011d\5\u0083B")
        buf.write("\2\u011d\u011e\5\u0099M\2\u011e\u011f\5\u00a9U\2\u011f")
        buf.write("\u0120\5\u0097L\2\u0120\u0121\5\u00a3R\2\u0121\u0122\5")
        buf.write("\u0099M\2\u0122\"\3\2\2\2\u0123\u0124\5\177@\2\u0124\u0125")
        buf.write("\5\u009fP\2\u0125\u0126\5\u0085C\2\u0126\u0127\5}?\2\u0127")
        buf.write("\u0128\5\u0091I\2\u0128$\3\2\2\2\u0129\u012a\5\u0081A")
        buf.write("\2\u012a\u012b\5\u0099M\2\u012b\u012c\5\u0097L\2\u012c")
        buf.write("\u012d\5\u00a3R\2\u012d\u012e\5\u008dG\2\u012e\u012f\5")
        buf.write("\u0097L\2\u012f\u0130\5\u00a5S\2\u0130\u0131\5\u0085C")
        buf.write("\2\u0131&\3\2\2\2\u0132\u0133\5\u009fP\2\u0133\u0134\5")
        buf.write("\u0085C\2\u0134\u0135\5\u00a3R\2\u0135\u0136\5\u00a5S")
        buf.write("\2\u0136\u0137\5\u009fP\2\u0137\u0138\5\u0097L\2\u0138")
        buf.write("(\3\2\2\2\u0139\u013a\5\u00a9U\2\u013a\u013b\5\u008dG")
        buf.write("\2\u013b\u013c\5\u00a3R\2\u013c\u013d\5\u008bF\2\u013d")
        buf.write("*\3\2\2\2\u013e\u013f\5\u00a7T\2\u013f\u0140\5}?\2\u0140")
        buf.write("\u0141\5\u009fP\2\u0141,\3\2\2\2\u0142\u0143\5\177@\2")
        buf.write("\u0143\u0144\5\u0099M\2\u0144\u0145\5\u0099M\2\u0145\u0146")
        buf.write("\5\u0093J\2\u0146\u0147\5\u0085C\2\u0147\u0148\5}?\2\u0148")
        buf.write("\u0149\5\u0097L\2\u0149.\3\2\2\2\u014a\u014b\5\u008dG")
        buf.write("\2\u014b\u014c\5\u0097L\2\u014c\u014d\5\u00a3R\2\u014d")
        buf.write("\u014e\5\u0085C\2\u014e\u014f\5\u0089E\2\u014f\u0150\5")
        buf.write("\u0085C\2\u0150\u0151\5\u009fP\2\u0151\60\3\2\2\2\u0152")
        buf.write("\u0153\5\u009fP\2\u0153\u0154\5\u0085C\2\u0154\u0155\5")
        buf.write("}?\2\u0155\u0156\5\u0093J\2\u0156\62\3\2\2\2\u0157\u0158")
        buf.write("\5\u00a1Q\2\u0158\u0159\5\u00a3R\2\u0159\u015a\5\u009f")
        buf.write("P\2\u015a\u015b\5\u008dG\2\u015b\u015c\5\u0097L\2\u015c")
        buf.write("\u015d\5\u0089E\2\u015d\64\3\2\2\2\u015e\u015f\5}?\2\u015f")
        buf.write("\u0160\5\u009fP\2\u0160\u0161\5\u009fP\2\u0161\u0162\5")
        buf.write("}?\2\u0162\u0163\5\u00adW\2\u0163\66\3\2\2\2\u0164\u0165")
        buf.write("\5\u0099M\2\u0165\u0166\5\u0087D\2\u01668\3\2\2\2\u0167")
        buf.write("\u0168\5\u0097L\2\u0168\u0169\5\u0099M\2\u0169\u016a\5")
        buf.write("\u00a3R\2\u016a:\3\2\2\2\u016b\u016c\5\u0099M\2\u016c")
        buf.write("\u016d\5\u009fP\2\u016d<\3\2\2\2\u016e\u016f\5}?\2\u016f")
        buf.write("\u0170\5\u0097L\2\u0170\u0171\5\u0083B\2\u0171>\3\2\2")
        buf.write("\2\u0172\u0173\5\u0083B\2\u0173\u0174\5\u008dG\2\u0174")
        buf.write("\u0175\5\u00a7T\2\u0175@\3\2\2\2\u0176\u0177\5\u0095K")
        buf.write("\2\u0177\u0178\5\u0099M\2\u0178\u0179\5\u0083B\2\u0179")
        buf.write("B\3\2\2\2\u017a\u017b\5\u00a3R\2\u017b\u017c\5\u009fP")
        buf.write("\2\u017c\u017d\5\u00a5S\2\u017d\u017e\5\u0085C\2\u017e")
        buf.write("D\3\2\2\2\u017f\u0180\5\u0087D\2\u0180\u0181\5}?\2\u0181")
        buf.write("\u0182\5\u0093J\2\u0182\u0183\5\u00a1Q\2\u0183\u0184\5")
        buf.write("\u0085C\2\u0184F\3\2\2\2\u0185\u0186\5M\'\2\u0186H\3\2")
        buf.write("\2\2\u0187\u018a\5C\"\2\u0188\u018a\5E#\2\u0189\u0187")
        buf.write("\3\2\2\2\u0189\u0188\3\2\2\2\u018aJ\3\2\2\2\u018b\u018c")
        buf.write("\5M\'\2\u018c\u0190\7\60\2\2\u018d\u018f\t\3\2\2\u018e")
        buf.write("\u018d\3\2\2\2\u018f\u0192\3\2\2\2\u0190\u018e\3\2\2\2")
        buf.write("\u0190\u0191\3\2\2\2\u0191\u0194\3\2\2\2\u0192\u0190\3")
        buf.write("\2\2\2\u0193\u0195\5O(\2\u0194\u0193\3\2\2\2\u0194\u0195")
        buf.write("\3\2\2\2\u0195\u019f\3\2\2\2\u0196\u0197\7\60\2\2\u0197")
        buf.write("\u0199\5M\'\2\u0198\u019a\5O(\2\u0199\u0198\3\2\2\2\u0199")
        buf.write("\u019a\3\2\2\2\u019a\u019f\3\2\2\2\u019b\u019c\5M\'\2")
        buf.write("\u019c\u019d\5O(\2\u019d\u019f\3\2\2\2\u019e\u018b\3\2")
        buf.write("\2\2\u019e\u0196\3\2\2\2\u019e\u019b\3\2\2\2\u019fL\3")
        buf.write("\2\2\2\u01a0\u01a2\t\3\2\2\u01a1\u01a0\3\2\2\2\u01a2\u01a3")
        buf.write("\3\2\2\2\u01a3\u01a1\3\2\2\2\u01a3\u01a4\3\2\2\2\u01a4")
        buf.write("N\3\2\2\2\u01a5\u01a7\t\4\2\2\u01a6\u01a8\7/\2\2\u01a7")
        buf.write("\u01a6\3\2\2\2\u01a7\u01a8\3\2\2\2\u01a8\u01aa\3\2\2\2")
        buf.write("\u01a9\u01ab\t\3\2\2\u01aa\u01a9\3\2\2\2\u01ab\u01ac\3")
        buf.write("\2\2\2\u01ac\u01aa\3\2\2\2\u01ac\u01ad\3\2\2\2\u01adP")
        buf.write("\3\2\2\2\u01ae\u01b3\7$\2\2\u01af\u01b2\5\u00b1Y\2\u01b0")
        buf.write("\u01b2\n\5\2\2\u01b1\u01af\3\2\2\2\u01b1\u01b0\3\2\2\2")
        buf.write("\u01b2\u01b5\3\2\2\2\u01b3\u01b1\3\2\2\2\u01b3\u01b4\3")
        buf.write("\2\2\2\u01b4\u01b6\3\2\2\2\u01b5\u01b3\3\2\2\2\u01b6\u01b7")
        buf.write("\7$\2\2\u01b7\u01b8\b)\3\2\u01b8R\3\2\2\2\u01b9\u01ba")
        buf.write("\7]\2\2\u01baT\3\2\2\2\u01bb\u01bc\7_\2\2\u01bcV\3\2\2")
        buf.write("\2\u01bd\u01be\7*\2\2\u01beX\3\2\2\2\u01bf\u01c0\7+\2")
        buf.write("\2\u01c0Z\3\2\2\2\u01c1\u01c2\7=\2\2\u01c2\\\3\2\2\2\u01c3")
        buf.write("\u01c4\7.\2\2\u01c4^\3\2\2\2\u01c5\u01c6\7<\2\2\u01c6")
        buf.write("`\3\2\2\2\u01c7\u01c8\7\60\2\2\u01c8\u01c9\7\60\2\2\u01c9")
        buf.write("b\3\2\2\2\u01ca\u01cc\t\6\2\2\u01cb\u01ca\3\2\2\2\u01cc")
        buf.write("\u01cd\3\2\2\2\u01cd\u01cb\3\2\2\2\u01cd\u01ce\3\2\2\2")
        buf.write("\u01ce\u01cf\3\2\2\2\u01cf\u01d0\b\62\2\2\u01d0d\3\2\2")
        buf.write("\2\u01d1\u01d2\7<\2\2\u01d2\u01d3\7?\2\2\u01d3f\3\2\2")
        buf.write("\2\u01d4\u01d5\7-\2\2\u01d5h\3\2\2\2\u01d6\u01d7\7,\2")
        buf.write("\2\u01d7j\3\2\2\2\u01d8\u01d9\7/\2\2\u01d9l\3\2\2\2\u01da")
        buf.write("\u01db\7\61\2\2\u01dbn\3\2\2\2\u01dc\u01dd\7>\2\2\u01dd")
        buf.write("\u01de\7@\2\2\u01dep\3\2\2\2\u01df\u01e0\7?\2\2\u01e0")
        buf.write("r\3\2\2\2\u01e1\u01e2\7>\2\2\u01e2t\3\2\2\2\u01e3\u01e4")
        buf.write("\7@\2\2\u01e4v\3\2\2\2\u01e5\u01e6\7>\2\2\u01e6\u01e7")
        buf.write("\7?\2\2\u01e7x\3\2\2\2\u01e8\u01e9\7@\2\2\u01e9\u01ea")
        buf.write("\7?\2\2\u01eaz\3\2\2\2\u01eb\u01ef\t\7\2\2\u01ec\u01ee")
        buf.write("\t\b\2\2\u01ed\u01ec\3\2\2\2\u01ee\u01f1\3\2\2\2\u01ef")
        buf.write("\u01ed\3\2\2\2\u01ef\u01f0\3\2\2\2\u01f0|\3\2\2\2\u01f1")
        buf.write("\u01ef\3\2\2\2\u01f2\u01f3\t\t\2\2\u01f3~\3\2\2\2\u01f4")
        buf.write("\u01f5\t\n\2\2\u01f5\u0080\3\2\2\2\u01f6\u01f7\t\13\2")
        buf.write("\2\u01f7\u0082\3\2\2\2\u01f8\u01f9\t\f\2\2\u01f9\u0084")
        buf.write("\3\2\2\2\u01fa\u01fb\t\4\2\2\u01fb\u0086\3\2\2\2\u01fc")
        buf.write("\u01fd\t\r\2\2\u01fd\u0088\3\2\2\2\u01fe\u01ff\t\16\2")
        buf.write("\2\u01ff\u008a\3\2\2\2\u0200\u0201\t\17\2\2\u0201\u008c")
        buf.write("\3\2\2\2\u0202\u0203\t\20\2\2\u0203\u008e\3\2\2\2\u0204")
        buf.write("\u0205\t\21\2\2\u0205\u0090\3\2\2\2\u0206\u0207\t\22\2")
        buf.write("\2\u0207\u0092\3\2\2\2\u0208\u0209\t\23\2\2\u0209\u0094")
        buf.write("\3\2\2\2\u020a\u020b\t\24\2\2\u020b\u0096\3\2\2\2\u020c")
        buf.write("\u020d\t\25\2\2\u020d\u0098\3\2\2\2\u020e\u020f\t\26\2")
        buf.write("\2\u020f\u009a\3\2\2\2\u0210\u0211\t\27\2\2\u0211\u009c")
        buf.write("\3\2\2\2\u0212\u0213\t\30\2\2\u0213\u009e\3\2\2\2\u0214")
        buf.write("\u0215\t\31\2\2\u0215\u00a0\3\2\2\2\u0216\u0217\t\32\2")
        buf.write("\2\u0217\u00a2\3\2\2\2\u0218\u0219\t\33\2\2\u0219\u00a4")
        buf.write("\3\2\2\2\u021a\u021b\t\34\2\2\u021b\u00a6\3\2\2\2\u021c")
        buf.write("\u021d\t\35\2\2\u021d\u00a8\3\2\2\2\u021e\u021f\t\36\2")
        buf.write("\2\u021f\u00aa\3\2\2\2\u0220\u0221\t\37\2\2\u0221\u00ac")
        buf.write("\3\2\2\2\u0222\u0223\t \2\2\u0223\u00ae\3\2\2\2\u0224")
        buf.write("\u0225\t!\2\2\u0225\u00b0\3\2\2\2\u0226\u0227\7^\2\2\u0227")
        buf.write("\u0228\t\"\2\2\u0228\u00b2\3\2\2\2\u0229\u022a\7^\2\2")
        buf.write("\u022a\u022b\n\"\2\2\u022b\u00b4\3\2\2\2\u022c\u022d\13")
        buf.write("\2\2\2\u022d\u022e\b[\4\2\u022e\u00b6\3\2\2\2\u022f\u0234")
        buf.write("\7$\2\2\u0230\u0233\5\u00b1Y\2\u0231\u0233\n#\2\2\u0232")
        buf.write("\u0230\3\2\2\2\u0232\u0231\3\2\2\2\u0233\u0236\3\2\2\2")
        buf.write("\u0234\u0235\3\2\2\2\u0234\u0232\3\2\2\2\u0235\u0237\3")
        buf.write("\2\2\2\u0236\u0234\3\2\2\2\u0237\u0238\t$\2\2\u0238\u0239")
        buf.write("\n\"\2\2\u0239\u023a\3\2\2\2\u023a\u023b\b\\\5\2\u023b")
        buf.write("\u00b8\3\2\2\2\u023c\u0244\7$\2\2\u023d\u0243\5\u00b1")
        buf.write("Y\2\u023e\u0243\n%\2\2\u023f\u0240\n$\2\2\u0240\u0241")
        buf.write("\7^\2\2\u0241\u0243\7$\2\2\u0242\u023d\3\2\2\2\u0242\u023e")
        buf.write("\3\2\2\2\u0242\u023f\3\2\2\2\u0243\u0246\3\2\2\2\u0244")
        buf.write("\u0242\3\2\2\2\u0244\u0245\3\2\2\2\u0245\u0248\3\2\2\2")
        buf.write("\u0246\u0244\3\2\2\2\u0247\u0249\t&\2\2\u0248\u0247\3")
        buf.write("\2\2\2\u0249\u024a\3\2\2\2\u024a\u024b\b]\6\2\u024b\u00ba")
        buf.write("\3\2\2\2\27\2\u00c1\u00cd\u00da\u0189\u0190\u0194\u0199")
        buf.write("\u019e\u01a3\u01a7\u01ac\u01b1\u01b3\u01cd\u01ef\u0232")
        buf.write("\u0234\u0242\u0244\u0248\7\b\2\2\3)\2\3[\3\3\\\4\3]\5")
        return buf.getvalue()


class MPLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    TRADITIONAL_CMT = 1
    BLOCK_CMT = 2
    LINE_CMT = 3
    NO = 4
    BEGIN = 5
    END = 6
    PROCEDURE = 7
    FUNCTION = 8
    IF = 9
    THEN = 10
    ELSE = 11
    WHILE = 12
    DO = 13
    FOR = 14
    TO = 15
    DOWNTO = 16
    BREAK = 17
    CONTINUE = 18
    RETURN = 19
    WITH = 20
    VAR = 21
    BOOLEANTYPE = 22
    INTTYPE = 23
    REALTYPE = 24
    STRINGTYPE = 25
    ARRAY = 26
    OF = 27
    NOT = 28
    OR = 29
    AND = 30
    DIV = 31
    MOD = 32
    TRUE = 33
    FALSE = 34
    INTLIT = 35
    BOOLLIT = 36
    REALLIT = 37
    STRINGLIT = 38
    LSB = 39
    RSB = 40
    LB = 41
    RB = 42
    SEMI = 43
    COMMA = 44
    COLON = 45
    DD = 46
    WS = 47
    ASSIGN = 48
    ADDOP = 49
    MULOP = 50
    SUBOP = 51
    DIVOP = 52
    NEQ = 53
    EQ = 54
    LT = 55
    GT = 56
    LTE = 57
    GTE = 58
    ID = 59
    ERROR_CHAR = 60
    ILLEGAL_ESCAPE = 61
    UNCLOSE_STRING = 62

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'['", "']'", "'('", "')'", "';'", "','", "':'", "'..'", "':='", 
            "'+'", "'*'", "'-'", "'/'", "'<>'", "'='", "'<'", "'>'", "'<='", 
            "'>='" ]

    symbolicNames = [ "<INVALID>",
            "TRADITIONAL_CMT", "BLOCK_CMT", "LINE_CMT", "NO", "BEGIN", "END", 
            "PROCEDURE", "FUNCTION", "IF", "THEN", "ELSE", "WHILE", "DO", 
            "FOR", "TO", "DOWNTO", "BREAK", "CONTINUE", "RETURN", "WITH", 
            "VAR", "BOOLEANTYPE", "INTTYPE", "REALTYPE", "STRINGTYPE", "ARRAY", 
            "OF", "NOT", "OR", "AND", "DIV", "MOD", "TRUE", "FALSE", "INTLIT", 
            "BOOLLIT", "REALLIT", "STRINGLIT", "LSB", "RSB", "LB", "RB", 
            "SEMI", "COMMA", "COLON", "DD", "WS", "ASSIGN", "ADDOP", "MULOP", 
            "SUBOP", "DIVOP", "NEQ", "EQ", "LT", "GT", "LTE", "GTE", "ID", 
            "ERROR_CHAR", "ILLEGAL_ESCAPE", "UNCLOSE_STRING" ]

    ruleNames = [ "TRADITIONAL_CMT", "BLOCK_CMT", "LINE_CMT", "NO", "BEGIN", 
                  "END", "PROCEDURE", "FUNCTION", "IF", "THEN", "ELSE", 
                  "WHILE", "DO", "FOR", "TO", "DOWNTO", "BREAK", "CONTINUE", 
                  "RETURN", "WITH", "VAR", "BOOLEANTYPE", "INTTYPE", "REALTYPE", 
                  "STRINGTYPE", "ARRAY", "OF", "NOT", "OR", "AND", "DIV", 
                  "MOD", "TRUE", "FALSE", "INTLIT", "BOOLLIT", "REALLIT", 
                  "DIGIT", "EXPONENT", "STRINGLIT", "LSB", "RSB", "LB", 
                  "RB", "SEMI", "COMMA", "COLON", "DD", "WS", "ASSIGN", 
                  "ADDOP", "MULOP", "SUBOP", "DIVOP", "NEQ", "EQ", "LT", 
                  "GT", "LTE", "GTE", "ID", "A", "B", "C", "D", "E", "F", 
                  "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", 
                  "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "ESC", "IESC", 
                  "ERROR_CHAR", "ILLEGAL_ESCAPE", "UNCLOSE_STRING" ]

    grammarFileName = "MP.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[39] = self.STRINGLIT_action 
            actions[89] = self.ERROR_CHAR_action 
            actions[90] = self.ILLEGAL_ESCAPE_action 
            actions[91] = self.UNCLOSE_STRING_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))

    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                        s=self.text[1:-1]
                        self.text=s
                    
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
             
                        raise ErrorToken(self.text) 
                    
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                       raise IllegalEscape(self.text[1:])
                    
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

                        if self.text[-1]=='\n':
                            raise UncloseString(self.text[1:-1])
                        else:
                            raise UncloseString(self.text[1:])
                    
     


