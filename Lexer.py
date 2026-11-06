from Tokens import TokenTypes


class Token(object):
    def __init__(self, type, value):
        self.type = type
        self.value = value
    
    def __str__(self):
        return f"Token({self.type}, {self.value})"
        
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
                    tokens.append(Token(TokenTypes.BOOLEAN, True))
                elif letters == "false":
                    tokens.append(Token(TokenTypes.BOOLEAN, False))
                else:
                    tokens.append(Token(TokenTypes.IDENTIFIER, str(letters)))
                
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
                        
                    tokens.append(Token(TokenTypes.FLOAT, float(digits)))
                        
                elif has_dot is not True:
                    digits = self.src[start:self.pos]
                    tokens.append(Token(TokenTypes.INTEGER, int(digits)))
                    
                else:
                    print("error")
                    
                continue
                
                
            elif current == '+':
                tokens.append(Token(TokenTypes.PLUS, '+'))
                self.advance()
                continue
                
                
            elif current == '-':
                tokens.append(Token(TokenTypes.MINUS, '-'))
                self.advance()
                continue
                
                
            elif current == '*':
                tokens.append(Token(TokenTypes.STAR, '*'))
                self.advance()
                continue
            
            
            elif current == '/':
                tokens.append(Token(TokenTypes.SLASH, '/'))
                self.advance()
                continue
                
                
            elif current == '(':
                tokens.append(Token(TokenTypes.LPAREN, '('))
                self.advance()
                continue
                
                
            elif current == ')':
                tokens.append(Token(TokenTypes.RPAREN, ')'))
                self.advance()
                continue
                
            elif current == '=':
                tokens.append(Token(TokenTypes.EQUAL, '='))
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
                    tokens.append(Token(TokenTypes.STRING, letters))
                    self.advance()
                else:
                    print("bro there's no closing clauses for your string value, fix it bruh")
                
                continue
            
                
            elif current == ';':
                tokens.append(Token(TokenTypes.SEMI, ';'))
                self.advance()
                continue
                       
            else:
                self.advance()
                
            
        tokens.append(Token(TokenTypes.EOF, None))     
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