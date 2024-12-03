import academic

while True:
    print("\nOptions:")
    print("1. Add a course")
    print("2. Drop a course")
    print("3. Print academic record")
    print("4. Calculate CGPA")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5): ")
    
    if choice == '1':
        name = input("Enter course name: ")
        credits = float(input("Enter course credits: "))
        points = float(input("Enter earned points: "))
        academic.add_course(name, credits, points)
        
    elif choice == '2':
        name = input("Enter course name to drop: ")
        academic.drop_course(name)
        
    elif choice == '3':
        academic.print_record()
        
    elif choice == '4':
        academic.calculate_cgpa()
        
    elif choice == '5':
        print("Exiting...")
        break
        
    else:
        print("Invalid choice! Please try again.")