"""
6. String and Dictionary Combination
 Write a Python function that:
 ● Takes a string as input.
 ● Counts the frequency of each character in the string and stores it in a
 dictionary.
 ● Ignores spaces and considers case-insensitive comparisons.
"""


def count_char(string1):
    char_count = {}
    
    for char in string1:
        if char == " ":
            continue
        else:
            char_count.update({char.lower() : string1.count(char)})

    # print(char_count)
    for char, number in char_count.items():
        print(f"Number of {char}'s : {number}")

#asking user for input
input_string = input("Enter a string: ")

#calling the function
print("\nDISPLAYING THE NUMBER OF EACH CHAR IN THE GIVEN STRING IGNORING SPACES AND CONSIDERING SPACE INSENSITIVE COMPARISONS:")
print(f"\nGiven String: {input_string}\n")
count_char(input_string)



