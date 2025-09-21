class BankAccount:
    def __init__(self, account_number, account_holder, initial_balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be greater than 0.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than 0.")
        elif amount > self.balance:
            print("Insufficient funds. Withdrawal canceled.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")

    def display_details(self):
        print("\n--- Account Details ---")
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.account_holder}")
        print(f"Current Balance: ${self.balance:.2f}")
        print("------------------------\n")

# Example usage:
if __name__ == "__main__":
    # Creating an account
    account = BankAccount("123456789", "Alice Johnson", 1000)

    # Displaying initial details
    account.display_details()

    # Depositing money
    account.deposit(500)

    # Attempt to deposit invalid amount
    account.deposit(-50)

    # Withdrawing money
    account.withdraw(300)

    # Attempt to withdraw more than balance
    account.withdraw(1500)

    # Displaying final details
    account.display_details()
