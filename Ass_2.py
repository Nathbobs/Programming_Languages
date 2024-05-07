# class SyntaxAnalyzer:
#     def __init__(self):
#         self.parsing_table = {
#             "E'": {"id": "E", "(": "E"},
#             "E": {"id": "T", "(": "T", "+": "E2", "-": "E3"},
#             "T": {"id": "N", "(": "N", "*": "T5", "/": "T6"},
#             "N": {"id": "id", "(": "(E')"}
#         }

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

#         def stack_str(self, stack):
#             return "".join(stack)
#         def input_buffer_str(self, input_buffer):
#             return "".join(input_buffer)

#         while True:
#             state = stack[-1]  # Get the current state from the top of the stack
#             symbol = input_buffer[0]  # Get the current input symbol

#             print(f"| ({stack_str(stack)}) |{input_buffer_str(input_buffer)}|               |               |                    |")

#             # Check if the current state and input symbol exist in the parsing table
#             if state in self.parsing_table and symbol in self.parsing_table[state]:
#                 entry = self.parsing_table[state][symbol]

#                 if entry in self.productions:
#                     # Perform reduction
#                     production = self.productions[entry]
#                     print(f"| ({stack_str(stack)}) |{input_buffer_str(input_buffer)}| Reduce {production}|               |                    |")

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
#                     print(f"| ({stack_str(stack)}) |{input_buffer_str(input_buffer)}| Shift {symbol}|               |                    |")

#             elif symbol == "$" and state == "0":
#                 # Accept the input
#                 print(f"| ({stack_str(stack)}) |{input_buffer_str(input_buffer)}|               | Accept        |                    |")
#                 break

#             else:
#                 # Reject the input
#                 print("Syntax Error")
#                 return

#         # Perform the actual calculations
#         if len(stack) == 2 and stack[-1] == "E":  # Check if the stack contains the expected final state
            
#             result = calculate(lexemes, tokens)
#             return result
#         else:
#             print("Syntax Error: Invalid stack state")
#             return

#     # def stack_str(self, stack):
#     #     return "".join(stack)

#     # def input_buffer_str(self, input_buffer):
#     #     return "".join(input_buffer)

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

# # Example usage
# S = SyntaxAnalyzer()
# lexemes, tokens = ["100", "-", "12", "/", "12"], ["N", "-", "N", "/", "N"]
# result = S.parser((lexemes, tokens))
# print("Result:" + str(result))

class SyntaxAnalyzer:
    def __init__(self, parsing_table):
        self.parsing_table = parsing_table
    
    def parser(self, lexemes, tokens):
        stack = ['$']
        input_index = 0
        output = ""
        
        # Print tracing header
        print("+------+--------------+---------------+----------------+--------------------+")
        print("| STACK| INPUT\t| ACTION\t|")
        print("+------+--------------+---------------+----------------+--------------------+")
        
        while True:
            stack_top = stack[-1]
            current_token = tokens[input_index] if input_index < len(tokens) else '$'
            
            # Print current stack and input
            print("|", stack, "\t|", current_token, "\t|", end=" ")
            
            # Check if we should reduce
            if stack_top in self.parsing_table and current_token in self.parsing_table[stack_top]:
                action = self.parsing_table[stack_top][current_token]
                if action == 'accept':
                    print("ACCEPT\t\t|")
                    break
                elif action.startswith('reduce'):
                    production_rule = action.split()[1]
                    num_to_pop = len(production_rule.split('->')[1].split())
                    for _ in range(num_to_pop):
                        stack.pop()
                    stack_top = stack[-1]
                    stack.append(production_rule.split('->')[0])
                    output = self.perform_operation(production_rule.split('->')[0], output)
                    print("REDUCE by", production_rule, "\t|")
                    continue  # Skip shifting
                else:
                    print("ERROR\t\t|")
                    break
            # Shift operation
            else:
                if current_token != '$':  # Avoid adding '$' to stack
                    stack.append(current_token)
                input_index += 1
                print("SHIFT\t\t|")
        
        return output
    
    def perform_operation(self, operator, output):
        if operator == 'E':
            return output + "="
        elif operator == '+':
            return output + "+"
        elif operator == '-':
            return output + "-"
        elif operator == '*':
            return output + "*"
        elif operator == '/':
            return output + "/"
        elif operator == 'N':
            return output + "N"
        else:
            return output

# Example usage:
parsing_table = {
    'E': {'N': 'E'},
    'T': {'N': 'T'},
    'N': {'N': 'N'},
    '+': {'N': 'shift'},
    '-': {'N': 'shift'},
    '*': {'N': 'shift'},
    '/': {'N': 'shift'},
    '$': {'$': 'accept'},
    'E\'': {'$': 'accept'}
}

S = SyntaxAnalyzer(parsing_table)
result = S.parser(['100', '-', '12', '/', '12', '$'], ['N', '-', 'N', '/', 'N', '$'])
print("Result:", result)
