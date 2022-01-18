from multiprocessing.managers import BaseManager


class BankAccount:
    accounts = []

    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance - amount <= 0:
            print("Insuffiecient funds: Charging a $5 fee.")
            self.balance = self.balance - 5 - amount
        else:
            self.balance -= amount
        return self

    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.int_rate * self.balance)
        return self

    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()


accnt1 = BankAccount(0.01, 100)
accnt2 = BankAccount(.05, 200)

accnt1.deposit(10).deposit(10).deposit(10).withdraw(
    50).yield_interest().display_account_info()

accnt2.deposit(100).deposit(100).withdraw(20).withdraw(20).withdraw(
    20).withdraw(20).yield_interest().display_account_info()

BankAccount.print_all_accounts()
