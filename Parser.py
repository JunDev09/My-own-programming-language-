from Tokens import TokenTypes
from Lexer import Lexer, Token

class BinOp(object):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right
        

class Num(object):
    def __init__(self, value):
        self.value = value
        
    def __repr__(self):
        return f"Num({self.value})"
        
        
if __name__ == "__main__":
    while True:
        text = input(">> ")
        
        if text == "exit":
            break
        
        print(Lexer(text).tokenize())
        print(Num(Lexer(text).tokenize()))