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
        if self.sprawdz_moc():
            pozycja = self.get_miejsce()[0]
            pozycja += down
            if pozycja > 8:
                pozycja = pozycja % 8
                self.doladuj_moc()
            moc = self.get_moc()
            moc -= down
            self.set_moc(moc)
            self.set_miejsce([pozycja, self.get_miejsce()[1]])

    def left(self, left):
        """Funkcja left przesuwa robota o określone pola w lewo
        :arg
        left(int): ilość pól o które robot ma się przesunąć"""
        if self.sprawdz_moc():
            pozycja = self.get_miejsce()[1]
            pozycja += left
            moc = self.get_moc()
            moc -= left
            self.set_moc(moc)
            if pozycja > 8:
                pozycja = pozycja % 8
            self.set_miejsce([self.get_miejsce()[0], pozycja])

    def sprawdz_moc(self):
        """Funkcja sprawdz_moc sprawdza czy moc robota nie spradła poniżej 0
        :return:
        bool: Zwraca True
        """
        if self.get_moc() <= 0:
            raise ValueError("Brak mocy")

        else:
            return True

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


robot = Robot("Robocik")
robot.down(3)
print(robot)
robot.left(5)
print(robot)
robot.down(7)
print(robot)
