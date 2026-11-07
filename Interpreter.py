from Parser import Num, Unary, BinOp, Boolean, String, Identifier, Assignment, Parser
from Lexer import Lexer
from Tokens import TokenTypes

class Interpreter():
    def __init__(self):
        self.variables = {}
        
        
    def visit_node(self, node):
        
        match node:
            
            case Num():
                value = node.value
                number = value
                return number
                
            case BinOp():
                left = self.visit_node(node.left)
                right = self.visit_node(node.right)
                op = node.op
                match op.type:
                    case TokenTypes.PLUS:
                        return left + right
                    case TokenTypes.MINUS:
                        return left - right
                    case TokenTypes.STAR:
                        return left * right
                    case TokenTypes.SLASH:
                        return left / right
                        
            case Unary():
                unary_operand = self.visit_node(node.operand)
                if node.operator.type == TokenTypes.MINUS:
                    return -unary_operand
                    
            case Boolean():
                return node.value
                
            case String():
                return node.value
                
            case Identifier():
                if node.name in self.variables:
                    return self.variables[node.name]
                else:
                    raise Exception(f"Variable {node.name} doesn't exist")
                
            case Assignment():
                value = self.visit_node(node.value)
                result = self.variables[node.name] = value
                return result
                
                
if __name__ == "__main__":
    interpreter = Interpreter()
    
    while True:
        text = input(">> ")
        
        if text == "exit":
            break
            
        tokens = Lexer(text).tokenize()
        tree = Parser(tokens).parse()
        result = interpreter.visit_node(tree)
        print(result)        