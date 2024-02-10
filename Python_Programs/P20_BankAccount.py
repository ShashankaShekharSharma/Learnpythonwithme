class BankAccount:
    def __init__(self, account_holder, initial_balance=0.0):
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        try:
            amount = float(amount)
            if amount > 0:
                self.balance += amount
                print(f"Deposited ${amount}. New balance: ${self.balance:.2f}")
            else:
                print("Invalid deposit amount. Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    def withdraw(self, amount):
        try:
            amount = float(amount)
            if amount > 0 and amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew ${amount}. New balance: ${self.balance:.2f}")
            elif amount <= 0:
                print("Invalid withdrawal amount. Please enter a positive number.")
            else:
                print("Insufficient funds for withdrawal.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    def check_balance(self):
        print(f"Account balance for {self.account_holder}: ${self.balance:.2f}")

def main():
    print("Welcome to the Bank!")
    account_holder = input("Enter your name: ")
    initial_balance = float(input("Enter initial balance (or 0 for no initial deposit): "))

    # Create a bank account
    account = BankAccount(account_holder, initial_balance)

    while True:
        print("\nMain Menu:")
        print("1. Deposit funds")
        print("2. Withdraw funds")
        print("3. Check balance")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            amount = input("Enter the amount to deposit: ")
            account.deposit(amount)
        elif choice == '2':
            amount = input("Enter the amount to withdraw: ")
            account.withdraw(amount)
        elif choice == '3':
            account.check_balance()
        elif choice == '4':
            print("Exiting the program. Thank you for using our bank services!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
