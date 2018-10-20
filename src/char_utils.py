from enum import Enum
import re

class CharType(Enum):
    LETTER = 1,
    ZERO = 2,
    POSITIVE_DIGIT = 3,
    DELIMITER = 4,
    OPERATOR = 5,
    DOT = 6,
    DOUBLE_QUOTE = 7,
    ESCAPE_CHARACTER = 8,
    UNDERSCORE = 9,
    NEWLINE = 10,
    UNRECOGNIZED = -1,

class CharUtils(object):

    DECIMAL_SPECIAL_CHARACTERS = 'Ee+-.'

    DIGIT_TYPES = [CharType.ZERO, CharType.POSITIVE_DIGIT]
    IDENTIFIER_TYPES = (
        [CharType.LETTER, CharType.UNDERSCORE, CharType.OPERATOR] + DIGIT_TYPES)

    @staticmethod
    def _is_zero(char):
        return char == '0'

    @staticmethod
    def _is_dot(char):
        return char == '.'

    @staticmethod
    def _is_double_quote(char):
        return char == '"'

    @staticmethod
    def _is_underscore(char):
        return char == '_'

    @staticmethod
    def _is_newline(char):
        return char == '\n'

    @staticmethod
    def _is_positive_digit(char):
        return re.search(r"[0-9]", char)

    @staticmethod
    def _is_letter(char):
        return re.search(r"[a-zA-Z]", char)

    @staticmethod
    def _is_delimiter(char):
        return char in '{}[]():,'

    @staticmethod
    def _is_operator(char):
        return char in '+-*/=<>!&%~$|^'

    @staticmethod
    def _is_escape_character(char):
        return char == "\\"

    @staticmethod
    def is_whitespace(char):
        return char == ' '

    @staticmethod
    def is_valid_number_character(char):
        return (char in CharUtils.DECIMAL_SPECIAL_CHARACTERS or
            CharUtils.classify(char) in CharUtils.DIGIT_TYPES)

    @staticmethod
    def classify(char):

        if not char:
            return CharType.UNRECOGNIZED

        if CharUtils._is_zero(char):
            return CharType.ZERO
        elif CharUtils._is_newline(char):
            return CharType.NEWLINE
        elif CharUtils._is_delimiter(char):
            return CharType.DELIMITER
        elif CharUtils._is_dot(char):
            return CharType.DOT
        elif CharUtils._is_underscore(char):
            return CharType.UNDERSCORE
        elif CharUtils._is_escape_character(char):
            return CharType.ESCAPE_CHARACTER
        elif CharUtils._is_double_quote(char):
            return CharType.DOUBLE_QUOTE
        elif CharUtils._is_positive_digit(char):
            return CharType.POSITIVE_DIGIT
        elif CharUtils._is_letter(char):
            return CharType.LETTER
        elif CharUtils._is_operator(char):
            return CharType.OPERATOR

        return CharType.UNRECOGNIZED
