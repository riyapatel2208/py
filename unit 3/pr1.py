class Person:
    def __init__(self, name, country, day, month, year):
        self.name = name
        self.country = country
        self.day_of_birth = day
        self.month_of_birth = month
        self.year_of_birth = year

    def calculate_age(self, current_day, current_month, current_year):
        age = current_year - self.year_of_birth
        if (current_month, current_day) < (self.month_of_birth, self.day_of_birth):
            print("Age is not calculated. Please check your entered information.")
        return age

if __name__ == "__main__":
    name = input("Enter your name: ")
    country = input("Enter your country: ")
    day_of_birth = int(input("Enter your birth day (DD): "))
    month_of_birth = int(input("Enter your birth month (MM): "))
    year_of_birth = int(input("Enter your birth year (YYYY): "))

    person = Person(name=name, country=country, day=day_of_birth, month=month_of_birth, year=year_of_birth)

    current_day = int(input("Enter the current day (DD): "))
    current_month = int(input("Enter the current month (MM): "))
    current_year = int(input("Enter the current year (YYYY): "))

    age = person.calculate_age(current_day, current_month, current_year)
    print(f"{person.name} from {person.country} is {age} years old.")
