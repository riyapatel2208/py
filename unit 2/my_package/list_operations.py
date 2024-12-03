# my_package/list_operations.py

def get_length(lst):
    return len(lst)

def append_item(lst, item):
    lst.append(item)
    return lst

def remove_item(lst, item):
    if item in lst:
        lst.remove(item)
    return lst

def sort_list(lst):
    return sorted(lst)