# mat_ops.py (renamed module for matrix operations)

a = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # Initialize 3x3 matrix a
b = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # Initialize 3x3 matrix b

# Initialize matrices with user input
def Initialize_matrix():
    global a, b
    print("Initialize First Matrix")
    for i in range(3):
        for j in range(3):
            while True:
                value = input(f"Enter value for a[{i}][{j}]: ")
                if value.isdigit() or (value[0] == '-' and value[1:].isdigit()):  # Check if input is a valid integer
                    a[i][j] = int(value)
                    break
                else:
                    print("Invalid input! Please enter an integer.")
                
    print("Initialize Second Matrix")
    for i in range(3):
        for j in range(3):
            while True:
                value = input(f"Enter value for b[{i}][{j}]: ")
                if value.isdigit() or (value[0] == '-' and value[1:].isdigit()):  # Check if input is a valid integer
                    b[i][j] = int(value)
                    break
                else:
                    print("Invalid input! Please enter an integer.")

# Print matrices a and b
def print_matrix():
    print("First Matrix:")
    for i in range(3):
        for j in range(3):
            print(f" {a[i][j]:3}", end=" ")
        print()

    print("Second Matrix:")
    for i in range(3):
        for j in range(3):
            print(f" {b[i][j]:3}", end=" ")
        print()

# Addition of matrices with dimension control
def Addition_matrix():
    print("Addition of Matrices:")
    # Ensure both matrices have the same dimension (3x3 in this case)
    if len(a) == len(b) and len(a[0]) == len(b[0]):
        for i in range(3):
            for j in range(3):
                print(f" {a[i][j] + b[i][j]:3}", end=" ")
            print()
    else:
        print("Matrices must have the same dimensions for addition.")

# Multiplication of matrices with dimension control
def Multiplication_matrix():
    print("Multiplication of Matrices:")
    # Ensure the number of columns in a is equal to the number of rows in b
    if len(a[0]) == len(b):
        for i in range(3):
            for j in range(3):
                mul = 0
                for k in range(3):
                    mul += a[i][k] * b[k][j]
                print(f" {mul:3}", end=" ")
            print()
    else:
        print("Number of columns in the first matrix must equal the number of rows in the second matrix for multiplication.")
