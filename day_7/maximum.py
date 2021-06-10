# code reusability

def max_num(n1, n2):
    if n1 > n2:
        return n1
    else:
        return n2

num1 = int(input('Enter number 1: '))
num2 = int(input('Enter number 2: '))

print('Maximum number:', max_num(num1, num2))