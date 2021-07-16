class User:
    def __init__(self, username, email_address):# now our method has 2 parameters!
        self.name = username			# and we use the values passed in to set the name attribute
        self.email = email_address		# and the email attribute
        self.account = BankAccount(int_rate=0.02, balance=0)

    def make_deposit(self, amount):
            self.account.deposit(amount)
            return self
    
    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self

    
    def display_user_balance(self):
        print('User:',self.name,', Balance: ', self.account.balance)
        return self
    
    def transfer_money(self, other_user, amount):
        self.account.withdraw(amount)
        other_user.account.deposit(amount)
        return self

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

guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
ashwin = User("Ashwin Sathya", "ashwin@python.com")

guido.make_deposit(100).make_deposit(200).make_deposit(50).make_withdrawal(75).display_user_balance()

monty.make_deposit(100).make_deposit(200).make_withdrawal(50).make_withdrawal(75).display_user_balance()

ashwin.make_deposit(200).make_withdrawal(100).make_withdrawal(50).make_withdrawal(75).display_user_balance()

guido.transfer_money(ashwin,100).display_user_balance()
ashwin.display_user_balance()

