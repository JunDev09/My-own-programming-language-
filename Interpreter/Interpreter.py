from Parser.Parser import Num, Unary, BinOp, Boolean, String, Identifier, Assignment, Block, ifNode, Parser
from Lexer.Lexer import Lexer
from Lexer.Tokens import TokenTypes
from Errors.ErrorClasses import Lang_RuntimeError

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
                    case TokenTypes.EQUAL_TO:
                        return left == right
                    case TokenTypes.NOT_EQUAL:
                        return left != right
                    case TokenTypes.GREATER_OP:
                        return left > right
                    case TokenTypes.LESSER_OP:
                        return left < right
                    case TokenTypes.GREATER_EQUAL:
                        return left >= right
                    case TokenTypes.LESSER_EQUAL:
                        return left <= right
                    case TokenTypes.OR:
                        return left or right
                    case TokenTypes.AND:
                        return left and right
                        
            case Unary():
                unary_operand = self.visit_node(node.operand)
                if node.operator.type == TokenTypes.MINUS:
                    return -unary_operand
                elif node.operator.type == TokenTypes.UNARY_NOT:
                    return not unary_operand
                    
            case Boolean():
                return node.value
                
            case String():
                return node.value
                
            case Identifier():
                if node.name in self.variables:
                    return self.variables[node.name]
                else:
                    raise Lang_RuntimeError(f"Variable '{node.name}' does not exist")
                    
            case ifNode():
                condition = self.visit_node(node.condition)
                if condition:
                    result = self.visit_node(node.thenBody)
                    return result
                elif node.elseBody is not None:
                    result = self.visit_node(node.elseBody)
                    return result
                else:
                    return None
                
            case Block():
                List = node.list
                latestRes = None
                for statement in List:
                    latestRes = self.visit_node(statement)
                return latestRes
                
            case Assignment():
                value = self.visit_node(node.value)
                match node.op:
                    case TokenTypes.EQUAL:
                        new_value = value 
                    case TokenTypes.PLUS_ASSIGN:
                        new_value = self.variables[node.name] + value
                    case TokenTypes.MINUS_ASSIGN:
                        new_value = self.variables[node.name] - value
                    case _:
                        new_value = value
                result = self.variables[node.name] = new_value
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