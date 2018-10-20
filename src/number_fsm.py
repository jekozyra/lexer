from char_utils import CharType, CharUtils
from enum import Enum
from fsm import FSM
from token_types import TokenType

class NumberFSM(FSM):

    class State(Enum):
        INITIAL = 1,
        INTEGER = 2,
        FRACTIONAL_BEGINNING = 3,
        FRACTIONAL_NUMBER = 4,
        EXPONENTIAL_BEGINNING = 5,
        SIGNED_EXPONENTIAL = 6,
        EXPONENTIAL_NUMBER = 7,
        INVALID = -1,

    EXPONENTIAL_PREFIXES = ['E', 'e']
    SIGNS = ['+', '-']
    ACCEPTING_STATE_TO_TOKEN_MAP = {
        State.INTEGER: TokenType.INTEGER,
        State.FRACTIONAL_NUMBER: TokenType.DECIMAL,
        State.EXPONENTIAL_NUMBER: TokenType.DECIMAL,
    }

    def __init__(self):
        super(NumberFSM, self).__init__(
            states=self.State,
            initial_state=self.State.INITIAL,
            accepting_states = [
                self.State.INTEGER,
                self.State.FRACTIONAL_NUMBER,
                self.State.EXPONENTIAL_NUMBER,
            ]
        )
        self.transition_map = {
            self.State.INITIAL: self._get_initial_transition,
            self.State.INTEGER: self._get_integer_transition,
            self.State.FRACTIONAL_BEGINNING: self._get_fractional_beginning_transition,
            self.State.FRACTIONAL_NUMBER: self._get_fractional_number_transition,
            self.State.EXPONENTIAL_BEGINNING: self._get_exponential_beginning_transition,
            self.State.SIGNED_EXPONENTIAL: self._get_signed_exponential_transition,
            self.State.EXPONENTIAL_NUMBER: self._get_exponential_number_transition,
        }

    def _get_initial_transition(self, char):
        if char == '.':
            return self.State.FRACTIONAL_BEGINNING
        elif CharUtils.classify(char) in CharUtils.DIGIT_TYPES:
            return self.State.INTEGER

        return self.State.INVALID

    def _get_integer_transition(self, char):
        if char == '.':
            return self.State.FRACTIONAL_BEGINNING
        elif char in self.EXPONENTIAL_PREFIXES:
            return self.State.EXPONENTIAL_BEGINNING
        elif CharUtils.classify(char) in CharUtils.DIGIT_TYPES:
            return self.State.INTEGER
        return self.State.INVALID

    def _get_fractional_beginning_transition(self, char):
        if CharUtils.classify(char) in CharUtils.DIGIT_TYPES:
            return self.State.FRACTIONAL_NUMBER
        return self.State.INVALID

    def _get_fractional_number_transition(self, char):
        if char in self.EXPONENTIAL_PREFIXES:
            return self.State.EXPONENTIAL_BEGINNING
        elif CharUtils.classify(char) in CharUtils.DIGIT_TYPES:
            return self.State.FRACTIONAL_NUMBER
        return self.State.INVALID

    def _get_exponential_beginning_transition(self, char):
        if char in self.SIGNS:
            return self.State.SIGNED_EXPONENTIAL
        elif CharUtils.classify(char) is CharType.POSITIVE_DIGIT:
            return self.State.EXPONENTIAL_NUMBER
        return self.State.INVALID

    def _get_signed_exponential_transition(self, char):
        if CharUtils.classify(char) is CharType.POSITIVE_DIGIT:
            return self.State.EXPONENTIAL_NUMBER
        return self.State.INVALID

    def _get_exponential_number_transition(self, char):
        if CharUtils.classify(char) in CharUtils.DIGIT_TYPES:
            return self.State.EXPONENTIAL_NUMBER

        return self.State.INVALID

    def next_state(self, current_state, input):
        transition_func = self.transition_map.get(current_state, None)

        if transition_func:
            return transition_func(input)

        return None

    def run(self, input):
        current_state = self.initial_state
        output = ''
        for c in input:
            # we've hit the end of the decimal token
            if not CharUtils.is_valid_number_character(c):
                break

            output += c
            next_state = self.next_state(current_state, c)
            current_state = next_state

        if current_state in self.accepting_states:
            return (
                self.ACCEPTING_STATE_TO_TOKEN_MAP.get(current_state, None),
                output)

        return (None, None)
