class MissingRequiredArgument(Exception):
    def __init__(self, message):
        super().__init__(message)

class TooMuchArguments(Exception):
    def __init__(self, message):
        super().__init__(message)

class UnableToRunFunction(Exception):
    def __init__(self, message):
        super().__init__(message)

class EmulatedTerminalDetected(Exception):
    def __init__(self, message):
        super().__init__(message)