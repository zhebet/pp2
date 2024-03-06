class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"You have {self.balance} on your account")
        else:
            print("Funds unavailable!")


acc = Account("John", 1000)
acc.deposit(500)
acc.withdraw(200)
acc.withdraw(1000)  
