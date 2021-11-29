from datetime import datetime


class Song():
    def __init__(self, author, title, yearOfWriting, length):
        self.author = author
        self.title = title
        self.yearOfWriting = yearOfWriting
        self.length = length

    def getLength(self):
        return self.length

    def getYearOfWriting(self):
        return self.yearOfWriting

    def getTitle(self):
        return self.title

    def getAuthor(self):
        return self.author

    def setTitle(self, title):
        self.title = title

    def setAuthor(self, author):
        self.author = author

    def setYearOfWriting(self, yearOfWriting):
        self.yearOfWriting = yearOfWriting

    def setLength(self, length):
        self.length = length

    def __str__(self):
        return f'Tytuł piosenki: {self.title}\n' \
               f'Autorem jest: {self.author}\n' \
               f'Rok napisania: {self.yearOfWriting}\n' \
               f'Długość: {self.length}\n'

    def __repr__(self):
        return f'Song (title = {self.title}, author = {self.author}, yearOfWriting = {self.yearOfWriting}, length = {self.length})'


class Disc():
    def __init__(self, title, length=0, numberOfSong=0, publicationDate=datetime.today()):
        self.title = title
        self.length = length
        self.numberOfSong = numberOfSong
        self.publicationDate = publicationDate
        self.song = []

    def addSong(self, SongClass):
        self.song.append(SongClass)
        self.length += SongClass.getLength()
        self.numberOfSong += 1
        if self.publicationDate > SongClass.getYearOfWriting():
            date = SongClass.getYearOfWriting()
            self.publicationDate = date

    def printTitle(self):
        for i in self.song:
            print(i.getTitle())

    def songExist(self, SongClass):
        for i in self.song:
            if i == SongClass:
                return True
        return False

    def __str__(self):
        return f'Tytuł albumu: {self.title}\n' \
               f'Ilość piosenek: {self.numberOfSong}\n' \
               f'Data wydania: {self.publicationDate}\n' \
               f'Długość: {self.length}\n'


piosenkaOne = Song('Justin Bimber', 'Yummy', datetime(year=2020, month=1, day=4), 3.51)
print(piosenkaOne)
piosenkaTwo = Song('Sanah', 'Szampan', datetime(year=2020, month=1, day=3), 3.18)
print(piosenkaTwo)

album = Disc('Zwykły album')
print(album)

album.addSong(piosenkaOne)
print(album)
print(album.songExist(piosenkaTwo))
album.addSong(piosenkaTwo)
print(album)
print(album.songExist(piosenkaOne))