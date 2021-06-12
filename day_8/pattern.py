# nested loop

number_of_rows = 5

for row in range(number_of_rows):
    for column in range(row + 1):
        print('r = {} c = {}; '.format(row, column), end=' ')
    print()