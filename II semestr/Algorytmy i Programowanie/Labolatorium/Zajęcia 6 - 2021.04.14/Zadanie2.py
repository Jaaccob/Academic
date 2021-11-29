class Address():
    def __init__(self, street, houseNumber, postalCode):
        self.street = street
        self.houseNumber = houseNumber
        self.postalCode = postalCode

    def getStreet(self):
        return self.street

    def getHouseNumber(self):
        return self.houseNumber

    def getPostalCode(self):
        return self.postalCode

    def __str__(self):
        return f'Ulica i numer domu: {self.getStreet()} {self.getHouseNumber()}\n' \
               f'Kod pocztowy: {self.getPostalCode()}\n'


class Person():

    def __init__(self, name, lastName):
        self.name = name
        self.lastName = lastName

    def getName(self):
        return self.name

    def getLastName(self):
        return self.lastName

    def setName(self, name):
        self.name = name

    def setLastName(self, lastName):
        self.lastName = lastName

    def __str__(self):
        return f'Imie i Nazwisko: {self.getName()} {self.getLastName()}'


class Student(Person):
    def __init__(self, ID, name, lastName, street, houseNumber, postalCode):
        self.ID = ID
        super(Student, self).__init__(name, lastName)
        self.address = Address(street, houseNumber, postalCode)

    def getID(self):
        return self.ID

    def getAddress(self):
        return f'ID studenta: {self.getID()}\n' \
               f'Imie i Nazwisko: {super().getName()} {super().getLastName()}\n' \
               f'Ulica i numer domu: {self.address.getStreet()} {self.address.getHouseNumber()}\n' \
               f'Kod pocztowy: {self.address.getPostalCode()}\n'

    def genDocGoogle(self):
        dictionary = {'Args': [self.getID(), self.getName(), self.getLastName(), self.address.getStreet(),
                               self.address.getHouseNumber(), self.address.getPostalCode()]}
        print(dictionary)

    def __str__(self):
        return f'ID studenta: {self.getID()}\n' \
               f'{super().__str__()}\n' \
               f'{self.address.__str__()}\n'


studentJakub = Student(0, "Jakub", "Kozubek", "Nowa", 937, "34-381")
# print(studentJakub)
# print(studentJakub.getAddress())
studentJakub.genDocGoogle()
