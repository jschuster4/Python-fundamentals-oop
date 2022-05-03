class User: 
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdrawl(self, amount):
        self.account_balance -= amount

    def display_balance(self):
        print(self.account_balance)

    def transfer_money(self, amount):
        self.make_withdrawl(amount)
        print("Name:", self.name, "balance", self.account_balance)
        Ashley.make_deposit(amount)
        print("Name:", Ashley.name, "balance:", Ashley.account_balance)
        



Joel = User("joel" , "joel@codingdojo.com")
Matt = User("Matt" , "matt@codingdojo.com") 
Ashley = User("Ashley" , "ashley@codingdojo.com")

Joel.make_deposit(100)
Joel.make_deposit(200)
Joel.make_deposit(300)
Joel.make_withdrawl(400)
Joel.display_balance()

Matt.make_deposit(500)
Matt.make_deposit(300)
Matt.make_withdrawl(600)
Matt.make_withdrawl(100)
Matt.display_balance()

Ashley.make_deposit(1000)
Ashley.make_withdrawl(200)
Ashley.make_withdrawl(100)
Ashley.make_withdrawl(260)
Ashley.display_balance()

Joel.transfer_money(100)