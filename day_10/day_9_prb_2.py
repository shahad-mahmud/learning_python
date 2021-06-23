# Write a function that will return the oddly positioned characters

# B a n g l a d e s h
# 1 2 3 4 5 6 7 8 9 10 


def odd_cherecters(word):
    odd_chars = []

    for i in range(len(word)):
        if i % 2 == 0:
            odd_chars.append(word[i])

    return odd_chars


text = 'Bangladesh'
print(odd_cherecters(text))