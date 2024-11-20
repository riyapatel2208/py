import matrix_ops

def get_matrix_input(name):
    rows = int(input(f"Enter the number of rows for {name}: "))
    cols = int(input(f"Enter the number of columns for {name}: "))
    return matrix_ops.initialize_matrix(rows, cols)

while True:
    print("\nMatrix Operations:")
    print("1. Initialize and Print a Matrix")
    print("2. Add Two Matrices")
    print("3. Multiply Two Matrices")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        matrix = get_matrix_input("Matrix")
        matrix_ops.print_matrix(matrix)

    elif choice == '2':
        print("Matrix 1:")
        matrix1 = get_matrix_input("Matrix 1")
        print("Matrix 2:")
        matrix2 = get_matrix_input("Matrix 2")

        result = matrix_ops.add_matrices(matrix1, matrix2)
        if result is not None:
            print("Result of Matrix Addition:")
            matrix_ops.print_matrix(result)

    elif choice == '3':
        print("Matrix 1:")
        matrix1 = get_matrix_input("Matrix 1")
        print("Matrix 2:")
        matrix2 = get_matrix_input("Matrix 2")

        result = matrix_ops.multiply_matrices(matrix1, matrix2)
        if result is not None:
            print("Result of Matrix Multiplication:")
            matrix_ops.print_matrix(result)

    elif choice == '4':
        print("Exiting...")
        break

    else:
        print("Invalid choice! Please try again.")