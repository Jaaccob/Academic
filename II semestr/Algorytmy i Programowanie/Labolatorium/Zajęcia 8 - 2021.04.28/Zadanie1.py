from random import randint


class Robot:
    """Obiekt Robot opisuje własności poruszającego się robota

    Args:
        nazwa (str): przechowuje nazwe robota
        start (tuple): przechowuje startowe położenie robota
        miejsce (list): przechowuje aktualne miejsce robota
        moc (int): przechowuje aktualną moc robota

    Attributes:
        nazwa: przechowuje nazwę robota
        start: przechowuje miejscec startowe robota. Początkowo startujemy w punkcie 0,0
        miejsce: przechowuje aktualną pozycje robota
        moc: przechowuje aktualną moc robota. Początkowo startujemy z mocą 9

        """

    def __init__(self, nazwa, start=(0, 0), moc=9):
        self.nazwa = nazwa
        self.start = start
        self.miejsce = list(start)
        self.moc = moc

    def down(self, down):
        """Funkcja down przesuwa robota o określone pola w dół
            :arg
            down(int): ilość pól o które robot ma się przesunąć"""
        if self.sprawdz_moc() and self.get_moc() - down >= 0:
            pozycja = self.get_miejsce()[0]
            pozycja += down
            if pozycja > 8:
                pozycja = pozycja % 8
                self.doladuj_moc()
            moc = self.get_moc()
            moc -= down
            self.set_moc(moc)
            self.set_miejsce([pozycja, self.get_miejsce()[1]])
        else:
            print("Brak możliwości ruchu")

    def left(self, left):
        """Funkcja left przesuwa robota o określone pola w lewo
        :arg
        left(int): ilość pól o które robot ma się przesunąć"""
        if self.sprawdz_moc() and self.get_moc() - left >= 0:
            pozycja = self.get_miejsce()[1]
            pozycja += left
            moc = self.get_moc()
            moc -= left
            self.set_moc(moc)
            if pozycja > 8:
                pozycja = pozycja % 8
            self.set_miejsce([self.get_miejsce()[0], pozycja])
        else:
            print("Brak możliwości ruchu")

    def sprawdz_moc(self):
        """Funkcja sprawdz_moc sprawdza czy moc robota nie spradła poniżej 0
        :return:
        bool: Zwraca True
        """
        try:
            if self.get_moc() <= 0:
                raise ValueError("Brak mocy")
            else:
                return True
        except:
            print("Brak mocy")
            return False

    def doladuj_moc(self):
        """Funkcja doladuj_moc dodaje 5 do mocy robota"""
        moc = self.get_moc()
        moc += 5
        self.set_moc(moc)

    def get_nazwa(self):
        return self.nazwa

    def get_start(self):
        return self.start

    def get_miejsce(self):
        return self.miejsce

    def get_moc(self):
        return self.moc

    def set_nazwa(self, nazwa):
        if isinstance(nazwa, str):
            self.nazwa = nazwa
        else:
            raise ValueError("Zmienna powinna być stringiem")

    def set_start(self, start):
        if isinstance(start, tuple):
            self.start = start
        else:
            raise ValueError("Zmienna powinna być tuplem")

    def set_miejsce(self, miejsce):
        if isinstance(miejsce, list):
            self.miejsce = miejsce
        else:
            raise ValueError("Zmienna powinna być tuplem")

    def set_moc(self, moc):
        if isinstance(moc, int):
            self.moc = moc
        else:
            raise ValueError("Zmienna powinna być intem")

    def __str__(self):
        return f'Nazwa: {self.get_nazwa()}\n' \
               f'Start: {self.get_start()}\n' \
               f'Miejsce: {self.get_miejsce()}\n' \
               f'Moc: {self.get_moc()}'


"""
### Zadanie 1
Wykorzystując klasę Robot - zaimplementuj bitwy robotów.
> Każdy z graczy ma 5 robotów. Osoby poruszają robotami na zmianę, jeżeli roboty spotkają się na jednym polu to  jeden 
przejmuje część energii drugiego (lub całą). Gdy moc robota się wyczerpie, automatycznie pojawia się drugi robot.

> lub zaimplemetuj bitwę w pełni losową.
"""


class RobotsBattle:
    def __init__(self):
        self.robotsOne = []
        self.robotsTwo = []
        for i in range(5):
            self.robotsOne.append(Robot(f"i robotsOne"))
            self.robotsTwo.append(Robot(f"i robotsTwo", (7, 7)))

    def battle(self):
        one = len(self.robotsOne) - 1
        two = len(self.robotsTwo) - 1
        while one >= 0 and two >= 0:
            if self.robotsOne[one].get_miejsce() == self.robotsTwo[two].get_miejsce():
                amountOfPower = randint(0, 9)
                power = self.robotsOne[one].get_moc() - amountOfPower
                self.robotsTwo[two].set_moc(amountOfPower - power + self.robotsTwo[two].get_moc())
                self.robotsOne[one].set_moc(amountOfPower - power + self.robotsOne[one].get_moc())
            if not self.robotsOne[one].sprawdz_moc():
                place = self.robotsOne[one].get_miejsce()
                one -= 1
                self.robotsOne[one].set_miejsce(place)
                print("Robot 1 traci życie")

            # Poruszanie się w dol pierwszego robota
            ilosc = randint(0, 9)
            self.robotsOne[one].down(ilosc)
            print(f"Robot 1 porusza się w dol na: {ilosc}")
            print(self.robotsOne[one].get_miejsce())

            # Poruszanie się w lewo pierwszego robota
            ilosc = randint(0, 9)
            self.robotsOne[one].left(ilosc)
            print(f"Robot 1 porusza się w lewo na: {ilosc}")
            print(self.robotsOne[one].get_miejsce())
            print(f"Zostalo mocy {self.robotsOne[one].get_moc()}")

            if self.robotsTwo[two].get_miejsce() == self.robotsOne[one].get_miejsce():
                amountOfPower = randint(0, 9)
                power = self.robotsTwo[two].get_moc() - amountOfPower
                self.robotsOne[one].set_moc(amountOfPower - power + self.robotsOne[one].get_moc())
                self.robotsTwo[two].set_moc(amountOfPower - power + self.robotsTwo[two].get_moc())
            if not self.robotsTwo[two].sprawdz_moc():
                place = self.robotsTwo[two].get_miejsce()
                two -= 1
                self.robotsTwo[two].set_miejsce(place)
                print("Robot 2 traci życie")

            # Poruszanie się w doł drugiego robota
            ilosc = randint(0, 9)
            self.robotsTwo[two].down(ilosc)
            print(f"Robot 2 porusza się w dol na: {ilosc}")
            print(self.robotsTwo[two].get_miejsce())

            # Poruszanie się w lewo drugiego robota
            ilosc = randint(0, 9)
            self.robotsTwo[two].left(ilosc)
            print(f"Robot 2 porusza się w lewo na: {ilosc}")
            print(self.robotsTwo[two].get_miejsce())
            print(f"Zostalo mocy {self.robotsTwo[two].get_moc()}")

        if one > 0:
            print("Robot 1 wygrał")
        else:
            print("Robot 2 wygrał")


walkaRobotow = RobotsBattle()
walkaRobotow.battle()
