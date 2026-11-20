from Lexer.Tokens import TokenTypes
from Lexer.Lexer import Lexer
from Errors.ErrorClasses import Lang_SyntaxError

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
    def __init__(self, name, value, op):
        self.name = name
        self.value = value
        self.op = op
        
    def __repr__(self):
        return f"Name:{self.name}\nValue:{self.value}"
        
        
class TypeDeclaration(object):
    def __init__(self, type_name, name, value):
        self.type_name = type_name
        self.name = name
        self.value = value
        
    def __repr__(self):
        return f"TYPE: {self.type_name}, NAME: {self.name}, VALUE: {self.value}"
        

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
        
        
class Block(object):
    def __init__(self, statementlist):
        self.list = statementlist
        
    def __repr__(self):
        return f"Block({self.list})"
        

class ifNode(object):
    def __init__(self, condition, thenBody, elseBody):
        self.condition = condition
        self.thenBody = thenBody
        self.elseBody = elseBody
        
    def __repr__(self):
        return f"IF: ({self.condition}, {self.thenBody}, {self.elseBody})"


class whileNode(object):
    def __init__(self, condition, thenBody):
        self.condition = condition
        self.thenBody = thenBody
        
    def __repr__(self):
        return f"WHILE: ({self.condition})"


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
            return result
                
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
        
        
    def And(self):
        return self.BinaryOp(self.comparison, TokenTypes.AND)
        
    
    def Or(self):
        return self.BinaryOp(self.And, TokenTypes.OR)
        
    
    def assignment(self):
        left = self.Or()
        if self.current_token is None or self.current_token.type not in (TokenTypes.EQUAL, TokenTypes.PLUS_ASSIGN, TokenTypes.MINUS_ASSIGN):
            return left
        else:
            op = self.current_token
            self.advance()
            right = self.assignment()
            
        
        return Assignment(left.name, right, op.type)
        
        
    def typeDeclaration(self):
        type_name = self.current_token.type          
        self.advance()  
        assignValue = self.assignment()
        return TypeDeclaration(type_name, assignValue.name, assignValue.value)
        
        
    def statement(self):
        if self.current_token.type in (TokenTypes.INTEGER_TYPE, TokenTypes.FLOAT_TYPE, TokenTypes.STRING_TYPE, TokenTypes.BOOLEAN_TYPE):
            return self.typeDeclaration()
            
        if self.current_token.type == TokenTypes.IF:
            return self.ifStatement()
        elif self.current_token.type == TokenTypes.WHILE:
            return self.whileStatement()
            
        result = self.assignment()
        
        if self.current_token.type == TokenTypes.SEMI:
            self.advance()
            return result
        else:
            raise Lang_SyntaxError("Expected ';' ", self.current_token.line)
            
        
    def ifStatement(self):
        self.advance()
        if self.current_token.type == TokenTypes.LPAREN:
            self.advance()
            condition = self.assignment()
        if self.current_token.type == TokenTypes.RPAREN:
            self.advance()
            
        thenResult = self.statementBlock()
        
        if self.current_token.type == TokenTypes.ELSE:
            self.advance()
            
            elseResult = self.statementBlock()
        else:
            elseResult = None
            
        return ifNode(condition, thenResult, elseResult)
        
        
    def whileStatement(self):
        self.advance()
        if self.current_token.type == TokenTypes.LPAREN:
            self.advance()
            condition = self.assignment()
        if self.current_token.type == TokenTypes.RPAREN:
            self.advance()
            
        thenBody = self.statementBlock()
        
        return whileNode(condition, thenBody)
        
            
    def statementBlock(self):
        if self.current_token.type != TokenTypes.LBRACE:
            raise Lang_SyntaxError("Expected opening '{'", self.current_token.line)
            
        self.advance()
        resList = []
        
        while self.current_token.type != TokenTypes.RBRACE:
            result = self.statement()
            resList.append(result)
        
        if self.current_token.type != TokenTypes.RBRACE:
            raise Lang_SyntaxError("Expected closing '}'", self.current_token.line)
            
        self.advance()   
        return Block(resList)
        
            
    def program(self):
        resList = []
        while self.current_token.type != TokenTypes.EOF:
            result = self.statement()
            resList.append(result)
        return Block(resList)
        
        
    def BinaryOp(self, func, ops):
        left = func()
        
        if self.current_token is not None:
            while self.current_token.type in ops:
                op_token = self.current_token
                self.advance()
                right = func()
                left = BinOp(left, op_token, right)
        else:
            raise Lang_SyntaxError("Expected operator", self.current_token.line)
            
        return left
        
        
    def parse(self):
        res = self.program()
        return res
                    
        
if __name__ == "__main__":
    while True:       
        text = input(">> ")
        
        if text == "exit":
            break
            
        parser = Parser(Lexer(text).tokenize())
        ast = parser.parse()
        
        print(ast)