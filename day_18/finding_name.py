name = input('Enter you name: ')
is_found = False

name_file = open('names1.txt', 'r')

for name_line in name_file:
    names_in_line = name_line.strip().split()
    
    for n in names_in_line:
        if name == n:
            is_found = True
            break
        
if is_found:
    print('Name found in the file')
else:
    print('Name not found in the file')