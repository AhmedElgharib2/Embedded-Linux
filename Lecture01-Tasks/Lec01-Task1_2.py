# Second Task in task 1
# Write a Python program to test whether a passed letter is a vowel or not.

def isVowel(letter):
    vowels = "aeiou"
    if letter.lower() in vowels:
        return True
    else:
        return False

# Taking the user input
letter = input("Enter a letter: ")

# Validate the input
if len(letter) != 1 or not letter.isalpha():
    print("Please enter a valid single alphabetic character.")
else:
    if isVowel(letter):
        print(f"The letter '{letter}' is a vowel.")
    else:
        print(f"The letter '{letter}' is not a vowel.")
