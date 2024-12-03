def print_list_recursive(lst):
    if not lst: 
        print("List is empty")
        return
    print(lst) 
    return

user_input = input("Enter a list of elements separated by spaces: ")
user_list = user_input.split()  

if user_list:
    print("List elements are:")
    print_list_recursive(user_list)  
else:
    print("List is empty")  
