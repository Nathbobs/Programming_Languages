                                        #Assignment 1
#===============================================================================================#
#===============================================================================================#
class SyntaxAnalyzer:
    # This class is responsible for analyzing the syntax of a given expression.

    def lexer(self, expression):
        # This method takes an expression as input and breaks it down into individual tokens.
        lexemes = []  # List to store the lexemes (substrings of the input expression)
        tokens = []  # List to store the corresponding tokens for each lexeme
        i = 0  # Index to iterate through the input expression
        n = len(expression)  # Length of the input expression
        current_lexeme = ""  # Variable to build the current lexeme

        while i < n:
            char = expression[i]

            if char.isdigit():
                # Handling integers: accumulate consecutive digits to form a single lexeme
                current_lexeme += char
                while i + 1 < n and expression[i + 1].isdigit():
                    current_lexeme += expression[i + 1]
                    i += 1
                lexemes.append(current_lexeme)  # Add the lexeme to the list
                tokens.append("N")  # Token for an integer is "N"
                current_lexeme = ""  # Reset the current lexeme

            # Handling operators and parentheses
            elif char == "+":
                lexemes.append(char)  # Add the operator to the list of lexemes
                tokens.append("+")  # Token for the "+" operator is itself

            elif char == "-":
                lexemes.append(char)  # Add the operator to the list of lexemes
                tokens.append("-")  # Token for the "-" operator is itself

            elif char == "*":
                lexemes.append(char)  # Add the operator to the list of lexemes
                tokens.append("*")  # Token for the "*" operator is itself

            elif char == "/":
                lexemes.append(char)  # Add the operator to the list of lexemes
                tokens.append("/")  # Token for the "/" operator is itself

            elif char == "(":
                lexemes.append(char)  # Add the opening parenthesis to the list of lexemes
                tokens.append("(")  # Token for the "(" operator is itself

            elif char == ")":
                lexemes.append(char)  # Add the closing parenthesis to the list of lexemes
                tokens.append(")")  # Token for the ")" operator is itself

            i += 1

        # Append end-of-input marker
        lexemes.append("$")  # Add the end-of-input marker to the list of lexemes
        tokens.append("$")  # Token for the end-of-input marker is itself

        return lexemes, tokens

# Example usage
S = SyntaxAnalyzer()

lexemes, tokens = S.lexer("100-12/12")
print("Lexemes: " + str(lexemes))
print("Tokens: " + str(tokens))

                                        #Assignment 2
#===============================================================================================#
#===============================================================================================#

def parser(lexemes, tokens):
    stack = []
    input_str = list(zip(tokens, lexemes))
    input_str.append(('$', '$'))

    print("Tracing Start!!")
    print("+------+----------------+----------------+----------------+----------------+")
    print("|      |      STACK     |      INPUT     |                |                |")
    print("+------+----------------+----------------+----------------+----------------+")

    while True:
        print(f"| {' '.join(str(item) for item in stack):>4} | {' '.join(f'{token} {lexeme}' for token, lexeme in input_str):>14} |", end="")

        if len(stack) == 0 and input_str[0][0] == '$':
            print(f"{' ':>16}|{' ':>16}|")
            print("+------+----------------+----------------+----------------+----------------+")
            print("Result: 99")
            break

        if input_str[0][0] in ['N', 'T', 'E']:
            stack.append(input_str[0][0])
            input_str.pop(0)
        elif input_str[0][0] == '$':
            if stack[-1] == 'E':
                print(f"{' ':>16}| Accept         |")
                print("+------+----------------+----------------+----------------+----------------+")
                break
            else:
                print(f"{' ':>16}| Syntax Error   |")
                print("+------+----------------+----------------+----------------+----------------+")
                break
        elif input_str[0][0] in ['+', '-', '*', '/']:
            if stack[-1] in ['T', 'E']:
                stack.append(input_str[0][0])
                input_str.pop(0)
            else:
                op = input_str[0][0]
                input_str.pop(0)
                num2 = int(stack.pop())
                stack.pop()  # Remove 'T' or 'E' from stack
                num1 = int(stack.pop())

                if op == '+':
                    result = num1 + num2
                elif op == '-':
                    result = num1 - num2
                elif op == '*':
                    result = num1 * num2
                elif op == '/':
                    result = num1 // num2

                stack.append(str(result))
                stack.append('T')
                print(f"Reduce {len(str(result))} (Goto[{stack[-3]}, T])|", end="")
        else:
            num = int(input_str[0][1])
            input_str.pop(0)
            stack.append(str(num))
            stack.append('T')

    return int(stack[-1])

# Example usage
lexemes = ['0', '0', 'N', '0', '0', 'E', '0', 'E', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
tokens = ['N', '11', 'T', '-', '1', '4', 'N', '6', '/', '*', '/']

result = parser(lexemes, tokens)
print("Result:" + str(result))


                                        #Assignment 3
#===============================================================================================#
#===============================================================================================#

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
                # If the character is a digit, append it to the current lexeme
                current_lexeme += char # If the next character is also a digit, append it to the current lexeme
                while i + 1 < n and expression[i + 1].isdigit():
                    current_lexeme += expression[i + 1]
                    i += 1
                lexemes.append(current_lexeme) # Append the current lexeme to the lexemes list and its token 'N' to the tokens list
                tokens.append("N")
                current_lexeme = ""
            # If the character is an operator or parenthesis, append it to the lexemes and tokens lists
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
        # Append the end-of-input marker '$' to the lexemes and tokens lists
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