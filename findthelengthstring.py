# Program to find the length of a string using for loop
str_input = input('Enter the word without space: ')

def find_len(s):
    counter = 0
    for i in s:
        counter += 1
    return counter

length = find_len(str_input)
print(f"The length of the string is: {length}")
