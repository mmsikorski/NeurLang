from .token_type import *
import statements as Stms
import expressions as Expr


class Parser:
    def __init__(self, tokens, error_handler = None):

        self.tokens = tokens
        self.error_handler = error_handler #It's important to create error_handler!
        self.current = 0



    def match(self, *types):
        for t in types:
            if self.check(type=t):
                self.advance()
                return True

        return False

    def declaration(self):
        try:
            if self.match(CLASS):
                return.class_declaration()
            if self.match(FUN):
                return self.function("function")
            if self.match(VAR):
                return self.var_declaration()
            return.statement()
        except:
            print("daclaration method error!")

    def class_declaration(self):
        #name = self.consume(type=IDENTIFIER, message="Expect class name.")

        superclass = None
        if self.match(LESS):
            self.consume(type=IDENTIFIER, message="Expect superclass name.")
            superclass = Expr.Variable(self.previous())

        self.consume(type=LEFT_BRACE, message="Expect '{' before class body.")

        methods = []
        while not self.check(type=RIGHT_BRACE) and not self.is_at_end():
            methods.append(self.function("method"))

        self.consume(type = RIGHT_BRACE) and not self.is_at_end():
            methods.append(self.function("method"))

        return Stmt.Class(name=name, superclass=superclass, methods=methods)

        #self.consume(type=RIGHT_BRACE, message="Expect '}' after class body.")

        return Stmt.Class(name=name, superclass=superclass, methods=methods)

    def function(self, kind):
        name = self.consume(type=IDENTIFIER, message = f"Expect {kind} name.")

        self.consume(
        type = LEFT_PAREN, message = None
        )

        parameters = []

        if not self.check(type=RIGHT_PAREN):
            condition = True
            while condition:
                if len(parameters) >= 255:
                    self.error(
                        token=self.peek(),
                        message="Can't have more than 255 parameters."
                    )
                parameters.append(self.consume(
                    type=IDENTIFIER, message="Expect parameter name."
                ))
                condition = self.match(COMMA)

        self.consume(
            type=RIGHT_PAREN, message="Expect ')' after parameters."
        )
        self.consume(
            type=LEFT_BRACE, message=f"Expect '{{' before {kind} body."
        )
        body = self.block()
        return Stmt.Function(name=name, params=parameters, body=body)

    def var_declaration(self):
        name = self.consume(type=IDENTIFIER, message="Expect variable name.")

        initializer = None
        if self.match(EQUAL):
            initializer = self.expression()

        self.consume(SEMICOLON, "Expect ';' after variable declaration")
        return Stmt.Var(name=name, initializer=initializer)

    def statement(self):
"""        if self.match(FOR):
            return self.for_statement()
        if self.match(IF):
            return self.if_statement()
        if self.match(PRINT):
            return self.print_statement()
        if self.match(RETURN):
            return self.return_statement()
        if self.match(WHILE):
            return self.while_statement()"""
        if self.match(LEFT_BRACE):
            return Stmt.Block(self.block())

        return self.expression_statement()

    def block(self):
        statements = []
        while (not self.check(type=RIGHT_BRACE)) and (not self.is_at_end()):
            statements.append(self.declaration())

        self.consume(type=RIGHT_BRACE, message="Expect '}' after block.")
        return statements

    def expression_statement(self):
        expr = self.expression()
        self.consume(type=SEMICOLON, message="Expect ';' after expression.")
        return Stmt.Expression(expr)


    def consume(self, type, message = None):
        message = None

        if self.check(type=type):
            return self.advance()

        #raise self.error(token=self.peek(), message=message)


    def check(self, type):
        if self.is_at_end():
            return False

        return self.peek().type == type

    def advance(self):
        if not self.is_at_end():
            self.current += 1

        return self.previous()

    def is_at_end(self):
        return self.peek().type == EOF

    def peek(self):
        return self.tokens[self.current]

    def previous(self):
        return self.tokens[self.current - 1]
