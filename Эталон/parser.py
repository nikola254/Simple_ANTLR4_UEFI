#yourGrammarNameParser.py
from testLexer import testLexer
from testListener import testListener
from testParser import testParser
from antlr4 import *
import sys
class yourGrammarNameParser(object):
    """
    Debugger class - accepts a single input script and processes
    all subsequent requirements
    """
def __init__(self): # this method creates the class object.
    pass
#function used to parse an input file
def parse(code):
    if len(sys.argv) > 1:
        input = FileStream(code) #read the first argument as a filestream
        lexer = testLexer(input) #call your lexer
        stream = CommonTokenStream(lexer)
        parser = testParser(stream)
        tree = parser.start() #start from the parser rule, however should be changed to yourentry rule for your specific grammar.
        printer = testListener(tree,input)
        walker = ParseTreeWalker()
        walker.walk(printer, tree)
    else:
        print('Error : Expected a valid file')
        