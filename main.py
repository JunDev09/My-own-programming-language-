EOF = 'EOF'
INTEGER = 'INTEGER'
FLOAT = 'FLOAT'
STRING = 'STRING'
BOOLEAN = 'BOOLEAN'
PLUS = 'PLUS'
MINUS = 'MINUS'
STAR = 'STAR'
SLASH = 'SLASH'
EQUAL = 'EQUAL'
RPAREN = 'RPAREN'
LPAREN = 'LPAREN'
SEMI = 'SEMI'

IDENTIFIER = 'IDENTIFIER'

class Token(object):
    def __init__(self, type, value):
        self.type = type
        self.value = value
    
    def __str__(self):
        return "\nToken({type}, {value})\n".format(type = self.type, value = repr(self.value))
        
    def __repr__(self):
        return self.__str__()
        
        
        
class Lexer(object):
    def __init__(self, src):
        self.src = src
        self.pos = 0
        
        
    def peek(self, offset = 0):
        src = self.src
        idx = self.pos + offset
        
        if idx < 0:
            raise Exception("OutOfBoundsError: Negative Index")
            return
        
        if idx > len(src) - 1:
            return None
            
        current_char = src[idx]
        return current_char
            
        
    def advance(self):
        self.pos += 1
        
        
    def tokenize(self):
        tokens = []
        
        while self.peek() is not None:
            current = self.peek()
            
            if current.isspace():
                self.advance()
                continue
            
            if current.isalpha() or current == '_':
                start = self.pos
            
                while self.peek() is not None and (self.peek().isalpha() or self.peek().isdigit() or self.peek() == '_'):
                    self.advance()
                
                letters = self.src[start:self.pos]
                    
                if letters == "true":
                    tokens.append(Token(BOOLEAN, True))
                elif letters == "false":
                    tokens.append(Token(BOOLEAN, False))
                else:
                    tokens.append(Token(IDENTIFIER, str(letters)))
                
                continue
                
            
            elif current.isdigit() or current == '.':
                start = self.pos
                has_dot = False

                
                while self.peek() is not None and (self.peek().isdigit() or self.peek() == '.' and (has_dot is False)):
                    
                    if self.peek() == '.':
                        has_dot = True
                        
                    self.advance()
                
                
                if has_dot is True:
                    digits = self.src[start:self.pos]
                        
                    if digits == '.':
                        print("Error")
                        break
                        
                    tokens.append(Token(FLOAT, float(digits)))
                        
                elif has_dot is not True:
                    digits = self.src[start:self.pos]
                    tokens.append(Token(INTEGER, int(digits)))
                    
                else:
                    print("error")
                    
                continue
                
                
            elif current == '+':
                tokens.append(Token(PLUS, '+'))
                self.advance()
                continue
                
                
            elif current == '-':
                tokens.append(Token(MINUS, '-'))
                self.advance()
                continue
                
                
            elif current == '*':
                tokens.append(Token(STAR, '*'))
                self.advance()
                continue
            
            
            elif current == '/':
                tokens.append(Token(SLASH, '/'))
                self.advance()
                continue
                
                
            elif current == '(':
                tokens.append(Token(LPAREN, '('))
                self.advance()
                continue
                
                
            elif current == ')':
                tokens.append(Token(RPAREN, ')'))
                self.advance()
                continue
                
            elif current == '=':
                tokens.append(Token(EQUAL, '='))
                self.advance()
                continue
            
            
            elif current == '"':
                quote_mark = '"'
                self.advance()
                start = self.pos
                
                while self.peek() is not None and self.peek() != quote_mark:
                    self.advance()
                    
                
                
                if self.peek() == quote_mark:
                    letters = self.src[start:self.pos]
                    tokens.append(Token(STRING, str(letters)))
                    self.advance()
                else:
                    print("bro there's no closing clauses for your string value, fix it bruh")
                
                continue
            
                
            elif current == ';':
                tokens.append(Token(SEMI, ';'))
                self.advance()
                continue
                       
            else:
                self.advance()
                
            
        tokens.append(Token(EOF, None))     
        return tokens
        
        
        
def main():
    pass
    
if __name__ == "__main__":
    while True:
        #print(Lexer("ab").peek(-1))
        text = input("\n>> ")
        
        if text == "exit":
            break
            
        print(Lexer(text).tokenize())