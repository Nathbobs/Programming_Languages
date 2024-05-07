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
                # Handling integers
                current_lexeme += char
                while i + 1 < n and expression[i + 1].isdigit():
                    current_lexeme += expression[i + 1]
                    i += 1
                lexemes.append(current_lexeme)
                tokens.append("N")
                current_lexeme = ""

            # Handling operators and parentheses
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

        # Append end-of-input marker
        lexemes.append("$")
        tokens.append("$")

        return lexemes, tokens

# Example usage
S = SyntaxAnalyzer()

lexemes, tokens = S.lexer("100-12/12")
print("Lexemes: " + str(lexemes))
print("Tokens: " + str(tokens))