class Token:
    def __init__(self, type, lexeme, literal, line):
        self.type = type
        self.lexeme = lexeme
        self.literal = literal
        self.line = line

    def __str__(self):
        return f"Type = {str(self.type)} | Lexeme =  {self.lexeme} | literal = {self.literal}"
