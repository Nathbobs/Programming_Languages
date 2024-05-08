# class SyntaxAnalyzer:
#     def __init__(self):
#         pass

#     def lexer(self, input_string):
#         lexemes = []
#         tokens = []
#         current_lexeme = ''
        
#         # Define a function to check if a character is a digit
#         def is_digit(char):
#             return char.isdigit()
        
#         # Define a function to check if a character is an operator
#         def is_operator(char):
#             return char in ['+', '-', '*', '/']
        
#         # Iterate through the characters in the input string
#         for char in input_string:
#             if char == ' ':  # Skip whitespace
#                 continue
#             elif is_digit(char):  # If the character is a digit
#                 current_lexeme += char
#             elif is_operator(char):  # If the character is an operator
#                 lexemes.append(current_lexeme)
#                 tokens.append('N')
#                 lexemes.append(char)
#                 tokens.append(char)
#                 current_lexeme = ''
#             else:  # If the character is not a digit or operator (e.g., end of input)
#                 lexemes.append(current_lexeme)
#                 tokens.append('N')
#                 lexemes.append('$')
#                 tokens.append('$')
#                 current_lexeme = ''
        
#         # Add the last lexeme and token
#         lexemes.append(current_lexeme)
#         tokens.append('N')
#         lexemes.append('$')
#         tokens.append('$')
        
#         return lexemes, tokens

#     def parser(self, lexemes, tokens):
#         self.lexemes = lexemes
#         self.tokens = tokens
#         self.index = 0

#         print("Start!!")
#         result = self.E()
#         return result

#     def match(self, expected_token):
#         if self.tokens[self.index] == expected_token:
#             self.index += 1
#         else:
#             raise ValueError(f"Expected {expected_token} but found {self.tokens[self.index]}")

#     def E(self):
#         print("enter E")
#         value = self.T()
#         value = self.E_prime(value)
#         print("exit E")
#         return value

#     def E_prime(self, inherited_value):
#         print("enter E'")
#         if self.tokens[self.index] == '+':
#             self.match('+')
#             value = inherited_value + self.T()
#             value = self.E_prime(value)
#             print("exit E'")
#             return value
#         elif self.tokens[self.index] == '-':
#             self.match('-')
#             value = inherited_value - self.T()
#             value = self.E_prime(value)
#             print("exit E'")
#             return value
#         else:
#             print("exit E'")
#             return inherited_value

#     def T(self):
#         print("enter T")
#         value = int(self.lexemes[self.index])
#         self.match('N')
#         value = self.T_prime(value)
#         print("exit T")
#         return value

#     def T_prime(self, inherited_value):
#         print("enter T'")
#         if self.tokens[self.index] == '*':
#             self.match('*')
#             value = inherited_value * int(self.lexemes[self.index])
#             self.match('N')
#             value = self.T_prime(value)
#             print("exit T'")
#             return value
#         elif self.tokens[self.index] == '/':
#             self.match('/')
#             value = inherited_value / int(self.lexemes[self.index])
#             self.match('N')
#             value = self.T_prime(value)
#             print("exit T'")
#             return value
#         else:
#             print("exit T'")
#             return inherited_value

# # Example usage:
# S = SyntaxAnalyzer()
# lexemes, tokens = S.lexer("100*12")
# result = S.parser(lexemes, tokens)
# print("Result:", result)

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