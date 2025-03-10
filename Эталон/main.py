#main.py
from  parser import parser
import sys
#main method and entry point of application
def main():
    """Main method calling a single debugger for an input script"""
    code = """
    int asd return
    """
    Parser = parser
    Parser.parse(code)
if __name__ == '__main__':
    main()