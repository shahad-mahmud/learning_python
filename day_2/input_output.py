# escape charecters -> 
# \n -> new line
# \t -> tab space
# \\ -> backslash
print(1,2, 3,      5,   4, 2, sep='\\', end='$\n\n')

# output formatting
name = 'Shahad'
age = 50
income = 20
print('My name is {}. I am {} years old. My income is {} BDT.'.format(name, age, income))

print('My name is {}'.format(input('Enter name: ')))