# a program to check if a 3-digit number is an Armstrong number
num = int(input('Enter any positive number: '))
sum = 0
original = num

while original > 0:
    digit = original % 10
    sum += digit ** 3
    original //= 10  # Use integer division

if num == sum:
    print('Number is Armstrong')
else:
    print('Number is not Armstrong')
