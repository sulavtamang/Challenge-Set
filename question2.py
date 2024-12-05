"""
2. Strings
 Write a Python program that:
 ● Takes a string as input.
 ● Reverses the string.
 ● Counts the number of vowels (a, e, i, o, u) in the string.
 ● Converts the string to uppercase.
"""


def reverse_string(string1):
    return string1[::-1]


def count_vowel(string1):
    vowel_count = 0

    for char in string1:
        if char.lower() not in ("a", "e", "i", "o", "u"):
            continue

        vowel_count += 1
    
    return vowel_count


def string_to_uppercase(string1):
    return string1.upper()



input_string = input("Enter a string: ")

reversed_string = reverse_string(input_string)
no_of_vowels = count_vowel(input_string)
string_upper = string_to_uppercase(input_string)

#Now displaying the reverse, vowel count and uppercase string
print(f"\nOriginal String: {input_string}")
print(f"\nReversed String: {reversed_string}")
print(f"No. of vowels : {no_of_vowels}")
print(f"String in uppercase: {string_upper}")