print('Calculator')
is_run = True

while is_run:
    print("Actions:'+', '-', '*', '/', '^', Exit: 'x'")
    number1 = float(input('Enter numbers 1: '))
    number2 = float(input('Enter numbers 2: '))
    action = input('Action: ')

    if action == 'x':
        is_run = False
    elif action == '+':
        result = number1 + number2
    elif action == '-':
        result = number1 - number2
    elif action == '*':
        result = number1 * number2
    elif action == '/':
        if number2 != 0:
            result = number1 / number2
    elif action == '^':
        result = number1 ** int(number2)
    else:
        print('Incorrrect action: [', action, ']')

    print(f'{number1}{action}{number2}', result)
