import unittest

from src.lexer import Lexer
from src.token_types import TokenType

class NextTokenTest(unittest.TestCase):

    def test_should_recognize_a_left_parenthesis(self):
        lexer = Lexer('(')
        token = lexer.next_token()

        self.assertEqual(token.type, TokenType.LEFT_PAREN)
        self.assertEqual(token.value, '(')

    def test_should_recognize_a_right_parenthesis(self):
        lexer = Lexer(')')
        token = lexer.next_token()

        self.assertEqual(token.type, TokenType.RIGHT_PAREN)
        self.assertEqual(token.value, ')')

    def test_should_recognize_the_number_0(self):
        lexer = Lexer('0')
        token = lexer.next_token()

        self.assertEqual(token.type, TokenType.INTEGER)
        self.assertEqual(token.value, '0')

    def test_should_recognize_simple_integer_literal(self):
        lexer = Lexer('42')
        token = lexer.next_token()

        self.assertEqual(token.type, TokenType.INTEGER)
        self.assertEqual(token.value, '42')

    def test_should_recognize_simple_decimal_literal(self):
        lexer = Lexer('3.14')
        token = lexer.next_token()

        self.assertEqual(token.type, TokenType.DECIMAL)
        self.assertEqual(token.value, '3.14')

    def test_should_recognize_decimal_starting_with_dot(self):
        lexer = Lexer('.25')
        token = lexer.next_token()

        self.assertEqual(token.type, TokenType.DECIMAL)
        self.assertEqual(token.value, '.25')

    def test_should_recognize_decimal_in_scientific_notation(self):
        lexer = Lexer('2e65')
        token = lexer.next_token()

        self.assertEqual(token.type, TokenType.DECIMAL)
        self.assertEqual(token.value, '2e65')

    def test_should_recognize_decimal_in_scientific_notation_with_negative_exponent_part(self):
        lexer = Lexer('42e-65')
        token = lexer.next_token()

        self.assertEqual(token.type, TokenType.DECIMAL)
        self.assertEqual(token.value, '42e-65')

    def test_should_recognize_simple_string_literal(self):
        lexer = Lexer('"Hello, World!"')
        token = lexer.next_token()

        self.assertEqual(token.type, TokenType.STRING)
        self.assertEqual(token.value, '"Hello, World!"')

    def test_should_recognize_string_containing_a_newline_character(self):
        lexer = Lexer('"a string containing a \\n newline character."')
        token = lexer.next_token()

        self.assertEqual(token.type, TokenType.STRING)
        self.assertEqual(token.value, '"a string containing a \\n newline character."')

    def test_should_recognize_a_string_containing_an_espaced_backslash(self):
        lexer = Lexer('"a string with a \\\\ backslash"')
        token = lexer.next_token()

        self.assertEqual(token.type, TokenType.STRING)
        self.assertEqual(token.value, '"a string with a \\\\ backslash"')

    def test_should_recognize_a_string_containing_escaped_double_quotes(self):
        lexer = Lexer('"a string containing an \\" escaped double quote"')
        token = lexer.next_token()

        self.assertEqual(token.type, TokenType.STRING)
        self.assertEqual(token.value, '"a string containing an \\" escaped double quote"')

    def test_should_recognize_a_string_containing_escape_sequences(self):
        lexer = Lexer('"a string containing \\t\\b\\r\\f\\v\\0 escape sequences"')
        token = lexer.next_token()

        self.assertEqual(token.type, TokenType.STRING)
        self.assertEqual(token.value, '"a string containing \\t\\b\\r\\f\\v\\0 escape sequences"')

    def test_should_recognize_an_identifier_of_a_single_letter(self):
        lexer = Lexer('i')
        token = lexer.next_token()

        self.assertEqual(token.type, TokenType.IDENTIFIER)
        self.assertEqual(token.value, 'i')

    def test_should_recognize_an_identifier_made_of_letters(self):
        lexer = Lexer('anIdentifier')
        token = lexer.next_token()

        self.assertEqual(token.type, TokenType.IDENTIFIER)
        self.assertEqual(token.value, 'anIdentifier')

    def test_should_recognize_an_identifier_starting_with_underscore(self):
        lexer = Lexer('_identifier')
        token = lexer.next_token()

        self.assertEqual(token.type, TokenType.IDENTIFIER)
        self.assertEqual(token.value, '_identifier')

    def test_should_recognize_an_identifier_containing_an_underscore(self):
        lexer = Lexer('an_identifier')
        token = lexer.next_token()

        self.assertEqual(token.type, TokenType.IDENTIFIER)
        self.assertEqual(token.value, 'an_identifier')

    def test_should_recognize_an_identifier_containing_dollar_sign_character(self):
        lexer = Lexer('an$identifier')
        token = lexer.next_token()

        self.assertEqual(token.type, TokenType.IDENTIFIER)
        self.assertEqual(token.value, 'an$identifier')

    def test_should_recognize_an_identifier_containing_a_digit(self):
        lexer = Lexer('identifier1')
        token = lexer.next_token()

        self.assertEqual(token.type, TokenType.IDENTIFIER)
        self.assertEqual(token.value, 'identifier1')

    def test_should_recognize_the_boolean_true_literal(self):
        lexer = Lexer('true')
        token = lexer.next_token()

        self.assertEqual(token.type, TokenType.TRUE)
        self.assertEqual(token.value, 'true')

    def test_should_recognize_the_boolean_false_literal(self):
        lexer = Lexer('false')
        token = lexer.next_token()

        self.assertEqual(token.type, TokenType.FALSE)
        self.assertEqual(token.value, 'false')

    def test_should_recognize_the_abstract_keyword(self):
        lexer = Lexer('abstract')
        token = lexer.next_token()

        self.assertEqual(token.type, TokenType.ABSTRACT)
        self.assertEqual(token.value, 'abstract')

    def test_should_recognize_the_class_keyword(self):
        lexer = Lexer('class')
        token = lexer.next_token()

        self.assertEqual(token.type, TokenType.CLASS)
        self.assertEqual(token.value, 'class')

    def test_should_recognize_the_func_keyword(self):
        lexer = Lexer('func')
        token = lexer.next_token()

        self.assertEqual(token.type, TokenType.FUNC)
        self.assertEqual(token.value, 'func')

    def test_should_recognize_the_else_keyword(self):
        lexer = Lexer('else')
        token = lexer.next_token()

        self.assertEqual(token.type, TokenType.ELSE)
        self.assertEqual(token.value, 'else')

    def test_should_recognize_the_extends_keyword(self):
        lexer = Lexer('extends')
        token = lexer.next_token()

        self.assertEqual(token.type, TokenType.EXTENDS)
        self.assertEqual(token.value, 'extends')

    def test_should_recognize_the_false_keyword(self):
        lexer = Lexer('false')
        token = lexer.next_token()

        self.assertEqual(token.type, TokenType.FALSE)
        self.assertEqual(token.value, 'false')

    def test_should_recognize_the_final_keyword(self):
        lexer = Lexer('final')
        token = lexer.next_token()

        self.assertEqual(token.type, TokenType.FINAL)
        self.assertEqual(token.value, 'final')

    def test_should_recognize_the_for_keyword(self):
        lexer = Lexer('for')
        token = lexer.next_token()

        self.assertEqual(token.type, TokenType.FOR)
        self.assertEqual(token.value, 'for')

    def test_should_recognize_the_in_keyword(self):
        lexer = Lexer('in')
        token = lexer.next_token()

        self.assertEqual(token.type, TokenType.IN)
        self.assertEqual(token.value, 'in')

    def test_should_recognize_the_if_keyword(self):
        lexer = Lexer('if')
        token = lexer.next_token()

        self.assertEqual(token.type, TokenType.IF)
        self.assertEqual(token.value, 'if')

    def test_should_recognize_the_let_keyword(self):
        lexer = Lexer('let')
        token = lexer.next_token()

        self.assertEqual(token.type, TokenType.LET)
        self.assertEqual(token.value, 'let')

    def test_should_recognize_the_new_keyword(self):
        lexer = Lexer('new')
        token = lexer.next_token()

        self.assertEqual(token.type, TokenType.NEW)
        self.assertEqual(token.value, 'new')

    def test_should_recognize_the_null_keyword(self):
        lexer = Lexer('null')
        token = lexer.next_token()

        self.assertEqual(token.type, TokenType.NULL)
        self.assertEqual(token.value, 'null')

    def test_should_recognize_the_override_keyword(self):
        lexer = Lexer('override')
        token = lexer.next_token()

        self.assertEqual(token.type, TokenType.OVERRIDE)
        self.assertEqual(token.value, 'override')

    def test_should_recognize_the_private_keyword(self):
        lexer = Lexer('private')
        token = lexer.next_token()

        self.assertEqual(token.type, TokenType.PRIVATE)
        self.assertEqual(token.value, 'private')

    def test_should_recognize_the_protected_keyword(self):
        lexer = Lexer('protected')
        token = lexer.next_token()

        self.assertEqual(token.type, TokenType.PROTECTED)
        self.assertEqual(token.value, 'protected')

    def test_should_recognize_the_return_keyword(self):
        lexer = Lexer('return')
        token = lexer.next_token()

        self.assertEqual(token.type, TokenType.RETURN)
        self.assertEqual(token.value, 'return')

    def test_should_recognize_the_super_keyword(self):
        lexer = Lexer('super')
        token = lexer.next_token()

        self.assertEqual(token.type, TokenType.SUPER)
        self.assertEqual(token.value, 'super')

    def test_should_recognize_the_to_keyword(self):
        lexer = Lexer('to')
        token = lexer.next_token()

        self.assertEqual(token.type, TokenType.TO)
        self.assertEqual(token.value, 'to')

    def test_should_recognize_the_this_keyword(self):
        lexer = Lexer('this')
        token = lexer.next_token()

        self.assertEqual(token.type, TokenType.THIS)
        self.assertEqual(token.value, 'this')

    def test_should_recognize_the_true_keyword(self):
        lexer = Lexer('true')
        token = lexer.next_token()

        self.assertEqual(token.type, TokenType.TRUE)
        self.assertEqual(token.value, 'true')

    def test_should_recognize_the_var_keyword(self):
        lexer = Lexer('var')
        token = lexer.next_token()

        self.assertEqual(token.type, TokenType.VAR)
        self.assertEqual(token.value, 'var')

    def test_should_recognize_the_while_keyword(self):
        lexer = Lexer('while')
        token = lexer.next_token()

        self.assertEqual(token.type, TokenType.WHILE)
        self.assertEqual(token.value, 'while')

    def test_should_recognize_an_identifier_starting_with_a_reserved_keyword(self):
        lexer = Lexer('toString')
        token = lexer.next_token()

        self.assertEqual(token.type, TokenType.IDENTIFIER)
        self.assertEqual(token.value, 'toString')

    def test_should_recognize_the_dispatch_operator(self):
        lexer = Lexer('.')
        token = lexer.next_token()

        self.assertEqual(token.type, TokenType.DOT)
        self.assertEqual(token.value, '.')

    def test_should_recognize_the_left_arrow_operator(self):
        lexer = Lexer('<-')
        token = lexer.next_token()

        self.assertEqual(token.type, TokenType.LEFT_ARROW)
        self.assertEqual(token.value, '<-')

    def test_should_recognize_the_div_equal_operator(self):
        lexer = Lexer('/=')
        token = lexer.next_token()

        self.assertEqual(token.type, TokenType.DIV_EQUAL)
        self.assertEqual(token.value, '/=')

    def test_should_recognize_the_equal_operator(self):
        lexer = Lexer('=')
        token = lexer.next_token()

        self.assertEqual(token.type, TokenType.EQUAL)
        self.assertEqual(token.value, '=')

    def test_should_recognize_the_minus_equal_operator(self):
        lexer = Lexer('-=')
        token = lexer.next_token()

        self.assertEqual(token.type, TokenType.MINUS_EQUAL)
        self.assertEqual(token.value, '-=')

    def test_should_recognize_the_modulo_equal_operator(self):
        lexer = Lexer('%=')
        token = lexer.next_token()

        self.assertEqual(token.type, TokenType.MOD_EQUAL)
        self.assertEqual(token.value, '%=')

    def test_should_recognize_the_plus_equal_operator(self):
        lexer = Lexer('+=')
        token = lexer.next_token()

        self.assertEqual(token.type, TokenType.PLUS_EQUAL)
        self.assertEqual(token.value, '+=')

    def test_should_recognize_the_right_arrow_operator(self):
        lexer = Lexer('->')
        token = lexer.next_token()

        self.assertEqual(token.type, TokenType.RIGHT_ARROW)
        self.assertEqual(token.value, '->')

    def test_should_recognize_the_times_equal_operator(self):
        lexer = Lexer('*=')
        token = lexer.next_token()

        self.assertEqual(token.type, TokenType.TIMES_EQUAL)
        self.assertEqual(token.value, '*=')

    def test_should_recognize_the_div_operator(self):
        lexer = Lexer('/')
        token = lexer.next_token()

        self.assertEqual(token.type, TokenType.DIV)
        self.assertEqual(token.value, '/')

    def test_should_recognize_the_modulo_operator(self):
        lexer = Lexer('%')
        token = lexer.next_token()

        self.assertEqual(token.type, TokenType.MOD)
        self.assertEqual(token.value, '%')

    def test_should_recognize_the_minus_operator(self):
        lexer = Lexer('-')
        token = lexer.next_token()

        self.assertEqual(token.type, TokenType.MINUS)
        self.assertEqual(token.value, '-')

    def test_should_recognize_the_plus_operator(self):
        lexer = Lexer('+')
        token = lexer.next_token()

        self.assertEqual(token.type, TokenType.PLUS)
        self.assertEqual(token.value, '+')

    def test_should_recognize_the_times_operator(self):
        lexer = Lexer('*')
        token = lexer.next_token()

        self.assertEqual(token.type, TokenType.TIMES)
        self.assertEqual(token.value, '*')

    def test_should_recognize_the_double_equal_operator(self):
        lexer = Lexer('==')
        token = lexer.next_token()

        self.assertEqual(token.type, TokenType.DOUBLE_EQUAL)
        self.assertEqual(token.value, '==')

    def test_should_recognize_the_greater_operator(self):
        lexer = Lexer('>')
        token = lexer.next_token()

        self.assertEqual(token.type, TokenType.GREATER)
        self.assertEqual(token.value, '>')

    def test_should_recognize_the_greater_or_equal_operator(self):
        lexer = Lexer('>=')
        token = lexer.next_token()

        self.assertEqual(token.type, TokenType.GREATER_OR_EQUAL)
        self.assertEqual(token.value, '>=')

    def test_should_recognize_the_less_operator(self):
        lexer = Lexer('<')
        token = lexer.next_token()

        self.assertEqual(token.type, TokenType.LESS)
        self.assertEqual(token.value, '<')

    def test_should_recognize_the_less_or_equal_operator(self):
        lexer = Lexer('<=')
        token = lexer.next_token()

        self.assertEqual(token.type, TokenType.LESS_OR_EQUAL)
        self.assertEqual(token.value, '<=')

    def test_should_recognize_the_not_equal_operator(self):
        lexer = Lexer('!=')
        token = lexer.next_token()

        self.assertEqual(token.type, TokenType.NOT_EQUAL)
        self.assertEqual(token.value, '!=')

    def test_should_recognize_the_and_operator(self):
        lexer = Lexer('&&')
        token = lexer.next_token()

        self.assertEqual(token.type, TokenType.AND)
        self.assertEqual(token.value, '&&')

    def test_should_recognize_the_not_operator(self):
        lexer = Lexer('!')
        token = lexer.next_token()

        self.assertEqual(token.type, TokenType.NOT)
        self.assertEqual(token.value, '!')

    def test_should_recognize_the_or_operator(self):
        lexer = Lexer('||')
        token = lexer.next_token()

        self.assertEqual(token.type, TokenType.OR)
        self.assertEqual(token.value, '||')

    def test_should_recognize_a_colon(self):
        lexer = Lexer(':')
        token = lexer.next_token()

        self.assertEqual(token.type, TokenType.COLON)
        self.assertEqual(token.value, ':')

    def test_should_recognize_a_comma(self):
        lexer = Lexer(',')
        token = lexer.next_token()

        self.assertEqual(token.type, TokenType.COMMA)
        self.assertEqual(token.value, ',')

    def test_should_recognize_a_left_brace(self):
        lexer = Lexer('{')
        token = lexer.next_token()

        self.assertEqual(token.type, TokenType.LEFT_BRACE)
        self.assertEqual(token.value, '{')

    def test_should_recognize_a_right_brace(self):
        lexer = Lexer('}')
        token = lexer.next_token()

        self.assertEqual(token.type, TokenType.RIGHT_BRACE)
        self.assertEqual(token.value, '}')

    def test_should_recognize_a_left_bracket(self):
        lexer = Lexer('[')
        token = lexer.next_token()

        self.assertEqual(token.type, TokenType.LEFT_BRACKET)
        self.assertEqual(token.value, '[')

    def test_should_recognize_a_right_bracket(self):
        lexer = Lexer(']')
        token = lexer.next_token()

        self.assertEqual(token.type, TokenType.RIGHT_BRACKET)
        self.assertEqual(token.value, ']')

    def test_should_recognize_newline_character_as_single_token(self):
        lexer = Lexer('\n')
        token = lexer.next_token()

        self.assertEqual(token.type, TokenType.NEWLINE)
        self.assertEqual(token.value, '\n')

class TokenizeTest(unittest.TestCase):

    def test_should_tokenize_a_simple_expression(self):
        lexer = Lexer('42 + 21')

        tokens = lexer.tokenize()

        self.assertEqual(3, len(tokens))

        self.assertEqual(tokens[0].type, TokenType.INTEGER)
        self.assertEqual(tokens[0].value, '42')

        self.assertEqual(tokens[1].type, TokenType.PLUS)
        self.assertEqual(tokens[1].value, '+')

        self.assertEqual(tokens[2].type, TokenType.INTEGER)
        self.assertEqual(tokens[2].value, '21')

    def test_should_properly_tokenize_a_full_method_definition(self):
        lexer = Lexer('func add(a: Int, b: Int): Int = {\n' +
            '   a + b\n' +
            '}')

        tokens = lexer.tokenize();

        self.assertEqual(21, len(tokens))

        self.assertEqual(tokens[0].type, TokenType.FUNC)

        self.assertEqual(tokens[1].type, TokenType.IDENTIFIER)
        self.assertEqual(tokens[1].value, 'add')

        self.assertEqual(tokens[2].type, TokenType.LEFT_PAREN)

        self.assertEqual(tokens[3].type, TokenType.IDENTIFIER)
        self.assertEqual(tokens[3].value, 'a')

        self.assertEqual(tokens[4].type, TokenType.COLON)

        self.assertEqual(tokens[5].type, TokenType.IDENTIFIER)
        self.assertEqual(tokens[5].value, 'Int')

        self.assertEqual(tokens[6].type, TokenType.COMMA)

        self.assertEqual(tokens[7].type, TokenType.IDENTIFIER)
        self.assertEqual(tokens[7].value, 'b')

        self.assertEqual(tokens[8].type, TokenType.COLON)

        self.assertEqual(tokens[9].type, TokenType.IDENTIFIER)
        self.assertEqual(tokens[9].value, 'Int')

        self.assertEqual(tokens[10].type, TokenType.RIGHT_PAREN)

        self.assertEqual(tokens[11].type, TokenType.COLON)

        self.assertEqual(tokens[12].type, TokenType.IDENTIFIER)
        self.assertEqual(tokens[12].value, 'Int')

        self.assertEqual(tokens[13].type, TokenType.EQUAL)

        self.assertEqual(tokens[14].type, TokenType.LEFT_BRACE)

        self.assertEqual(tokens[15].type, TokenType.NEWLINE)

        self.assertEqual(tokens[16].type, TokenType.IDENTIFIER)
        self.assertEqual(tokens[16].value, 'a')

        self.assertEqual(tokens[17].type, TokenType.PLUS)

        self.assertEqual(tokens[18].type, TokenType.IDENTIFIER)
        self.assertEqual(tokens[18].value, 'b')

        self.assertEqual(tokens[19].type, TokenType.NEWLINE)

        self.assertEqual(tokens[20].type, TokenType.RIGHT_BRACE)

    def test_should_assign_the_correct_line_and_column_numbers(self):
        lexer = Lexer('func equals(a: Int, b: Int): Boolean = {\n' +
            '   a == b\n' +
            '}')

        tokens = lexer.tokenize()

        self.assertEqual(0, tokens[0].line)
        self.assertEqual(0, tokens[0].column)

        self.assertEqual(0, tokens[1].line)
        self.assertEqual(5, tokens[1].column)

        self.assertEqual(0, tokens[2].line)
        self.assertEqual(11, tokens[2].column)

        self.assertEqual(0, tokens[3].line)
        self.assertEqual(12, tokens[3].column)

        self.assertEqual(0, tokens[4].line)
        self.assertEqual(13, tokens[4].column)

        self.assertEqual(0, tokens[5].line)
        self.assertEqual(15, tokens[5].column)

        self.assertEqual(0, tokens[6].line)
        self.assertEqual(18, tokens[6].column)

        self.assertEqual(0, tokens[7].line)
        self.assertEqual(20, tokens[7].column)

        self.assertEqual(0, tokens[8].line)
        self.assertEqual(21, tokens[8].column)

        self.assertEqual(0, tokens[9].line)
        self.assertEqual(23, tokens[9].column)

        self.assertEqual(0, tokens[10].line)
        self.assertEqual(26, tokens[10].column)

        self.assertEqual(0, tokens[11].line)
        self.assertEqual(27, tokens[11].column)

        self.assertEqual(0, tokens[12].line)
        self.assertEqual(29, tokens[12].column)

        self.assertEqual(0, tokens[13].line)
        self.assertEqual(37, tokens[13].column)

        self.assertEqual(0, tokens[14].line)
        self.assertEqual(39, tokens[14].column)

        self.assertEqual(0, tokens[15].line)
        self.assertEqual(40, tokens[15].column)

        self.assertEqual(1, tokens[16].line)
        self.assertEqual(3, tokens[16].column)

        self.assertEqual(1, tokens[17].line)
        self.assertEqual(5, tokens[17].column)

        self.assertEqual(1, tokens[18].line)
        self.assertEqual(8, tokens[18].column)

        self.assertEqual(1, tokens[19].line)
        self.assertEqual(9, tokens[19].column)

        self.assertEqual(2, tokens[20].line)
        self.assertEqual(0, tokens[20].column)
