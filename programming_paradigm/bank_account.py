class BankAccount:
    def __init__(self, inital_balance=0):
        self.account_balance = inital_balance

    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount

        else:
            print('Deposit amount must be positive.')

    def withdraw(self, amount):
        if 0 < amount <= self.account_balance:
            self.account_balance -= amount
            # print(f'Withdrew: {amount}')
            return True  # main.py prints "Withdrew: $..."
        return False 


    def display_balance(self):
        print(f"Current Balance: ${self.account_balance:.2f}")
