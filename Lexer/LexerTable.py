from .Tokens import TokenTypes

KEYWORDS = {
    'and': TokenTypes.AND,
    'or': TokenTypes.OR,
    'if': TokenTypes.IF,
    'else': TokenTypes.ELSE,
    'while': TokenTypes.WHILE,
}

PUNCTUATION = {
    ';': TokenTypes.SEMI
}

PARENTHESIS = {
    ')': TokenTypes.RPAREN,
    '(': TokenTypes.LPAREN,
}

BRACES = {
    '{': TokenTypes.LBRACE,
    '}': TokenTypes.RBRACE,
}

SINGLE_OPS = {
    '+': TokenTypes.PLUS,
    '-': TokenTypes.MINUS,
    '*': TokenTypes.STAR,
    '/': TokenTypes.SLASH,
    '!': TokenTypes.UNARY_NOT,
    '=': TokenTypes.EQUAL,
    '>': TokenTypes.GREATER_OP,
    '<': TokenTypes.LESSER_OP,
}

DOUBLE_OPS = {
    '==': TokenTypes.EQUAL_TO,
    '!=': TokenTypes.NOT_EQUAL,
    '<=': TokenTypes.LESSER_EQUAL,
    '>=': TokenTypes.GREATER_EQUAL,
    '+=': TokenTypes.PLUS_ASSIGN,
    '-=': TokenTypes.MINUS_ASSIGN,
}

BOOLEAN_WORDS = {
    'true': True,
    'false': False,
}

DATA_TYPE = {
    'int': TokenTypes.INTEGER_TYPE,
    'float': TokenTypes.FLOAT_TYPE,
    'str': TokenTypes.STRING_TYPE,
    'bool': TokenTypes.BOOLEAN_TYPE,
}