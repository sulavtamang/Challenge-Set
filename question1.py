"""
1. Numbers and Floats
 Write a Python function that takes two numbers (integers or floats) as input
 and returns:
 ● Their sum
 ● Their difference
 ● Their product
 ● Their division (handle the case where division by zero might occur).
"""


def compute_basic_math_operations(number1, number2):
    try:
        sum_result = number1 + number2
        diff_result = number1 - number2
        product_result = number1 * number2
        div_result = number1 / number2

        return sum_result, diff_result, product_result, div_result

    except ZeroDivisionError:
        print("\nThe divisor must be non-zero integer..")


    

try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    sum, diff, product, division = compute_basic_math_operations(num1, num2)

    print("\n*****DISPLAYING THE RESULT*****")

    print(f"\nSUM: {sum}")
    print(f"DIFFERENCE: {diff}")
    print(f"PRODUCT: {product}")
    print(f"DIVISION: {division}")

except ValueError:
     print("Please enter valid numbers like 1, 18, 4.5, 0, 34.9797....")

except ZeroDivisionError:
        print("\nThe divisor must be non-zero integer..")

except:
     print("\nAn unknown error occured.")

finally:
     print("\nThank You!!!!!!")