""" This is the bank inheritance file """
class BankAccount:
    """ This is the BankAcount parent class """
    def __init__(self, interest_rate=.02):
        self.balance = 0
        self.interest_rate = interest_rate

    def deposit(self, amount):
        """ This is the depost parent function """
        if amount < 0:
            return False
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        """ This is the withdraw parent function """
        if amount < 0:
            return False
        self.balance -= amount
        return amount

    def accumulate_interest(self):
        """ This is the accumulate_interest parent function """
        self.balance += self.balance * self.interest_rate

class ChildrensAccount(BankAccount):
    """ This is the ChildrensAccount child class """
    def __init__(self):
        self.interest_rate = 0
        super().__init__(self.interest_rate)

    def accumulate_interest(self):
        self.balance += 10

class OverdraftAccount(BankAccount):
    """ This is the OverdraftAccount child class """
    def __init__(self, interest_rate=.02, overdraft_penalty=40):
        super().__init__(interest_rate)
        self.overdraft_penalty = overdraft_penalty

    def withdraw(self, amount):
        if amount > self.balance:
            self.balance -= self.overdraft_penalty
            return False

            #use the inherited withdraw method if the user
            #has enough money
        return super().withdraw(amount)
    def accumulate_interest(self):
        if self.balance <= 0:
            return False

        return super().accumulate_interest()

basic_account = BankAccount()
basic_account.deposit(600)
print("Basic account has ${}".format(basic_account.balance))
basic_account.withdraw(17)
print("After withdraw, Basic account has ${}".format(basic_account.balance))
basic_account.accumulate_interest()
print("Basic account has ${}".format(basic_account.balance))
print()

childs_account = ChildrensAccount()
childs_account.deposit(34)
print("Child's account has ${}".format(childs_account.balance))
childs_account.withdraw(17)
print("Child's account has ${} after withdraw".format(childs_account.balance))
childs_account.accumulate_interest()
print("Child's account has ${} after interest accumulation".format(childs_account.balance))
print()

overdraft_account = OverdraftAccount()
overdraft_account.deposit(12)
print("Overdraft account has ${}".format(overdraft_account.balance))
overdraft_account.withdraw(17)
print("Overdraft account has ${} after withdraw".format(overdraft_account.balance))
overdraft_account.accumulate_interest()
print("Overdraft account has ${} after interest accumulation".format(overdraft_account.balance))
