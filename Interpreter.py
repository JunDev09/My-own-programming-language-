from Parser import Num, Unary, BinOp, Parser
from Lexer import Lexer
from Tokens import TokenTypes

class Interpreter():
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
                
if __name__ == "__main__":
    while True:
        text = input(">> ")
        
        if text == "exit":
            break
            
        tokens = Lexer(text).tokenize()
        tree = Parser(tokens).parse()
        interpreter = Interpreter()
        result = interpreter.visit_node(tree)
        print(result)        