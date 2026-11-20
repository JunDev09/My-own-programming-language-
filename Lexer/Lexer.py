from Errors.ErrorClasses import Lang_SyntaxError, Lang_LexicalError
from .Tokens import TokenTypes
from .LexerTable import DATA_TYPE, SINGLE_OPS, BOOLEAN_WORDS, KEYWORDS, PARENTHESIS, BRACES, DOUBLE_OPS, PUNCTUATION


class Token(object):
    def __init__(self, Datatype, value, line):
        self.type = Datatype
        self.value = value
        self.line = line
    
    def __str__(self):
        return f"Token({self.type}, {self.value})"
        
    def __repr__(self):
        return self.__str__()
        
        
        
class Lexer(object):
    def __init__(self, src):
        self.src = src
        self.pos = 0
        self.line = 1
        
        
    def peek(self, offset = 0):
        src = self.src
        idx = self.pos + offset
        
        if idx < 0:
            raise Exception("OutOfBoundsError: Negative Index")
            return None
        
        if idx > len(src) - 1:
            return None
            
        current_char = src[idx]
        return current_char
            
        
    def advance(self):
        self.pos += 1
        
        
    def read_num(self, current):
        start = self.pos
        has_dot = False
        
        if self.peek() == '.' and has_dot == False:
                has_dot = True
        
        while self.peek() is not None and (self.peek().isdigit() or self.peek() == '.'):
            self.advance()
            
            if has_dot is True and self.peek() == '.':
                raise Lang_LexicalError("Too many decimal points for a float type", self.line)
            
            if self.peek() == '.' and has_dot == False:
                has_dot = True
            
        number = self.src[start:self.pos]    
            
        match has_dot:
                case True:                      
                    return Token(TokenTypes.FLOAT, float(number), self.line)
                case _:
                    return Token(TokenTypes.INTEGER, int(number), self.line)
        
        
    def read_string(self, text):
                quote_mark = '"'
                self.advance()
                start = self.pos
                
                while self.peek() is not None and self.peek() != quote_mark and self.peek() != '\n':
                    self.advance()
                    
                match self.peek():
                    case '"':
                        letters = self.src[start:self.pos]
                        self.advance()
                        return Token(TokenTypes.STRING, letters, self.line)
                    case _:
                        raise Lang_LexicalError('Expected " at line', self.line)
                        return None
        
        
    def tokenize(self):
        tokens = []
        
        while self.peek() is not None:
            current = self.peek()
            
            if current == '\n':
                self.line += 1
                self.advance()
                continue
            
            if current.isspace():
                self.advance()
                continue
            
            if current.isalpha() or current == '_':
                start = self.pos
            
                while self.peek() is not None and (self.peek().isalpha() or self.peek().isdigit() or self.peek() == '_'):
                    self.advance()
                
                letters = self.src[start:self.pos]
                    
                if letters in BOOLEAN_WORDS:
                    tokens.append(Token(TokenTypes.BOOLEAN, BOOLEAN_WORDS[letters], self.line))
                elif letters in KEYWORDS:
                    tokens.append(Token(KEYWORDS[letters], letters, self.line))
                elif letters in DATA_TYPE:
                    tokens.append(Token(DATA_TYPE[letters], letters, self.line))
                else:
                    tokens.append(Token(TokenTypes.IDENTIFIER, str(letters), self.line))
                
                continue
                
            
            elif current.isdigit() or current == '.':
                number = self.read_num(current)
                tokens.append(number)
                continue
                
                
            elif current in SINGLE_OPS or current in DOUBLE_OPS:
                two_ops = self.src[self.pos:self.pos + 2]
                    
                if two_ops in DOUBLE_OPS:
                    tokens.append(Token(DOUBLE_OPS[two_ops], two_ops, self.line))
                    self.advance()
                    self.advance()
                    
                elif current in SINGLE_OPS:
                    tokens.append(Token(SINGLE_OPS[current], current, self.line))
                    self.advance()
                continue
                    
                
            elif current in PARENTHESIS:
                tokens.append(Token(PARENTHESIS[current], current, self.line))
                self.advance()
                continue
                
                
            elif current in BRACES:
                tokens.append(Token(BRACES[current], current, self.line))
                self.advance()
                continue          
                
            
            elif current == '"':
                text = self.read_string(current)
                tokens.append(text)
                continue
            
                
            elif current in PUNCTUATION:
                tokens.append(Token(PUNCTUATION[current], current, self.line))
                self.advance()
                continue     
            else:
                self.advance()
            
            
        tokens.append(Token(TokenTypes.EOF, None, self.line))     
        return tokens
        
        
if __name__ == "__main__":
    while True:
        text = input("\n>> ")
        
        if text == "exit":
            break
            
        print(Lexer(text).tokenize())