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