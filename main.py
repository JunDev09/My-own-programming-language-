from Lexer.Lexer import Lexer
from Parser.Parser import Num, Unary, BinOp, Boolean, String, Identifier, Assignment, Block, ifNode, Parser
from Interpreter.Interpreter import Interpreter
from Errors.ErrorClasses import LangError

if __name__ == "__main__":
    interpreter = Interpreter()
    
    while True:
        try:
            text = input(">> ")
            if text == "exit":
                break
            if not text.strip():
                continue
                
            tokens = Lexer(text).tokenize()
            tree = Parser(tokens).parse()
            runtime = interpreter.visit_node(tree)
            print(runtime)
            
        except LangError as e:
            print(f"{e.message}")

