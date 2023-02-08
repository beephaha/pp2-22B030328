class account:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance
    def deposit(self, dep):
        self.balance += dep
        print("accepted")
    def withdraw(self, withdraw):
        if withdraw > self.balance:
            print("request exceeds the current balance")
        else:
            self.balance -= withdraw
        return self.balance
owner = account("beep",15000)
print(owner.withdraw(10000))
print(owner.deposit(5000))