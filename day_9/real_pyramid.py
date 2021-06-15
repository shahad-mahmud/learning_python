total_row_num = 5

for row in range(1, total_row_num + 1):
    space_needed = total_row_num - row
    print(' ' * space_needed, end='')
    for col in range(row):
        print('* ', end='')
    print()