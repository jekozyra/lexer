from char_utils import CharType, CharUtils
from enum import Enum
from number_fsm import NumberFSM
from token import Token
from token_types import TokenType

class OperatorType(Enum):
    EQUAL = 1,
    PLUS = 2,
    MINUS = 3,
    TIMES = 4,
    DIV = 5,
    GREATER = 6,
    LESS = 7,
    NOT = 8,
    AMP = 9,
    MOD = 10,
    TILDE = 11,
    DOLLAR = 12,
    CARET = 13,
    PIPE = 14

    @staticmethod
    def map_operator_to_type(operator):
        operator_map = {
            '=': OperatorType.EQUAL,
            '+': OperatorType.PLUS,
            '-': OperatorType.MINUS,
            '*': OperatorType.TIMES,
            '/': OperatorType.DIV,
            '>': OperatorType.GREATER,
            '<': OperatorType.LESS,
            '!': OperatorType.NOT,
            '&': OperatorType.AMP,
            '%': OperatorType.MOD,
            '~': OperatorType.TILDE,
            '$': OperatorType.DOLLAR,
            '^': OperatorType.CARET,
            '|': OperatorType.PIPE,
        }
        return operator_map.get(operator, None)

class Tokenizer(object):

    @staticmethod
    def tokenize_delimiter(lexer, char):
        if CharUtils.classify(char) is not CharType.DELIMITER:
            raise ValueError('Character must be one of [, ], {, }, (, ), :, or comma.')

        start_line, start_column = lexer.line, lexer.column
        lexer.move_right()
        return Token(
            TokenType.get_delimiter_token_type(char),
            char,
            start_line,
            start_column,
        )

    @staticmethod
    def tokenize_identifier(lexer, char):
        if CharUtils.classify(char) not in [CharType.LETTER, CharType.UNDERSCORE]:
            raise ValueError('Identifiers must begin with LETTER or UNDERSCORE (_).')

        start_line = lexer.line
        start_column = lexer.column
        token_value = ''

        for c in lexer.input[lexer.position:]:
            if CharUtils.classify(c) not in CharUtils.IDENTIFIER_TYPES:
                break
            token_value += c

        lexer.move_right_n(len(token_value))

        keyword_to_token_type_map = {
            'abstract': TokenType.ABSTRACT,
            'as': TokenType.AS,
            'class': TokenType.CLASS,
            'else': TokenType.ELSE,
            'extends': TokenType.EXTENDS,
            'false': TokenType.FALSE,
            'final': TokenType.FINAL,
            'func': TokenType.FUNC,
            'for': TokenType.FOR,
            'if': TokenType.IF,
            'in': TokenType.IN,
            'lazy': TokenType.LAZY,
            'let': TokenType.LET,
            'new': TokenType.NEW,
            'null': TokenType.NULL,
            'override': TokenType.OVERRIDE,
            'private': TokenType.PRIVATE,
            'protected': TokenType.PROTECTED,
            'return': TokenType.RETURN,
            'super': TokenType.SUPER,
            'to': TokenType.TO,
            'this': TokenType.THIS,
            'true': TokenType.TRUE,
            'var': TokenType.VAR,
            'while': TokenType.WHILE,
        }

        return Token(
            keyword_to_token_type_map.get(token_value, TokenType.IDENTIFIER),
            token_value,
            start_line,
            start_column)

    @staticmethod
    def tokenize_newline(lexer, char):
        if CharUtils.classify(char) is not CharType.NEWLINE:
            raise ValueError('Character must be newline (\n).')

        start_line, start_column = lexer.line, lexer.column

        lexer.next_line()

        return Token(
            TokenType.NEWLINE,
            char,
            start_line,
            start_column,
        )

    @staticmethod
    def tokenize_number(lexer, char):
        if CharUtils.classify(char) not in (CharUtils.DIGIT_TYPES + [CharType.DOT]):
            raise ValueError('Numbers must begin with ZERO, POSITIVE_DIGIT, or dot (.).')

        fsm = NumberFSM()
        token_type, token_value = fsm.run(lexer.input[lexer.position:])

        if token_type:
            # if we have a valid number, update the lexer position to reflect
            # the length of the number and return the token
            start_line, start_column = lexer.line, lexer.column
            lexer.move_right_n(len(token_value))
            return Token(token_type, token_value, start_line, start_column)

        return None

    @staticmethod
    def tokenize_operator(lexer, char):
        char_type = CharUtils.classify(char)
        operator_type = OperatorType.map_operator_to_type(char)
        next_char = lexer.look_ahead()
        next_operator_type = OperatorType.map_operator_to_type(next_char)

        start_line, start_column = lexer.line, lexer.column
        token_value = char

        # all of these symbols can have `=` tacked on to them
        extended_by_equal = [
            OperatorType.PLUS,
            OperatorType.MINUS,
            OperatorType.MOD,
            OperatorType.DIV,
            OperatorType.TIMES,
            OperatorType.LESS,
            OperatorType.EQUAL,
            OperatorType.GREATER,
            OperatorType.EQUAL,
            OperatorType.NOT,
        ]

        if char_type is CharType.DOT:
            if CharUtils.classify(lexer.look_ahead()) in CharUtils.DIGIT_TYPES:
                return Tokenizer.tokenize_number(lexer, char)
        elif (operator_type in extended_by_equal and
            next_operator_type is OperatorType.EQUAL):
            token_value += next_char
        elif (operator_type is OperatorType.LESS and
            next_operator_type is OperatorType.MINUS):
            # gives us the arrow operator
            token_value += next_char
        elif (operator_type is OperatorType.MINUS and
            next_operator_type is OperatorType.GREATER):
            token_value += next_char
        elif (operator_type is OperatorType.AMP or
            operator_type is OperatorType.PIPE):
            if next_operator_type == operator_type:
                token_value += next_char
            else:
                return None

        lexer.move_right_n(len(token_value))
        return Token(
            TokenType.get_operator_token_type(token_value),
            token_value,
            start_line,
            start_column
        )

    @staticmethod
    def tokenize_string(lexer, char):
        if CharUtils.classify(char) is not CharType.DOUBLE_QUOTE:
            raise ValueError('Strings must begin and end with DOUBLE_QUOTE (").')

        token_value = ''
        start_line = lexer.line
        start_column = lexer.column

        for position in range(lexer.position, len(lexer.input)):
            c = lexer.input[position]
            token_value += c

            # terminating double quote
            if (CharUtils.classify(c) is CharType.DOUBLE_QUOTE and not
                (position == lexer.position or
                CharUtils.classify(lexer.input[position - 1]) is CharType.ESCAPE_CHARACTER)):
                break

        if token_value[-1] == '"':
            lexer.move_right_n(len(token_value))
            return Token(TokenType.STRING, token_value, start_line, start_column)

        return None
