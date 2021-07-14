# f = open('files/file_write.txt', 'a')

# f.write('New line 1\n')
# f.write('How are you')

# f.close()

# write a program to
#   1. Open a file in write/append mode
#   2. Take 3 names as input in three times
#   3. Write the names in the file

f = open('files/input_names.txt', 'a')

for i in range(3):
    name = input('Enter a name: ')
    f.write(name + '\n')