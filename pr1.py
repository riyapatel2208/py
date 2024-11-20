def is_perfect(n):
    divisors = [i for i in range(1, n) if n % i == 0]
    return sum(divisors) == n, divisors

# Main program
while True:
    choice = input("Check a single number (s) or a range (r)? (or 'q' to quit): ").lower()
    
    if choice == 's':
        num = int(input("Enter a number: "))
        perfect, divisors = is_perfect(num)
        if perfect:
            print(f"{num} is a perfect number: {num} = {' + '.join(map(str, divisors))}")
        else:
            print(f"{num} is not a perfect number.")
    
    elif choice == 'r':
        start = int(input("Enter the starting range: "))
        end = int(input("Enter the ending range: "))
        perfect_numbers = []
        
        for num in range(start, end + 1):
            perfect, divisors = is_perfect(num)
            if perfect:
                perfect_numbers.append((num, divisors))
        
        if perfect_numbers:
            for num, divisors in perfect_numbers:
                print(f"{num} is a perfect number: {num} = {' + '.join(map(str, divisors))}")
        else:
            print(f"There are no perfect numbers between {start} and {end}.")
    
    elif choice == 'q':
        print("Exiting the program.")
        break
    
    else:
        print("Invalid choice. Please select 's' for single number, 'r' for range, or 'q' to quit.")
