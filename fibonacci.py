# Fibonacci series up to n terms
n = int(input("Enter any number: "))

a, b = 0, 1
print("Fibonacci Series:")

for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
