class Osoba:
    def __init__(self, imie, nazwisko, pesel):
        self.imie = imie
        self.nazwisko = nazwisko
        self.pesel = pesel

    @property
    def imie(self):
        return self.__dict__['imie']

    @property
    def nazwisko(self):
        return self.__dict__['nazwisko']

    @property
    def pesel(self):
        return self.__dict__['pesel']

    @imie.setter
    def imie(self, imie):
        if isinstance(imie, str):
            self.__dict__['imie'] = imie
        else:
            raise ValueError("Zmienna 'imie' powinna być stringiem")

    @nazwisko.setter
    def nazwisko(self, nazwisko):
        if isinstance(nazwisko, str):
            self.__dict__['nazwisko'] = nazwisko
        else:
            raise ValueError(f"Zmienna 'nazwisko' powinna być stringiem")

    @pesel.setter
    def pesel(self, pesel):
        if isinstance(pesel, int):
            self.__dict__['pesel'] = pesel
        else:
            raise ValueError("Zmienna 'pesel' powinna być intem")
