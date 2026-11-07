from Tokens import TokenTypes
from Lexer import Lexer, Token


class Unary(object):
    def __init__(self, operator, operand):
        self.operator = operator
        self.operand = operand
        
    def __repr__(self):
        return f"Unary({self.operator}, {self.operand})"
        

class BinOp(object):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right
        
    def __repr__(self):
        return f"Node({self.left}, {self.op}, {self.right})"
        

class Num(object):
    def __init__(self, value):
        self.value = value
        
    def __repr__(self):
        return f"Num({self.value})"
        

class Parser(object):
    def __init__(self, tokenlist):
        self.tokenlist = tokenlist
        self.pos = -1
        self.advance()
        
        
    def advance(self):
        self.pos += 1
        
        if self.pos < len(self.tokenlist):
            self.current_token = self.tokenlist[self.pos]
        else:
            self.current_token = None
        return self.current_token
        
        
    def factor(self):
        token = self.current_token
        
        if token.type in (TokenTypes.INTEGER, TokenTypes.FLOAT):
            self.advance()
            return Num(token.value)
        elif token.type == TokenTypes.LPAREN:
            self.advance()
            result = self.expression()
            if self.current_token.type == TokenTypes.RPAREN:
                self.advance()
                return result
            else:
                #error
                print("Error, expected ')'")
                
        
    def unary(self):
        token = self.current_token
            
        if self.current_token.type == TokenTypes.MINUS:
            unary_op = self.current_token
            self.advance()
            result = self.unary()
            return Unary(unary_op, result)
        else:
            return self.factor()
            
            
    def term(self):
        return self.BinaryOp(self.unary, (TokenTypes.STAR, TokenTypes.SLASH))
        
        
    def expression(self):
        return self.BinaryOp(self.term, (TokenTypes.PLUS, TokenTypes.MINUS))
        
        
    def BinaryOp(self, func, ops):
        left = func()
        
        if self.current_token is not None:
            while self.current_token.type in ops:
                op_token = self.current_token
                self.advance()
                right = func()
                left = BinOp(left, op_token, right)
        else:
            pass
            
        return left
        
        
    def parse(self):
        res = self.expression()
        return res
                
                
        
        
        
        
if __name__ == "__main__":
    while True:       
        text = input(">> ")
        
        if text == "exit":
            break
            
        parser = Parser(Lexer(text).tokenize())
        ast = parser.parse()
        
        print(ast)