"""
4. Tuples
 Write a Python function that:
 ● Takes a tuple of integers as input.
 ● Returns a new tuple with only the even numbers from the original
 tuple.
 ● Converts the tuple into a list and adds a new element to it.
"""



def filter_even_number_from_tuple(numbers):
    even_nums = ()
    for number in numbers:
        if number % 2 == 0:
            even_nums += (number,)
        continue
    
    return even_nums

def convert_tuple_into_list(tuple1):
    return list(tuple1)


def add_new_element_into_list(list1, new_element):
    list1.append(new_element)

    return list1

def take_int_input_into_tuple():
    elements = tuple(map(int, input("Enter the integers separated by comma: ").split(",")))

    return elements


numbers = take_int_input_into_tuple()
even_numbers_only = filter_even_number_from_tuple(numbers)
nums = convert_tuple_into_list(numbers)

new_nums = add_new_element_into_list(nums, 24)

#displaying the result
print("\n*****DISPLAYING THE RESULTS*****")
print(f"\nOriginal Tuple: {numbers}")
print(f"Filtered tuple (even numbers only): {even_numbers_only}")
print(f"Converted tuple into list: {nums}")
print(f"Adding new element into list: {new_nums}")