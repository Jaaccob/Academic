import time
import random


class Baza:
    """
        Klasa Timer pozwala na utworzenie listy pomiarów czasu

        ...

        Attributes
        ----------

        Methods
        -------
        __str__(self):
            Zwraca listę wszystkich obiektów umieszczonych w bazie

        dodaj(self,obiekt):
            Dodaje obiekt Timer do bazy

        ile_obiektow(self):
            Zwraca ilość obiektów umieszczonych w klasie baza
    """

    def __init__(self):
        self.lista = []

    def dodaj(self, obiekt):
        self.lista.append(obiekt)

    def ile_obiektow(self):
        return len(self.lista)

    def __str__(self):
        string = f"Nazwy obiektów klasy zegar: \n"
        for i in self.lista:
            string += f"{i}"
        return string


class Timer:
    """
        Klasa Timer pozwala na utworzenie listy pomiarów czasu
        ...

        Attributes
        ----------
        nazwa : str/int
            Nazwa timera
        lista : list
            Zawiera listę pomiarów w danym timerze

        Methods
        -------
        __str__(self):
            Opis funkcji print

        set_lista(self,kanal):
            Zmienia ustawioną listę pomiarów

        get_lista(self):
            Zwraca listę pomiarów

        start(self,start=None):
            Zapisuje w zmiennej klasowej aktualny czas
            Po wywołaniu funkcji "stop" odejmuje od aktualnego czasu
            Czas poprzedni

        stop(self):
            Odwołuje się do klasy start
    """

    def __init__(self, nazwa, lista=None):
        self.nazwa = nazwa
        self.lista = []

    def __str__(self):
        string = f'Nazwa obiektu: {self.nazwa} \nPomiary: \n'
        for y in self.lista:
            string += f"{str(y)}\n"
        return string

    def start(self, start=None):
        if start == None:
            self.czas = time.time()
        elif start == "stop":
            timer = time.time() - self.czas
            self.lista.append(timer)

    def stop(self):
        self.start("stop")

    def get_nazwa(self):
        return self.nazwa

    def set_nazwa(self, nazwa):
        self.nazwa = nazwa

    def get_lista(self):
        return self.lista

    def set_lista(self, lista):
        self.lista = lista


def generuj_timer(ile):
    """
    Funkcja odpowiedzialna za tworzenie instancji klas Timer
    Attribute
    ---------
    param ile:
        Przymuje ile instancji klasy Timer ma wytworzyć
    Return
    ------
        Zwraca listę instancji klasy Timer
    """
    timer = 0
    lista = []
    for i in range(ile):
        lista.append(Timer(random.randint(0, 20)))
    return lista


inic = 0
baza = Baza()

zegar = Timer("zegar")
baza.dodaj(zegar)
zegar.start()
time.sleep(2)
zegar.stop()
print(zegar.lista)
zegar1 = Timer("zegar5")
baza.dodaj(zegar1)
zegar2 = Timer("zegar10")
baza.dodaj(zegar2)

for i in range(5):
    zegar.start()
    time.sleep(random.randint(0, 3))
    zegar.stop()

randomowe_zegary = generuj_timer(10)
for i in randomowe_zegary:
    baza.dodaj(i)

print(zegar)
zegar.set_nazwa("Zegarek")
print(zegar)
print(baza)
print("Liczba instancji: ", baza.ile_obiektow())
