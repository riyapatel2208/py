def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1  

user_input = input("Enter a sorted list of numbers (separated by spaces): ")
arr = user_input.split()  

for i in range(len(arr)):
    arr[i] = int(arr[i])

if arr != sorted(arr):
    print("The list must be sorted for binary search.")
else:
    target = int(input("Enter the number to search: "))
    result = binary_search(arr, target)
    if result != -1:
        print(f"Element is present at index {result}")
    else:
        print("Element is not present in the array")
