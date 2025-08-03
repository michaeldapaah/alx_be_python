class BankAccount:
    def __init__(self, inital_balance=0):
        self.account_balance = inital_balance

    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
            print(f'Deposited {amount}')

        else:
            print('Deposit amount must be positive.')

    def withdraw(self, amount):
        if 0 < amount <= self.account_balance:
            self.account_balance -= amount
            print(f'Withdrew {amount} from account.')

        else:
            print('Withdrawal amount must be positive and less than or equal to the account balance.')

    def display_balance(self):
        print(f'Current Balance: {self.account_balance}')
