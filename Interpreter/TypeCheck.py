from Errors.ErrorClasses import Lang_RuntimeError
from Lexer.Tokens import TokenTypes

class TypeChecker():
    
    def check(Type, Value):
        if Value is not None:
            valueType = type(Value).__name__
            
            match Type:
                case TokenTypes.INTEGER_TYPE:     
                    if type(Value) is not int:
                        raise Lang_RuntimeError(f"Expected int, got {valueType} instead")
                        return None
                    Value = int(Value) 
                        
                case TokenTypes.FLOAT_TYPE:
                    if type(Value) not in (int, float):
                        raise Lang_RuntimeError(f"Expected float, got {valueType} instead")
                        return None
                    Value = float(Value)
                    
                case TokenTypes.STRING_TYPE:
                    if type(Value) is not str:
                        raise Lang_RuntimeError(f"Expected str, got {valueType} instead")
                        return None
                        
                case TokenTypes.BOOLEAN_TYPE:
                    if type(Value) is not bool:
                        raise Lang_RuntimeError(f"Expected bool, got {valueType} instead")
                        return None
                    Value = bool(Value)
                    
            return Value