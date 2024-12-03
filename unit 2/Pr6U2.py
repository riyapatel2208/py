import matrix_ops as mat_ops

while True:
    print("\nMatrix Operations Menu:")
    print("1. Initialize Matrix")
    print("2. Addition of Matrices")
    print("3. Multiplication of Matrices")
    print("4. Print Matrices")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    # Validate the choice input
    if choice.isdigit() and 1 <= int(choice) <= 5:
        choice = int(choice)
        if choice == 1:
            mat_ops.Initialize_matrix()
        elif choice == 2:
            mat_ops.Addition_matrix()
        elif choice == 3:
            mat_ops.Multiplication_matrix()
        elif choice == 4:
            mat_ops.print_matrix()
        elif choice == 5:
            print("Exiting...")
            break
    else:
        print("Invalid input! Please enter a number between 1 and 5.")