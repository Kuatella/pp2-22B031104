# 5
class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        return self.balance + amount

    def withdraw(self, amount):
        if amount <= self.balance:
             return self.balance - amount
        else:
            print("Transaction is impossible")


my_acc = Account("Kuk", 100)

my_acc.deposit(100)
my_acc.withdraw(3000)
