# Write a function that will return the length of a string (do not use len() function)

def length(text):
    l = 0

    for char in text:
        l += 1
    return l

print(length('My name is Shahad.'))