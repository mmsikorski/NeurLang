def is_digit(char):
    return char >= "0" and char <= "9"


def is_alpha(char):
    return (
        (char >= "a" and char <= "z") or (char >= "A" and char <= "Z") or char == "_"
        )


def is_alphanumeric(char):
    return is_digit(char) or is_alpha(char)

class Scanner:
    def __init__(self):
        self.tokens = []
        self.line = 1
        self.start = 1
        self.current = 1
        self.source = None
        self.end = len(self.source)
        pass


    def scan_tokens(self, source):
        self.source = source

        return self.tokens

    def scan_token(self):

        pass
