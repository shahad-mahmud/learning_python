number_list = []
sum = 0

for i in range(1, 1001):
    number_list.append(i)
    sum += i * 3

print(sum)

for num in number_list:
    if num % 5 ==0:
        print(num, end= ' ')
print()
