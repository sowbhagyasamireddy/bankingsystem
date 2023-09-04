class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Account Number: {self.account_number}\nAccount Holder: {self.account_holder}\nBalance: {self.balance}"


class Bank:
    def __init__(self):
        self.accounts = []

    def open_account(self, account_number, account_holder):
        account = BankAccount(account_number, account_holder)
        self.accounts.append(account)

    def get_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return None

    def close_account(self, account_number):
        account = self.get_account(account_number)
        if account:
            self.accounts.remove(account)
            return True
        return False

    def list_accounts(self):
        for account in self.accounts:
            print(account)
            print("-------------------")

    def modify_account(self, account_number, new_holder):
        account = self.get_account(account_number)
        if account:
            account.account_holder = new_holder
            return True
        return False


bank = Bank()

while True:
    print("1. Open Account")
    print("2. Deposit Amount")
    print("3. Withdraw Amount")
    print("4. Balance Enquiry")
    print("5. All Account Holder List")
    print("6. Close Bank Account")
    print("7. Modify Bank Account")
    print("8. Exit")
    
    choice = int(input("Enter your choice: "))

    if choice == 1:
        account_number = input("Enter account number: ")
        account_holder = input("Enter account holder's name: ")
        bank.open_account(account_number, account_holder)
        print("Account opened successfully!")

    elif choice == 2:
        account_number = input("Enter account number: ")
        account = bank.get_account(account_number)
        if account:
            amount = float(input("Enter deposit amount: "))
            if account.deposit(amount):
                print("Deposit successful!")
            else:
                print("Invalid deposit amount!")

    elif choice == 3:
        account_number = input("Enter account number: ")
        account = bank.get_account(account_number)
        if account:
            amount = float(input("Enter withdrawal amount: "))
            if account.withdraw(amount):
                print("Withdrawal successful!")
            else:
                print("Invalid withdrawal amount!")

    elif choice == 4:
        account_number = input("Enter account number: ")
        account = bank.get_account(account_number)
        if account:
            print(f"Account Balance: {account.get_balance()}")

    elif choice == 5:
        bank.list_accounts()

    elif choice == 6:
        account_number = input("Enter account number: ")
        if bank.close_account(account_number):
            print("Account closed successfully!")
        else:
            print("Account not found!")

    elif choice == 7:
        account_number = input("Enter account number: ")
        new_holder = input("Enter new account holder's name: ")
        if bank.modify_account(account_number, new_holder):
            print("Account holder modified successfully!")
        else:
            print("Account not found!")

    elif choice == 8:
        print("Exiting...")
        break

    else:
        print("Invalid choice! Please select a valid option.")

