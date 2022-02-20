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
        pass


    def scan_tokens(self):


        return self.tokens
