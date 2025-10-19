from abc import ABC, abstractmethod

# 🔹 1. Abstraction
class Account(ABC):
    def __init__(self, account_number, balance):
        # 🔹 2. Encapsulation (Private variables)
        self.__account_number = account_number
        self.__balance = balance

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    def show_balance(self):
        print(f"Account {self.__account_number} balance: ₹{self.__balance}")

    # Encapsulated getter & setter
    def _get_balance(self):
        return self.__balance

    def _set_balance(self, new_balance):
        self.__balance = new_balance


# 🔹 3. Inheritance
class SavingsAccount(Account):
    def deposit(self, amount):
        new_balance = self._get_balance() + amount
        self._set_balance(new_balance)
        print(f"₹{amount} deposited successfully!")

    def withdraw(self, amount):
        if amount <= self._get_balance():
            new_balance = self._get_balance() - amount
            self._set_balance(new_balance)
            print(f"₹{amount} withdrawn successfully!")
        else:
            print("Insufficient balance!")


class CurrentAccount(Account):
    def deposit(self, amount):
        new_balance = self._get_balance() + amount
        self._set_balance(new_balance)
        print(f"₹{amount} deposited in current account!")

    def withdraw(self, amount):
        if amount <= self._get_balance() + 5000:  # overdraft allowed
            new_balance = self._get_balance() - amount
            self._set_balance(new_balance)
            print(f"₹{amount} withdrawn successfully (overdraft allowed)!")
        else:
            print("Withdrawal limit exceeded!")


# 🔹 4. Polymorphism
accounts = [
    SavingsAccount("SAV123", 10000),
    CurrentAccount("CUR456", 20000)
]

for acc in accounts:
    acc.show_balance()
    acc.deposit(5000)
    acc.withdraw(3000)
    acc.show_balance()
    print("---------------")
