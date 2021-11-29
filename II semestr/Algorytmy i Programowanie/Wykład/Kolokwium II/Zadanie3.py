class Telewizor():
    """
    Klasa telewizor przechowuje dane związane z obsługą telewwizora.
    ...

    Attributes
    ----------
    kanal_set : str/int
        Kanał który jest ustawiony
    kanal_list : list
        Lista dostępnych kanałów

    Methods
    -------
    info(additional=""):
        Prints the person's name and age.
    __str__(self):
        Opis funkcji print

    set_kanal_set(self,kanal):
        Zmienia ustawiony kanał

    get_kanal_set(self):
        Zwraca ustawiony kanal

    dostepne_kanaly(self):
        Zwraca dostępne kanały

    save(self):
        Zapisuje do pliku aktualną listę kanałów

    def read(self,plik):
        Zczytuje z danego pliku listę kanałów.

    """

    def __init__(self, kanal_set=None, kanal_list=None):
        self.kanal_set = kanal_set
        print('Telewizor włączony', '\nUstawiony kanał: TVP1')
        self.kanal_list = kanal_list

    def __str__(self):
        return (f"Oglądasz kanał {self.kanal_set}")

    def set_kanal_set(self, kanal):
        if isinstance(kanal, (str, int)):
            self.kanal_set = kanal
        else:
            print("Podano złą wartość dla kanału")

    def get_kanal_set(self):
        print(f"Aktualny kanał: {self.kanal_set}")
        return self.kanal_set

    def dostepne_kanaly(self):
        tekst = 'Dostępne kanały:\n'
        for i in self.kanal_list:
            tekst += i + "\n"
        print(tekst)
        return tekst

    def save(self):
        with open('kanal.txt', 'w') as lista_kanalow:
            lista_kanalow.write(f"#{self.kanal_set}\n")
            for i in self.kanal_list:
                lista_kanalow.write(f"{i}\n")
            lista_kanalow.close()

    def read(self, plik):
        if isinstance(plik, str):
            kanaly = open(plik, 'r')
            tekst = kanaly.read()
            lista = tekst.split()

            if lista[0][0] == "#":
                self.kanal_set = lista[0][1:]
                self.kanal_list = lista[1:]
            else:
                raise ValueError("Wczytano zły plik!")


telewizor = Telewizor("POLSAT", ['TVP', 'POLSAT', 'TVN'])
telewizor.dostepne_kanaly()
telewizor.set_kanal_set("Ziemniak")
telewizor.get_kanal_set()
print(telewizor)
telewizor.save()

telewizor2 = Telewizor()
telewizor2.read('kanal.txt')
telewizor2.get_kanal_set()
telewizor2.dostepne_kanaly()