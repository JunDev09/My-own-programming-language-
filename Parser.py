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
        

class Assignment(object):
    def __init__(self, name, value):
        self.name = name
        self.value = value
        
    def __repr__(self):
        return f"Name:{self.name}\nValue:{self.value}"
        

class Num(object):
    def __init__(self, value):
        self.value = value
        
    def __repr__(self):
        return f"Num({self.value})"
    

class Boolean(object):
    def __init__(self, value):
        self.value = value
        
    def __repr__(self):
        return f"Bool({self.value})"
        
class String(object):
    def __init__(self, value):
        self.value = value
        
    def __repr__(self):
        return f"String({self.value})"
        

class Identifier(object):
    def __init__(self, name):
        self.name = name
        
    def __repr__(self):
        return f"Identifier({self.name})"


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
            result = self.assignment()
            if self.current_token.type == TokenTypes.RPAREN:
                self.advance()
                return result
            else:
                #error
                print("Error, expected ')'")
                
                
        elif token.type == TokenTypes.BOOLEAN:
            self.advance()
            return Boolean(token.value)
        elif token.type == TokenTypes.STRING:
            self.advance()
            return String(token.value)
        elif token.type == TokenTypes.IDENTIFIER:
            self.advance()
            return Identifier(token.value)
                
        
    def unary(self): 
        if self.current_token.type in (TokenTypes.MINUS, TokenTypes.UNARY_NOT):
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
        
        
    def comparison(self):
        return self.BinaryOp(self.expression, (TokenTypes.EQUAL_TO, TokenTypes.NOT_EQUAL, TokenTypes.LESSER_OP, TokenTypes.GREATER_OP, TokenTypes.LESSER_EQUAL, TokenTypes.GREATER_EQUAL))
        
    
    def assignment(self):
        left = self.comparison()
        if self.current_token is None or self.current_token.type != TokenTypes.EQUAL:
            return left
        else:
            self.advance()
            right = self.assignment()
            
        return Assignment(left.name, right)
        
        
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
        res = self.assignment()
        return res
                
                
        
        
        
        
if __name__ == "__main__":
    while True:       
        text = input(">> ")
        
        if text == "exit":
            break
            
        parser = Parser(Lexer(text).tokenize())
        ast = parser.parse()
        
        print(ast)