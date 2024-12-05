"""
3. Lists
 Write a Python function that:
 ● Accepts a list of integers as input. (use split method)
 ● Returns the largest and smallest number in the list.
 ● Removes duplicates from the list.
 ● Sorts the list in descending order.

"""

def find_largest_and_smallest_in_list(list1):
    largest_num = 0
    smallest_num = 0

    for number in list1:
        if number > largest_num:
            largest_num = number
        elif number < smallest_num:
            smallest_num = number
    
    return largest_num, smallest_num


def remove_duplicate_list_items(list1):
    return list(set(list1))


def sort_list_desc(list1):
    return sorted(list1, reverse=True)


    # sorted_list = list1.sort(reverse = True)
    # return sorted_list


#asking user for entering integers separated by comma
try:
    int_numbers = list(map(int, input("Enter the integers in list separated by comma: ").split(",")))

    largest_num, smallest_num = find_largest_and_smallest_in_list(int_numbers)
    filtered_numbers = remove_duplicate_list_items(int_numbers)
    desc_sorted_numbers = sort_list_desc(int_numbers)

    #displaying the result
    print(f"\n*****DISPLAYING THE RESULTS*****")
    print(f"\nOriginal List: {int_numbers}")
    print(f"Largest number: {largest_num}\nSmallest number: {smallest_num}")
    print(f"Filtered List (no duplicates): {filtered_numbers}")
    print(f"Sorted List (Descending): {desc_sorted_numbers}")


except ValueError as e:
    print(e)

finally:
    print("\nThank You!")    