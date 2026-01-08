# Simple Banking System
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance
    #New Feature
    def transfer(self, target_account, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            target_account.balance += amount
            print(f"Transferred ${amount} to {target_account.account_holder}")
            print(f"Your new balance: ${self.balance}")
        else:
            print("Insufficient funds or invalid amount!")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid amount!")
            
    def add_interest(self, rate):
        if rate > 0:
            interest = self.balance * (rate / 100)
            self.balance += interest
            print(f"Interest of ${interest:.2f} added at rate {rate}%. New balance: ${self.balance:.2f}")
        else:
            print("Invalid interest rate!")


    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. Remaining balance: ${self.balance}")
        else:
            print("Insufficient funds or invalid amount!")

    def check_balance(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Current Balance: ${self.balance}")

    def transfer(self, target_account, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            target_account.balance += amount
            print(f"Transferred ${amount} to {target_account.account_holder}")
            print(f"Your new balance: ${self.balance}")
        else:
            print("Insufficient funds or invalid amount!")

def main():
    print("Welcome to the Python Bank!")
    name = input("Enter your name: ")
    account = BankAccount(name)

    while True:
        print("\n--- Menu ---")
        print("1. Deposit funds")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Transfer to Friend")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif choice == '2':
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        elif choice == '3':
            account.check_balance()
        elif choice == '4':
            target_account = BankAccount("Friend")  # Dummy friend account
            amount = float(input("Enter amount to transfer: "))
            account.transfer(target_account, amount)
        elif choice == '5':
            print("Thank you for banking with us!")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
