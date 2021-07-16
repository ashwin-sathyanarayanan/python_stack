class User:
    def __init__(self, username, email_address):# now our method has 2 parameters!
        self.name = username			# and we use the values passed in to set the name attribute
        self.email = email_address		# and the email attribute
        self.account_balance = 0		# the account balance is set to $0, so no need for a third parameter

    def make_deposit(self, amount):
            self.account_balance += amount
    
    def make_withdrawal(self, amount):
        self.account_balance -= amount
    
    def display_user_balance(self):
        print('User:',self.name,', Balance: ', self.account_balance)


guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
ashwin = User("Ashwin Sathya", "ashwin@python.com")
print(guido.name)	# output: Guido van Rossum
print(monty.name)	# output: Monty Python


guido.make_deposit(100)
guido.make_deposit(200)
guido.make_deposit(50)
guido.make_withdrawal(75)
print(guido.account_balance)
monty.make_deposit(100)
monty.make_deposit(200)
monty.make_withdrawal(50)
monty.make_withdrawal(75)
print(monty.account_balance)
ashwin.make_deposit(200)
ashwin.make_withdrawal(100)
ashwin.make_withdrawal(50)
ashwin.make_withdrawal(75)
print(ashwin.account_balance)

guido.display_user_balance()

