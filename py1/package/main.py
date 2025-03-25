# main.py

from my_package import arithmetic_ops
from my_package import string_ops
from my_package import list_ops

def main():
    # Arithmetic operations
    print("Arithmetic Operations:")
    print("Addition (5 + 7):", arithmetic_ops.add(5, 7))
    print("Subtraction (10 - 4):", arithmetic_ops.subtract(10, 4))
    print("Multiplication (3 * 6):", arithmetic_ops.multiply(3, 6))
    print("Division (8 / 2):", arithmetic_ops.divide(8, 2))
    print("Division (8 / 0):", arithmetic_ops.divide(8, 0))  # Division by zero test

    # String operations
    print("\nString Operations:")
    string_example = "radar"
    print("Capitalized:", string_ops.capitalize_string(string_example))
    print("Reversed:", string_ops.reverse_string(string_example))
    print("Number of vowels in 'education':", string_ops.count_vowels("education"))
    print(f"Is '{string_example}' a palindrome?:", string_ops.is_palindrome(string_example))

    # List operations
    print("\nList Operations:")
    my_list = [1, 2, 3, 4, 5, 5, 6, 1, 3]
    print("Max value:", list_ops.max_value(my_list))
    print("Min value:", list_ops.min_value(my_list))
    print("Sum of list:", list_ops.sum_list(my_list))
    print("Unique items in list:", list_ops.unique_items(my_list))

if __name__ == "__main__":
    main()
