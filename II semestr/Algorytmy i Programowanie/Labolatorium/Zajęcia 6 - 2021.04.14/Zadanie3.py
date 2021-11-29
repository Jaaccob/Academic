from random import random


class Person(object):
    def __init__(self, name, lastName, street, houseNumber, postalCode):
        self.name = name
        self.lastName = lastName
        self.street = street
        self.houseNumber = houseNumber
        self.postalCode = postalCode


class Account(Person):
    def __init__(self, name, lastName, street, houseNumber, postalCode):
        super(Account, self).__init__(name, lastName, street, houseNumber, postalCode)
        self.amount = 0
        self.PINNumber = int(random() * 100000)
        print(f"Twoj numer Pin to: {self.getPINNumber()}. Czy chcesz go zmienić ?\n")
        print("T/N")
        if input().upper() == "T":
            self.chancePINNumber()

    def paymentOnAccount(self, amount):
        self.setAmount(self.amount + amount)

    def paymentToAccount(self, amount):
        if self.getAmount() - amount < 0:
            print("Brak środków na koncie")
            return False
        else:
            self.setAmount(self.getAmount() - amount)

    def chancePINNumber(self):
        print("Podaj swój numer PIN")
        PIN = input()
        while len(PIN) != 5:
            if len(PIN) > 5:
                print("Za długi PIN")
            else:
                print("Za krótki PIN")
            PIN = input()
        self.setPINNumber(PIN)

    def getAmount(self):
        return self.amount

    def getPINNumber(self):
        return self.PINNumber

    def setPINNumber(self, PINNumber):
        self.PINNumber = PINNumber

    def setAmount(self, amount):
        self.amount = amount


class SavingAccount(Account):
    def __init__(self, name, lastName, street, houseNumber, postalCode):
        super(SavingAccount, self).__init__(name, lastName, street, houseNumber, postalCode)
        income = 0.02


kontoOszczednosciowe = SavingAccount("Jakub", "Kozubek", "Nowa", 937, "34-381")
kontoOszczednosciowe.paymentOnAccount(100)
kontoOszczednosciowe.paymentToAccount(150)
print(kontoOszczednosciowe.PINNumber)
kontoOszczednosciowe.chancePINNumber()
