def sum(*nums: int) -> int:
    _sum = 0

    for num in nums:
        _sum += num

    return _sum

res = sum(1, 2, 3, 5)
print(res)


# Write a program to-
# 1. Declear a funtion which can take arbitary numbers of input
# 2. The input will be name of one or persons
# 3. In the function print a message to greet every one
