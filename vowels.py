# programm to check the given character is vowel or consonant

character = input("Enter a character: ")
vowels = ['a','e','i','o','u','A','E','I','O','U']
if character in vowels:
    print(f"The character '{character}' is vowel!")
else:
    print(f"The character '{character}' is consonant!")
