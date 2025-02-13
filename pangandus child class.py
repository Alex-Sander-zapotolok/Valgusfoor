# Child Class
class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0

    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print("Account balance has been updated : €", self.balance)

    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print("Insufficient Euro | Balance Available : €", self.balance)
        else:
            self.balance = self.balance - self.amount
            print("Account balance has been updated : €", self.balance)

    def view_balance(self):
        self.show_details()
        print("Account balance: €", self.balance)