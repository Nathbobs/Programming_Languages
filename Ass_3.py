class SyntaxAnalyzer:
    def lexer(self, expression):
        lexemes = []
        tokens = []
        i = 0
        n = len(expression)
        current_lexeme = ""

        while i < n:
            char = expression[i]

            if char.isdigit():
                current_lexeme += char
                while i + 1 < n and expression[i + 1].isdigit():
                    current_lexeme += expression[i + 1]
                    i += 1
                lexemes.append(current_lexeme)
                tokens.append("N")
                current_lexeme = ""

            elif char == "+":
                lexemes.append(char)
                tokens.append("+")

            elif char == "-":
                lexemes.append(char)
                tokens.append("-")

            elif char == "*":
                lexemes.append(char)
                tokens.append("*")

            elif char == "/":
                lexemes.append(char)
                tokens.append("/")

            elif char == "(":
                lexemes.append(char)
                tokens.append("(")

            elif char == ")":
                lexemes.append(char)
                tokens.append(")")

            i += 1

        lexemes.append("$")
        tokens.append("$")

        return lexemes, tokens
    def parser(self, input_data):
        self.lexemes, self.tokens = input_data
        self.index = 0
        self.result = None

        print("Start!!")
        self.E()

        if self.tokens[self.index] == "$":
            print("Result:" + str(self.result))
        else:
            print("Syntax Error")

    def E(self):
        print("enter E")
        self.T()
        self.E_prime()
        print("exit E")

    def E_prime(self):
        print("enter E'")
        if self.tokens[self.index] == "+":
            self.index += 1
            operand1 = self.result  # Store the current result as operand1
            self.T()
            operand2 = self.result  # Store the new result as operand2
            self.result = operand1 + operand2  # Perform addition
            self.E_prime()
        elif self.tokens[self.index] == "-":
            self.index += 1
            operand1 = self.result  # Store the current result as operand1
            self.T()
            operand2 = self.result  # Store the new result as operand2
            self.result = operand1 - operand2  # Perform subtraction
            self.E_prime()
        else:
            print("epsilon")
        print("exit E'")

    def T(self):
        print("enter T")
        self.N()
        self.T_prime()
        print("exit T")

    def T_prime(self):
        print("enter T'")
        if self.tokens[self.index] == "*":
            self.index += 1
            operand1 = self.result  # Store the current result as operand1
            self.N()
            operand2 = self.result  # Store the new result as operand2
            self.result = operand1 * operand2  # Perform multiplication
            self.T_prime()
        elif self.tokens[self.index] == "/":
            self.index += 1
            operand1 = self.result  # Store the current result as operand1
            self.N()
            operand2 = self.result  # Store the new result as operand2
            self.result = operand1 // operand2  # Perform integer division
            self.T_prime()
        else:
            print("epsilon")
        print("exit T'")

    def N(self):
        if self.tokens[self.index] == "N":
            self.result = int(self.lexemes[self.index])
            self.index += 1

# Example usage
S = SyntaxAnalyzer()
lexemes, tokens = S.lexer("100*12")
S.parser((lexemes, tokens))