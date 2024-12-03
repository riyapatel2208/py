def is_perfect(n):
    divisors = [i for i in range(1, n) if n % i == 0]
    return sum(divisors) == n, divisors

while True:
    choice = input("Check a single number (s), a range (r), or 'q' to quit: ").lower()
    
    if choice == 's':
        num = int(input("Enter a number: "))
        perfect, divisors = is_perfect(num)
        print(f"{num} is a perfect number: {num} = {' + '.join(map(str, divisors))}" if perfect else f"{num} is not a perfect number.")
    
    elif choice == 'r':
        start = int(input("Enter the starting range: "))
        end = int(input("Enter the ending range: "))
        perfect_numbers = [(num, divisors) for num in range(start, end + 1) if (perfect := sum((i for i in range(1, num) if num % i == 0))) == num]
        
        if perfect_numbers:
            for num, divisors in perfect_numbers:
                print(f"{num} is a perfect number: {num} = {' + '.join(map(str, divisors))}")
        else:
            print(f"No perfect numbers between {start} and {end}.")
    
    elif choice == 'q':
        print("Exiting the program.")
        break
    
    else:
        print("Invalid choice. Please select 's', 'r', or 'q'.")
