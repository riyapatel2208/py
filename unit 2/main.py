from my_package import arithmetic
from my_package import string_operations
from my_package import list_operations

def main():
    # Using arithmetic functions
    print("Arithmetic Operations:")
    print("Add 5 + 3:", arithmetic.add(5, 3))
    print("Subtract 10 - 4:", arithmetic.subtract(10, 4))
    print("Multiply 6 * 7:", arithmetic.multiply(6, 7))
    print("Divide 8 / 2:", arithmetic.divide(8, 2))

    # Using string operations
    print("\nString Operations:")
    print("Uppercase 'hello':", string_operations.to_uppercase('Hello'))
    print("Reverse 'world':", string_operations.reverse_string('World'))
    print("Concatenate 'My' , 'Python' , 'Code' :", string_operations.concatenate('My ', 'Python ','Code'))

    # Using list operations
    my_list = [3, 1, 4, 2]
    print("\nList Operations:")
    print("Original list:", my_list)
    print("Sorted list:", list_operations.sort_list(my_list))
    print("Length of list:", list_operations.get_length(my_list))
    print("Append 5 to list:", list_operations.append_item(my_list, 5))
    print("Remove 3 from list:", list_operations.remove_item(my_list, 3))

if __name__ == "__main__":
    main()