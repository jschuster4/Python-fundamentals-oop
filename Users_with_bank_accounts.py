class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate = 0, balance = 0): 
        self.int_rate = int_rate
        self.balance = balance
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        self.balance += amount
        return(self)
    def withdraw(self, amount):
        if self.balance > amount: 
            self.balance -= amount
        else: 
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return(self)
    def display_account_info(self):
        print("Balance: $" , self.balance)
        return(self)

    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance * self.int_rate + self.balance 
        return(self)
    
    # def print_info():
    #     print

# BankAccount1 = BankAccount(.1, 0)
# BankAccount2 = BankAccount(.2,0)

# BankAccount1.deposit(100).deposit(200).deposit(300).withdraw(300).yield_interest().display_account_info()
# BankAccount2.deposit(100).deposit(300).withdraw(50).withdraw(50).withdraw(100).withdraw(100).yield_interest().display_account_info()

class User: 
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount()

    def make_deposit(self, amount):
        self.account.balance += amount
        return(self)

    def make_withdrawl(self, amount):
        self.account.balance -= amount
        return(self)

    def display_balance(self):
        print(self.account.balance)
        return(self)
        # why do I need a return self?

    # def transfer_money(self, amount):
    #     self.make_withdrawl(amount)
    #     print("Name:", self.name, "balance", self.account)
    #     Ashley.make_deposit(amount)
    #     print("Name:", Ashley.name, "balance:", Ashley.account)
        

Joel = User("Joel", "joel@codingdojo.com")
Joel.make_deposit(100).make_withdrawl(50).display_balance()
