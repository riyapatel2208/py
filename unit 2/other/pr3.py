def print_list_recursive(lst):
    if lst==[]: 
        print("List is empty") 
        return
    print(lst[0])
    print_list_recursive(lst[1:])

user_input = input("Enter a list of elements separated by spaces: ")
user_list = user_input.split()  

if user_list:
    print("List elements are:")
    print_list_recursive(user_list)  # Print the list recursively
else:
    print("List is empty")  # Handle case when the list is empty
