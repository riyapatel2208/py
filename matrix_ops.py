def initialize_matrix(rows, cols):
    matrix = []
    print(f"Enter the elements row by row (for a {rows}x{cols} matrix):")
    for i in range(rows):
        row = list(map(int, input(f"Row {i+1}: ").split()))
        # Ensure correct number of columns
        while len(row) != cols:
            print(f"Error: You must enter exactly {cols} numbers.")
            row = list(map(int, input(f"Row {i+1}: ").split()))
        matrix.append(row)
    return matrix

# Function to print a matrix
def print_matrix(matrix):
    print("Matrix:")
    for row in matrix:
        print(" ".join(map(str, row)))

# Function to add two matrices
def add_matrices(matrix1, matrix2):
    # Check if matrices have the same dimensions
    if len(matrix1) == len(matrix2) and len(matrix1[0]) == len(matrix2[0]):
        result = []
        for i in range(len(matrix1)):
            row = [matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))]
            result.append(row)
        return result
    else:
        print("Error: Matrices must have the same dimensions for addition.")
        return None

# Function to multiply two matrices
def multiply_matrices(matrix1, matrix2):
    # Check if matrices can be multiplied
    if len(matrix1[0]) == len(matrix2):
        result = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]

        for i in range(len(matrix1)):
            for j in range(len(matrix2[0])):
                for k in range(len(matrix2)):
                    result[i][j] += matrix1[i][k] * matrix2[k][j]

        return result
    else:
        print("Error: The number of columns in Matrix 1 must equal the number of rows in Matrix 2 for multiplication.")
        return None




