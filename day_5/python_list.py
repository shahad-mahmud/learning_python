# bangla_mark_saba = 89
# bangla_mark_shafin = 50
# bangla_mark_pinki = 85
# bangla_mark_fahim = 82
# bangla_mark_shahad = 33 

# meutable

# write a code to-
# a. create a list to store the age of at least 5 people
# b. Check the type of your created list
# c. Print the 3rd and 4th element
# d. Change the value of the 3rd element and print it. 
# e. Add a new student's number at the end of the list
# f. Print the lenght of the current list. 
# g. Print the number of the last student
# h. Print the number of 3rd, 4th and 5th students.

# creating list
mark = [89, 50, 85, 82, 33, 56, 9, 87, 56]
print(mark[7])

# changing element
mark[7] = -89
print(mark[7])

# adding at the end
mark.append(45)
print(mark)

# lenght of a list
list_lenght = len(mark)
print(list_lenght)

# negative indexing
print('Last element with positive indexing: ', mark[list_lenght -1])
print('Last element with negative indexing: ', mark[-1])

print('second last element: ', mark[-2])

# slicing
print(mark[2:4])

# inserting
print('Before inserting: ', mark)
mark.insert(4, 91)
print('After inserting: ', mark)

# removing an elemnet
# remove(element)
mark.remove(-89)
print(mark)

# del variable
del mark[4]
print(mark)

# sorting 
mark.sort(reverse=True)
print(mark)
