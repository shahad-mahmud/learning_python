# score > 100, score < 0 -> invalid input
# score >= 80, a+

score = int(input('Enter a score'))

if score > 100:
    print('Invalid score. Please try again')
elif score >= 80:
    print('A+')
elif score >= 70:
    print('A')