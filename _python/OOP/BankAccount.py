class BankAccount:
    def __init__(self, int_rate = 0.03, balance = 0): 
        self.interest_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if(self.balance - amount >= 0):
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        print('Balance:',self.balance)
        return self

    def yield_interest(self):
        if(self.balance > 0):
            self.balance += (self.interest_rate * self.balance)
        return self

account1 = BankAccount(0.05,200)
account2 = BankAccount()

account1.deposit(100).deposit(100).deposit(100).withdraw(50).yield_interest().display_account_info()

account2.deposit(300).deposit(300).withdraw(100).withdraw(50).withdraw(50).withdraw(50).yield_interest().display_account_info()


