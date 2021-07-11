# modes: 
#   1. Read (r) -> Opens a file to read. Raises error if file not available
#   2. Write (w) -> Opens a file to write. Creates if not available
#   3. Append (a) -> Opens a file to append. Creates if not available
#   4. Create (x) -> Creates a file. Raises an error if file already available

f = open('sample.txt', 'r')

file_data = f.read(5)
print(file_data)

file_data = f.read(5)
print(file_data)

f.seek(0)
file_data = f.read(10)
print(file_data)

f.seek(27)
file_data = f.read(10)
print(file_data)

print(f.tell())

f.close()

# write a program to-
#   1. Open a file in read mode.
#   2. Read first 15 data.
#   3. Move 8 positons.
#   4. Read more 13 data.
#   5. Print the current cursor position.