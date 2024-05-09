# class SyntaxAnalyzer:
#     def __init__(self):
#         # Parsing table
#         self.parsing_table = {
#             "E'": {"id": "E", "(": "E"},
#             "E": {"id": "T", "(": "T", "+": "E2", "-": "E3"},
#             "T": {"id": "N", "(": "N", "*": "T5", "/": "T6"},
#             "N": {"id": "id", "(": "(E')"}
#         }

#         # Production rules
#         self.productions = {
#             "E2": "E+T",
#             "E3": "E-T",
#             "T5": "T*N",
#             "T6": "T/N"
#         }

#     def parser(self, input_data):
#         lexemes, tokens = input_data
#         stack = ["0"]  # Initialize stack with the start state
#         input_buffer = tokens + ["$"]  # Add end marker to the input buffer

#         print("Tracing Start!!")
#         print("+------+--------------+---------------+----------------+--------------------+")
#         print("| STACK |INPUT         |ACTION         |               |                    |")
#         print("+------+--------------+---------------+----------------+--------------------+")

#         while True:
#             state = stack[-1]  # Get the current state from the top of the stack
#             symbol = input_buffer[0]  # Get the current input symbol

#             print(f"| ({stack_to_str(stack)}) |{input_buffer_to_str(input_buffer)}|               |               |                    |")

#             # Check if the current state and input symbol exist in the parsing table
#             if state in self.parsing_table and symbol in self.parsing_table[state]:
#                 entry = self.parsing_table[state][symbol]

#                 if entry in self.productions:
#                     # Perform reduction
#                     production = self.productions[entry]
#                     print(f"| ({stack_to_str(stack)}) |{input_buffer_to_str(input_buffer)}| Reduce {production}|               |                    |")

#                     # Pop the appropriate number of symbols from the stack
#                     num_symbols = len(production.split()) - 1
#                     for _ in range(num_symbols):
#                         stack.pop()

#                     # Get the new state from the parsing table
#                     new_state = self.parsing_table[stack[-1]][production.split()[0]]
#                     stack.append(new_state)

#                 else:
#                     # Perform shift
#                     stack.append(symbol)
#                     input_buffer = input_buffer[1:]
#                     print(f"| ({stack_to_str(stack)}) |{input_buffer_to_str(input_buffer)}| Shift {symbol}|               |                    |")

#             elif symbol == "$" and state == "0":
#                 # Accept the input
#                 print(f"| ({stack_to_str(stack)}) |{input_buffer_to_str(input_buffer)}|               | Accept        |                    |")
#                 break

#             else:
#                 # Reject the input
#                 print("Syntax Error")
#                 return

#         # Perform the actual calculations
#         result = calculate(lexemes, tokens)
#         return result

#     def calculate(self, lexemes, tokens):
#         stack = []
#         for lexeme, token in zip(lexemes, tokens):
#             if token == "N":
#                 stack.append(int(lexeme))
#             elif token == "+":
#                 operand2 = stack.pop()
#                 operand1 = stack.pop()
#                 result = operand1 + operand2
#                 stack.append(result)
#             elif token == "-":
#                 operand2 = stack.pop()
#                 operand1 = stack.pop()
#                 result = operand1 - operand2
#                 stack.append(result)
#             elif token == "*":
#                 operand2 = stack.pop()
#                 operand1 = stack.pop()
#                 result = operand1 * operand2
#                 stack.append(result)
#             elif token == "/":
#                 operand2 = stack.pop()
#                 operand1 = stack.pop()
#                 result = operand1 // operand2  # Integer division
#                 stack.append(result)

#         return stack.pop()

# def stack_to_str(stack):
#     return "".join(stack)

# def input_buffer_to_str(input_buffer):
#     return "".join(input_buffer)

# # Example usage
# S = SyntaxAnalyzer()
# lexemes, tokens = ["100", "-", "12", "/", "12"], ["N", "-", "N", "/", "N"]
# result = S.parser((lexemes, tokens))
# print("Result:" + str(result))

class SyntaxAnalyzer:
    def __init__(self):
        self.parsing_table = {
            "E'": {"id": "E", "(": "E"},
            "E": {"id": "T", "(": "T", "+": "E2", "-": "E3"},
            "T": {"id": "N", "(": "N", "*": "T5", "/": "T6"},
            "N": {"id": "N", "(": "(E')"}
        }

        self.productions = {
            "E2": "E+T",
            "E3": "E-T",
            "T5": "T*N",
            "T6": "T/N"
        }

    def parser(self, input_data):
        lexemes, tokens = input_data
        stack = ["0"]  # Initialize stack with the start state
        input_buffer = tokens + ["$"]  # Add end marker to the input buffer

        print("Tracing Start!!")
        print("+------+--------------+---------------+----------------+--------------------+")
        print("| STACK |INPUT         |ACTION         |               |                    |")
        print("+------+--------------+---------------+----------------+--------------------+")

        while True:
            state = stack[-1]  # Get the current state from the top of the stack
            symbol = input_buffer[0]  # Get the current input symbol

            print(f"| ({stack_to_str(stack)}) |{input_buffer_to_str(input_buffer)}|               |               |                    |")

            # Check if the current state and input symbol exist in the parsing table
            if state in self.parsing_table and symbol in self.parsing_table[state]:
                entry = self.parsing_table[state][symbol]

                if entry in self.productions:
                    # Perform reduction
                    production = self.productions[entry]
                    print(f"| ({stack_to_str(stack)}) |{input_buffer_to_str(input_buffer)}| Reduce {production}|               |                    |")

                    # Pop the appropriate number of symbols from the stack
                    num_symbols = len(production.split()) - 1
                    for _ in range(num_symbols):
                        stack.pop()

                    # Get the new state from the parsing table
                    new_state = self.parsing_table[stack[-1]][production.split()[0]]
                    stack.append(new_state)

                else:
                    # Perform shift
                    stack.append(symbol)
                    input_buffer = input_buffer[1:]
                    print(f"| ({stack_to_str(stack)}) |{input_buffer_to_str(input_buffer)}| Shift {symbol}|               |                    |")

            elif symbol == "$" and state == "0":
                # Accept the input
                print(f"| ({stack_to_str(stack)}) |{input_buffer_to_str(input_buffer)}|               | Accept        |                    |")
                break

            else:
                # Reject the input
                print("Syntax Error")
                return

        # Perform the actual calculations
        result = self.calculate(lexemes, tokens)
        return result

    def calculate(self, lexemes, tokens):
        stack = []
        for lexeme, token in zip(lexemes, tokens):
            if token == "N":
                stack.append(int(lexeme))
            elif token == "+":
                operand2 = stack.pop()
                operand1 = stack.pop()
                result = operand1 + operand2
                stack.append(result)
            elif token == "-":
                operand2 = stack.pop()
                operand1 = stack.pop()
                result = operand1 - operand2
                stack.append(result)
            elif token == "*":
                operand2 = stack.pop()
                operand1 = stack.pop()
                result = operand1 * operand2
                stack.append(result)
            elif token == "/":
                operand2 = stack.pop()
                operand1 = stack.pop()
                result = operand1 // operand2  # Integer division
                stack.append(result)

        return stack.pop()

def stack_to_str(stack):
    return "".join(stack)

def input_buffer_to_str(input_buffer):
    return "".join(input_buffer)

# Example usage
S = SyntaxAnalyzer()
lexemes, tokens = ["100", "-", "12", "/", "12"], ["N", "-", "N", "/", "N"]
result = S.parser((lexemes, tokens))
if result is not None:
    print("Result:" + str(result))
else:
    print("Result:None")