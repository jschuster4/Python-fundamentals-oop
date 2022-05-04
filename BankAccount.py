class BankAccount:
    all_accounts = []
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate = 0, balance = 0): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)
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

    @classmethod
    def print_info(cls):
        for i in cls.all_accounts:
            i.display_account_info()



BankAccount1 = BankAccount(.1, 0)
BankAccount2 = BankAccount(.2,0)

BankAccount1.deposit(100).deposit(200).deposit(300).withdraw(300).yield_interest().display_account_info()
BankAccount2.deposit(100).deposit(300).withdraw(50).withdraw(50).withdraw(100).withdraw(100).yield_interest().display_account_info()

BankAccount.print_info()