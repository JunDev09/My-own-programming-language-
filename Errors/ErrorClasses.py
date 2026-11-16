class LangError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)
        
    def __str__(self):
        return f"{self.message}"

class Lang_SyntaxError(LangError):
    def __init__(self, message, line):
        error = f"SyntaxError: {message} at line {line}"
        super().__init__(error)
    
class Lang_LexicalError(LangError):
    def __init__(self, message, line):
        error = f"LexicalError: {message} at line {line}"
        super().__init__(error)
    
class Lang_RuntimeError(LangError): 
    def __init__(self, message, line=None):
        super().__init__(f"RuntimeError: {message}")