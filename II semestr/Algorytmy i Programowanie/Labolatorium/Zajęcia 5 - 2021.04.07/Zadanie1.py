class Osoba():
    def __init__(self, ID, name, surName):
        self.ID = ID
        self.name = name
        self.surName = surName
        self.setDay(int(self.ID[4] + self.ID[5]))
        self.setMonth(int(self.ID[2] + self.ID[3]))
        self.setYear(int(self.ID[0] + self.ID[1]))

    def setDay(self, day):
        self.day = day

    def setMonth(self, month):
        self.month = month

    def setYear(self, year):
        self.year = year

    def __str__(self):
        return self.ID + " " + str(self.day) + " " + str(self.month) + " " + str(self.year)


person = Osoba("99071103673", "Jakub", "Kozubek")
print(person)
