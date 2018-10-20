from enum import Enum

class TokenType(Enum):
    # Keywords
    ABSTRACT = 1, #'abstract',
    AS = 2, #'as',
    CLASS = 3, #'class',
    ELSE = 4, #'else',
    EXTENDS = 5, #'extends',
    FALSE = 6, #'false',
    FINAL = 7, #'final',
    FUNC = 8, #'func',
    FOR = 9, #'for',
    IF = 10, #'if',
    IN = 11, #'in',
    LAZY = 12, #'lazy',
    LET = 13, #'let',
    NEW = 14, # 'new',
    NULL = 15, # 'null',
    OVERRIDE = 16, # 'override',
    PRIVATE = 17, # 'private',
    PROTECTED = 18, # 'protected',
    RETURN = 19, #'return',
    SUPER = 20, # 'super',
    TO = 21, # 'to',
    THIS = 22, # 'this',
    TRUE = 23, # 'true',
    VAR = 24, # 'var',
    WHILE = 25, # 'while',

    # Dispatch operators
    DOT = 26, # '.',

    # Assignment operators
    LEFT_ARROW = 27, # '<-',
    DIV_EQUAL = 28, # '/=',
    EQUAL = 29, # '=',
    MINUS_EQUAL = 30, # '-=',
    MOD_EQUAL = 31, # '%=',
    PLUS_EQUAL = 32, # '+=',
    RIGHT_ARROW = 33, # '->',
    TIMES_EQUAL = 34, # '*=',

    # Arithmetic operators
    DIV = 35, # '/',
    MOD = 36, # '%',
    MINUS = 37, # '-',
    PLUS =  38, # '+',
    TIMES = 39, # '*',

    # Comparison operators
    DOUBLE_EQUAL = 40, # '==',
    GREATER = 41, # '>',
    GREATER_OR_EQUAL = 42, # '>=',
    LESS = 43, # '<',
    LESS_OR_EQUAL = 44, # '<=',
    NOT_EQUAL = 45, # '!=',

    # Boolean operators
    AND = 46, # '&&',
    NOT = 47, # '!',
    OR = 48, # '||',

    # Other operators
    TILDE = 49, # '~',
    TILDE_EQUAL = 50, # '~=',
    DOLLAR = 51, # '$',
    DOLLAR_EQUAL = 52, # '$=',
    CARET = 53, # '^',
    CARET_EQUAL = 54, # '^=',

    # Identifier and Literals
    IDENTIFIER = 55, # 'identifier',
    INTEGER = 56, # 'integer',
    DECIMAL = 57, # 'decimal',
    STRING = 58, # 'string',

    # Delimiters
    COLON = 59, # ':',
    COMMA = 60, # ',',
    LEFT_BRACE = 61, # '{',
    LEFT_BRACKET = 62, # '[',
    LEFT_PAREN = 63, # '(',
    NEWLINE = 64, # '\n',
    RIGHT_BRACE = 65, # '}',
    RIGHT_BRACKET = 66, # ']',
    RIGHT_PAREN = 67, # ')',

    # Special token types
    END_OF_INPUT = 68, # 'EndOfInput',
    UNRECOGNIZED = 69, # 'Unrecognized'

    @staticmethod
    def get_operator_token_type(operator):
        operator_to_token_type_map = {
            '.': TokenType.DOT,
            '=': TokenType.EQUAL,
            '<-': TokenType.LEFT_ARROW,
            '->': TokenType.RIGHT_ARROW,
            '/=': TokenType.DIV_EQUAL,
            '-=': TokenType.MINUS_EQUAL,
            '%=': TokenType.MOD_EQUAL,
            '+=': TokenType.PLUS_EQUAL,
            '*=': TokenType.TIMES_EQUAL,
            '/': TokenType.DIV,
            '+': TokenType.PLUS,
            '-': TokenType.MINUS,
            '*': TokenType.TIMES,
            '%': TokenType.MOD,
            '==': TokenType.DOUBLE_EQUAL,
            '>': TokenType.GREATER,
            '<': TokenType.LESS,
            '>=': TokenType.GREATER_OR_EQUAL,
            '<=': TokenType.LESS_OR_EQUAL,
            '!': TokenType.NOT,
            '!=': TokenType.NOT_EQUAL,
            '&&': TokenType.AND,
            '||': TokenType.OR,

        }
        return operator_to_token_type_map.get(operator, None)

    @staticmethod
    def get_delimiter_token_type(delimiter):
        delimiter_to_token_type_map = {
            ':': TokenType.COLON,
            ',': TokenType.COMMA,
            '{': TokenType.LEFT_BRACE,
            '}': TokenType.RIGHT_BRACE,
            '(': TokenType.LEFT_PAREN,
            ')': TokenType.RIGHT_PAREN,
            '[': TokenType.LEFT_BRACKET,
            ']': TokenType.RIGHT_BRACKET,
        }
        return delimiter_to_token_type_map.get(delimiter, None)
