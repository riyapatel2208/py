class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        self.__account_number = account_number
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.__balance:
                self.__balance -= amount
                print(f"Withdrawn: {amount}")
            else:
                print("Insufficient balance.")
        else:
            print("Withdrawal amount must be positive.")

    def get_balance(self):
        return self.__balance


if __name__ == "__main__":
    account_number = input("Enter account number: ")
    initial_balance = float(input("Enter initial balance: "))
    my_account = BankAccount(account_number, initial_balance)

    while True:
        print("\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            amount = float(input("Enter amount to deposit: "))
            my_account.deposit(amount)
        elif choice == "2":
            amount = float(input("Enter amount to withdraw: "))
            my_account.withdraw(amount)
        elif choice == "3":
            print(f"Current Balance: {my_account.get_balance()}")
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")