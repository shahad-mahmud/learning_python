# first way, range(n): 1 parameter
# starts from zero, ends in (n-1)
for i in range(10):
    print(i, end=' ')
print()

# second way, range(start, stop)
for num in range(10, 21):
    print(num, end=' ')
print()

# second way, range(start, stop, step)
for j in range(1, 30, 2):
    print(j, end=' ')
print()

# using for loop, print 10 to 1
for i in range(10, 0, -1):
    print(i, end=' ')