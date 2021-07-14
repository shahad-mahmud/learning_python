name = input('Enter you name: ')
is_found = False

name_file = open('names.txt', 'r')

for line in name_file:    
    if line.strip() == name: 
        is_found = True
        break
    
if is_found:
    print('Name found in the file')
else:
    print('Name not found in the file')
    