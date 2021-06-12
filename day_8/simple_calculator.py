# add, sub, mul, div
# exp, log, sin, cos

# input -> two numbers, option

num1 = float(input('Enter number 1: '))
num2 = float(input('Enter number 2: '))

operation_type = int(input('Choose an operation' +
    ':\n1. Add\n2. Mul\nEnter your option: '))

if operation_type not in [1, 2]:
    print('Invalid option')
    exit()

if operation_type == 1:
    print('Sum = ', num1 + num2)
else:
    print('Mul = ', num1 * num2)
