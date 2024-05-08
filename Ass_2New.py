from collections import defaultdict

# Parsing table from the given problem
parsing_table = {
    0: {'N': 7, '$': 1},
    1: {},
    2: {},
    3: {},
    4: {'+': 5, '-': 6, 'N': 7},
    5: {'N': 8, '/': 9},
    6: {'N': 8, '/': 9},
    7: {'N': None, '/': 8, '*': 9, '$': 'R6'},
    8: {'N': 10, '$': 'R5'},
    9: {'N': 10, '$': 'R5'},
    10: {'$': 'R5'},
    11: {'N': None, '$': 'R6'}
}

# Grammar rules
rules = [
    "E' -> E",
    "E -> TE'",
    "E' -> +TE'",
    "E' -> -TE'",
    "E' -> ε",
    "T -> NT'",
    "T' -> *NT'",
    "T' -> /NT'",
    "T' -> ε"
]

def parser(lexemes, tokens):
    stack = [(0, 'E')]
    input_tokens = tokens + ['$']
    output = []

    print("Tracing Start!!")
    print("+------+---------------+---------------+-----------------+")
    print("|      | STACK         | INPUT         | ACTION          |")
    print("+------+---------------+---------------+-----------------+")

    while True:
        state, symbol = stack[-1]
        token = input_tokens[0]

        print(f"| ({len(stack)-1:02d}) | {' '.join([f'{s}/{sym}' for s, sym in stack])} | {' '.join(input_tokens)} | ", end='')

        if symbol in parsing_table[state] and parsing_table[state][symbol] is not None:
            action = parsing_table[state][symbol]
            if isinstance(action, int):
                stack.append((action, token))
                input_tokens = input_tokens[1:]
                output.append(token)
                print(f"Shift {action}|")
            else:
                rule_index = int(action[1:])
                rule = rules[rule_index]
                lhs, rhs = rule.split(' -> ')
                rhs_symbols = rhs.split()
                stack = stack[:-len(rhs_symbols)]
                next_state = parsing_table[stack[-1][0]][lhs]
                stack.append((next_state, lhs))
                if rule_index == 6:  # T' -> *NT'
                    operand2 = int(output.pop())
                    operand1 = int(output.pop())
                    result = operand1 * operand2
                    output.append(str(result))
                elif rule_index == 7:  # T' -> /NT'
                    operand2 = int(output.pop())
                    operand1 = int(output.pop())
                    result = operand1 // operand2
                    output.append(str(result))
                print(f"Reduce {rule_index} (Goto[{stack[-2][0]}, {lhs}])|")
        elif symbol == '$' and token == '$':
            print("Accept|")
            break
        else:
            print("Error|")
            break

    if output:
        result = int(output[0])
        print(f"Result: {result}")
    else:
        print("Error: Invalid expression")

# Example usage
lexemes = ['N', '-', 'N', '/', 'N', '$']
tokens = ['2', '-', '3', '/', '4']
parser(lexemes, tokens)