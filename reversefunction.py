# a program to check the function that reverses a user-defined value
number = int(input("Enter a number: "))

def reverse(n):
    rev = 0
    while n > 0:
        rem = n % 10
        rev = (rev * 10) + rem
        n = n // 10  # Use integer division
    return rev

rev = reverse(number)
print("Reverse of the given number is:", rev)
