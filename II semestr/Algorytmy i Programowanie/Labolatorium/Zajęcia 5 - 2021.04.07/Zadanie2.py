import datetime
import pickle


class Book():
    def __init__(self, ISBN, title, releaseDate, category):
        self.ISBN = ISBN
        self.title = title
        self.releaseDate = releaseDate
        self.category = category

    def getISBN(self):
        return self.ISBN

    def getTitle(self):
        return self.title

    def getReleaseDate(self):
        return self.releaseDate

    def getCategory(self):
        return self.category

    def __str__(self):
        return "ISBN: " + str(self.ISBN) + "\nTitle: " + self.title + "\nRelease date: " + str(
            self.releaseDate) + "\nCategory: " + self.category + "\n"


class Base():
    def __init__(self):
        self.dictionary = {}

    def addBook(self, book):
        self.dictionary[book.getISBN()] = book

    def printTitle(self):
        for i in range(len(self.dictionary)):
            print(list(self.dictionary.values())[i].getTitle())

    def toFile(self, name='plik'):
        with open(f'{name}.p', 'wb') as file:
            pickle.dump(self.dictionary, file)

    def fromFile(self, name):
        with open(f'{name}.p', 'rb') as file:
            self.dictionary = pickle.load(file)

    def __str__(self):
        date = ""
        for i in range(len(self.dictionary)):
            date += str(list(self.dictionary.values())[i].__str__())
        return date


bookOne = Book(9788328333130, "Wzorce projektowe. Elementy oprogramowania obiektowego wielokrotnego użytku",
               datetime.datetime(year=2010, month=9, day=21), "Programowanie")
bookTwo = Book(9788328375178, "Data Science w Pythonie. Kurs video. Przetwarzanie i analiza danych",
               datetime.datetime(year=2020, month=9, day=29), "Programowanie")

baza = Base()
# baza.addBook(bookOne)
# baza.addBook(bookTwo)
# baza.printTitle()
# baza.toFile()
baza.fromFile('plik')
print(baza)
