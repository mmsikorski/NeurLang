from .token import *
from .token_type import *

def is_digit(char):
    return char >= "0" and char <= "9"


def is_alpha(char):
    return (
        (char >= "a" and char <= "z") or (char >= "A" and char <= "Z") or char == "_"
        )


def is_alphanumeric(char):
    return is_digit(char) or is_alpha(char)

#
# KEYWORDS
KEYWORDS = {
    "class": CLASS,
    "func": FUNC,
    "print": PRINT,
}
# KEYWORDS
#
class Scanner:
    def __init__(self, source):
        self.tokens = []
        self.line = 1
        self.start = 0
        self.current = 0
        self.source = source

        #self.keywords = {}
        self.token_strings = {
            "(": lambda: LEFT_PAREN,
            ")": lambda: RIGHT_PAREN,
            "{": lambda: LEFT_BRACE,
            "}": lambda: RIGHT_BRACE,
            "[": lambda: LEFT_BRACKET,
            "]": lambda: RIGHT_BRACKET,
            ",": lambda: COMMA,
            ".": lambda: DOT,
            "-": lambda: MINUS,
            "+": lambda: PLUS,
            ";": lambda: SEMICOLON,
            "*": lambda: STAR,
            "!": lambda: BANG_EQUAL if self.match("=") else BANG,
            "=": lambda: EQUAL_EQUAL if self.match("=") else EQUAL,
            "<": lambda: LESS_EQUAL if self.match("=") else LESS,
            ">": lambda: GREATER_EQUAL if self.match("=") else GREATER,
            "/": lambda: self.slash(),
            " ": lambda: None,
            "\r": lambda: None,
            "\t": lambda: None,
            "\n": lambda: self.newline(),
        }


    def scan_tokens(self):

        while not self.is_at_end():
            self.start = self.current
            self.scan_token()


        self.tokens.append(
            Token(type=EOF, lexeme="", literal=None, line=self.line)
        )

        return self.tokens

    def scan_token(self):
            char = self.advance()
            if char in self.token_strings:
                self.add_token(type=self.token_strings[char]())
            elif char == "\"":
                self.add_token(*self.string())
            elif is_digit(char):
                self.add_token(*self.number())
            elif is_alpha(char):
                self.add_token(type=self.indentifier())
            else:
                print("Error")

    def string(self):
        while self.peek() != "\"" and not self.is_at_end():
            if self.peek() == "\n":
                self.line += 1
            self.advance()


        if self.is_at_end():
            #print("STRING ERROR method")
            return (None, None)

        self.advance() #Here we increment current in order to close "

        value = self.source[self.start+1: self.current-1]
        return (STRING, value)

    def number(self):
        while is_digit(self.peek()):
            self.advance()
        if self.peek() == '.' and is_digit(self.peek_next()):
            self.advance()
        return (NUMBER, float(self.source[self.start:self.current]))




    def indentifier(self):
        while(is_alphanumeric(self.peek())):
            self.advance()

        text = self.source[self.start:self.current]

        if text in KEYWORDS:
            return KEYWORDS[text]
        else:
            return IDENTIFIER


    def add_token(self, type, literal = None):

        if type == None:
            return
        text = self.source[self.start: self.current]

        self.tokens.append(
        Token(type = type, lexeme = text, literal = literal, line = self.line)
        )


    #Methods below help us manipulate a source code.
    def advance(self, spaces = 1):
        self.current += spaces

        return self.source[self.current - 1]

    def peek_next(self):
        if self.current + 1 >= len(self.source):
            return "\0"
        else:
            return self.source[self.current + 1]

    def match(self, expected):
        if self.is_the_end():
            return False

        if self.source[self.current] != expected:
            return False

    def peek(self):

        return "\0" if self.is_at_end() else self.source[self.current]

    def is_at_end(self):
        return self.current >= len(self.source)

    def newline(self):

        self.line += 1
        return None


    def error(self, line, message):
        pass
