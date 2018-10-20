from abc import ABCMeta, abstractmethod

class FSM(object):
    __metaclass__ = ABCMeta

    def __init__(self, states, initial_state, accepting_states):
        self.states = states
        self.initial_state = initial_state
        self.accepting_states = accepting_states

    @abstractmethod
    def next_state(self):
        pass

    @abstractmethod
    def run(self):
        pass
