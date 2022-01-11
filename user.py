class User:
    bank_name = "First National Dojo"
    def __init__(self , name, email_address):
        self.name = name
        self.email = email_address
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
    
    def make_withdrawal(self, amount):
        self.account_balance -= amount

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")

    def transfer_money(self, amount, reciever):
        self.account_balance -= amount
        reciever.account_balance += amount


guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
vogard = User("Vogard Fyrion", "vogard@python.com")

print(guido.name)	# output: Guido van Rossum
print(monty.name)	# output: Monty Python

guido.make_deposit(100)
guido.make_deposit(200)
guido.make_deposit(423)
guido.make_withdrawal(50)

monty.make_deposit(50)
monty.make_deposit(127)
monty.make_withdrawal(62)
monty.make_withdrawal(12)

vogard.make_deposit(400)
vogard.make_withdrawal(147)
vogard.make_withdrawal(23)
vogard.make_withdrawal(176)

guido.display_user_balance()
monty.display_user_balance()
vogard.display_user_balance()

guido.transfer_money(300, vogard)

guido.display_user_balance()
vogard.display_user_balance()