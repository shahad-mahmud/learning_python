# 0 1 1 2 3 5 8 13 21.....

# first and second elements are fixed
# first element = 0
# second element = 1
# n_th element is the summation of (n-1)_th element and
# (n-2)_th element; n >= 3, n is natural number

# n = 4
# (n-1) = 4 - 1 = 3rd
# (n - 2) = 4 - 2 = 2nd

first_e = 0
second_e = 1
n_elements = 2

print(first_e, second_e, end=' ')

while n_elements <= 10:
    current_e = second_e + first_e
    print(current_e, end=' ')

    first_e = second_e  # keep the second element in the fist element
    second_e = current_e  # keep the current element in the second element
    n_elements += 1

