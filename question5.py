"""
5. Dictionaries (Basics)
 Write a Python program that:
 ● Creates a dictionary with keys as numbers from 1 to 5 and values as
 their squares.
 ● Prints all the keys and values.
 ● Updates the value of key 3 to 27.
 ● Deletes the key 5 from the dictionary.
"""


def create_dict(keys, values):
    return dict(zip(keys, values))


def display_dict(dict_1):
    for key, value in dict_1.items():
        print(f"{key} : {value}")
    

def update_dict(dict_1, key, value):
    dict_1.update({key : value})

    for key, value in dict_1.items():
        print(f"{key} : {value}")


def del_key_from_dict(dict_1, key):
    del dict_1[key]

    for key, value in dict_1.items():
        print(f"{key} : {value}")




#creating dictionary
numbers = list(map(int, input("Enter the numbers separated by comma: ").strip().split(",")))
squares = [number ** 2 for number in numbers]

numbers_squares_mapping = create_dict(numbers, squares)
# print(numbers_squares_mapping)

#displaying all the keys and values
print("\nDisplaying dictionary:")
display_dict(numbers_squares_mapping)


#displaying updated dictionary:
print(f"\nAfter updating the value of key 3 to 27:")
update_dict(numbers_squares_mapping, 3, 27)


print(f"\nAfter deleting key \"5\":")
del_key_from_dict(numbers_squares_mapping, 5)


# print(numbers_squares_mapping)



    



