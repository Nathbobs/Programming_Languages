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