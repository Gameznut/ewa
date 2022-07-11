from abc import ABC, abstractmethod


class Account(ABC):

    def __init__(self, ID: str, balance: float):
        self.id = ID
        self.balance = balance

    def getID(self):
        return f"ID: {self.id}"

    def getBalance(self):
        return f"Balance: {self.balance}"

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def deposit(self, amount):
        pass

    def __str__(self):
        return f"ID: {self.id}, Balance: {self.balance}"


class SavingAccount(Account):

    def __init__(self, ID: str, balance: float):
        super().__init__(ID, balance)

    def withdraw(self, amount):
        balance = self.balance - amount
        if balance > 10:
            self.balance = balance
        return bool(balance > 10)

    def deposit(self, amount):
        if amount > 0:
            self.balance = self.balance + amount
        else:
            "Can't be negative"
        return bool(amount > 0)


class CheckingAccount(Account):

    def __init__(self, ID: str, balance: float):
        super().__init__(ID, balance)

    def withdraw(self, amount):
        balance = self.balance - amount
        if balance > 0:
            self.balance = balance
        return bool(balance > 0)

    def deposit(self, amount):
        if amount > 0:
            self.balance = self.balance + amount
        return bool(amount > 0)


if __name__ == '__main__':
    a1 = SavingAccount("Trina", 105.00)
    a2 = CheckingAccount("Lena", 150)
    result = a1.withdraw(30.00)
    print(result)
    result = a2.deposit(50.00)
    print(result)
    print(a1)
    print(a2)


