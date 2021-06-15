# list meutable, string is immeutable

name = 'Thor'

# ------------string operations------------

# concatenation (join two strings)
first_name = 'Shahad'
second_name = 'Mahmud'

print(first_name, second_name)

full_name = first_name + ' ' + second_name
print(full_name)


# repeatation
print(first_name * 5)


# concatenation using parenthesis
paragraph = (
    'Hello! I am Shahad. '
    'My home town is Dinajpur. '
    'I studied at DZS.'
)

print(paragraph)

# membership checking
print('Sha' in first_name)


# get string length
print(len(first_name), len(second_name), len(full_name))


# formatting
print('My first name is {}'.format(first_name))


# way to write a string
str1 = '''Someting'''
str2 = "One more thing"
str3 = 'Some other thing'

print(type(str1))
print(type(str2))
print(type(str3))

print(str1 + str2 + str3)


# more functions
print(first_name)
print(first_name.upper())
print(first_name.lower())
