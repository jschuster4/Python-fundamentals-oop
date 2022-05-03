class User: 
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return(self)

    def make_withdrawl(self, amount):
        self.account_balance -= amount
        return(self)

    def display_balance(self):
        print(self.account_balance)
        return(self)
        # why do I need a return self?

    def transfer_money(self, amount):
        self.make_withdrawl(amount)
        print("Name:", self.name, "balance", self.account_balance)
        Ashley.make_deposit(amount)
        print("Name:", Ashley.name, "balance:", Ashley.account_balance)
        



Joel = User("joel" , "joel@codingdojo.com")
Matt = User("Matt" , "matt@codingdojo.com") 
Ashley = User("Ashley" , "ashley@codingdojo.com")

Joel.make_deposit(100).make_deposit(200).make_deposit(300).make_withdrawl(400).display_balance()

Matt.make_deposit(500).make_deposit(300).make_withdrawl(600).make_withdrawl(100).display_balance()

Ashley.make_deposit(1000).make_withdrawl(200).make_withdrawl(100).make_withdrawl(260).display_balance()

Joel.transfer_money(100)
