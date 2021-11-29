class ptak():
    def __init__(self, gatunek, szybkość):
        self.gatunek = gatunek
        self.szybkość = szybkość

    def lec(self):
        print("Tu", self.gatunek, ". Startuje, i zaraz osiągne prędkość", self.szybkość)

    def wydajOdglos(self):
        pass


class orzeł(ptak):
    def __init__(self, szybkość):
        super().__init__("orzeł", szybkość)

    def poluj(self):
        print("Tu", self.gatunek, ". Rozpoczołem polowanie")

    def wydajOdglos(self):
        print("wrrrr")


class pingwin(ptak):
    def __init__(self, szybkość):
        super().__init__("pingwin", szybkość)

    def slizgaj(self):
        print("Tu", self.gatunek, ". Rozpoczołem ślizg")

    def lec(self):
        print("Tu", self.gatunek, ". Przykro mi, ale nie latam")

    def wydajOdglos(self):
        print("kwiiiii")


ping = pingwin(5)
ping.slizgaj()
orz = orzeł(100)
orz.poluj()
orz.lec()