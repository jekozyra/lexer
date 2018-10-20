from char_utils import CharType, CharUtils
from token import Token
from tokenizers import Tokenizer
from token_types import TokenType

class Lexer(object):

    tokenizer_map = {
        CharType.DELIMITER: Tokenizer.tokenize_delimiter,
        CharType.ZERO: Tokenizer.tokenize_number,
        CharType.POSITIVE_DIGIT: Tokenizer.tokenize_number,
        CharType.DOT: Tokenizer.tokenize_operator,
        CharType.DOUBLE_QUOTE: Tokenizer.tokenize_string,
        CharType.LETTER: Tokenizer.tokenize_identifier,
        CharType.UNDERSCORE: Tokenizer.tokenize_identifier,
        CharType.OPERATOR: Tokenizer.tokenize_operator,
        CharType.NEWLINE: Tokenizer.tokenize_newline,
    }

    def __init__(self, input):
        self.input = input
        self.position = 0
        self.line = 0
        self.column = 0

    def current_char(self):
        if self.position >= len(self.input):
            raise ValueError('Input length exceeded.')
        return self.input[self.position]

    def move_right(self):
        self.move_right_n(1)

    def move_right_n(self, n):
        self.position += n
        self.column += n

    def next_line(self):
        self.position += 1
        self.line += 1
        self.column = 0

    def look_ahead(self):
        next_position = self.position + 1
        return (self.input[next_position] if next_position < len(self.input)
            else None)

    def skip_whitespace(self):
        while (self.position < len(self.input) and
            CharUtils.is_whitespace(self.input[self.position])):
            self.move_right()

    def next_token(self):

        if self.position >= len(self.input):
            return Token(TokenType.END_OF_INPUT, None, None, None)

        self.skip_whitespace()

        char = self.input[self.position]
        tokenizer_func = self.tokenizer_map.get(CharUtils.classify(char), None)

        if not tokenizer_func:
            raise ValueError('Token not in tokenizer map.')

        return tokenizer_func(self, char)

    def tokenize(self):
        tokens = []
        token = self.next_token()

        while (token.type is not TokenType.END_OF_INPUT):
            tokens.append(token)
            token = self.next_token()

        return tokens
