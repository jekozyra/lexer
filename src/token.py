class Token(object):
    def __init__(self, type, value, line, column):
        self.type = type
        self.value = value
        self.line = line
        self.column = column

    def toString(self):
        return ('<%s, %s, %d: %d>' % (self.type, self.value, self.line, self.column))
