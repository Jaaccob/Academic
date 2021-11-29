import math


class Prostokat():
    """Obiekt <code>Prostokat</code> reprezentuje prostokąt w układzie kartezjańskim
    Obiekt jest reprezentowany przez 3 parametry
    :param <code>a</code> (Współrzędne punktu) reprezentuje współrzędne lewego dolnego punktu w układzie kartezjańskim
    :type list
    :param <code>w<code> (Szerokość) reprezentuje szerokość jednego z boków od punktu <code>a</code>
    :type int
    :param <code>h</code> (Wysokość) reprezentuje wysokość jednego z boków od punktu <code>a</code>
    """

    def __init__(self, a, w, h):
        """Konstruktor obiektu <code>Prostokąt</code>
        """
        self.a = a
        self.w = w
        self.h = h

    def get_a(self):
        """Metoda <code>get_a</code> zwraca współrzędne """
        return self.a

    def get_w(self):
        """Metoda <code>get_w</code> zwraca szerokość"""
        return self.w

    def get_h(self):
        """Metoda <code>get_h</code> zwraca wysokość"""
        return self.h

    def wspWierzcholkow(self):
        """Metoda <code>wspWierzchołkow</code> zwraca na standardowy strumień danych wyściowych informacje o położeniu reszty współrzędnych obiektu Prostokat w układzie kartezjańskim"""
        print("Współrzędne wierzchołka A: ({},{})".format(self.get_a()[0], self.get_a()[1]))
        print("Współrzędne wierzchołka B: ({},{})".format(self.get_a()[0] + self.get_w(), self.get_a()[1]))
        print(
            "Współrzędne wierzchołka C: ({},{})".format(self.get_a()[0] + self.get_w(), self.get_a()[1] + self.get_h()))
        print("Współrzędne wierzchołka D: ({},{})".format(self.get_a()[0], self.get_a()[1] + self.get_h()))

    def area(self):
        """Metoda <code>area</code> zwraca pole powierzchni prostokąta"""
        return self.get_h() * self.get_w()

    def circuit(self):
        """Metoda <code>circuit</code> zwraca objętość prostokąta"""
        return self.get_h() * 2 + self.get_w() * 2

    def diagonal(self):
        """Metoda <code>diagonal</code> zwraca długość przekątnej prostokąta"""
        return math.pow(self.get_w(), 2) + math.pow(self.get_h(), 2)

    def middle(self):
        """Metoda <code>middle</code> zwraca współrzędne środka prostokąta"""
        return (self.get_a()[0] + (self.get_w() / 2), self.get_a()[1] + (self.get_h() / 2))

    def __str__(self):
        """Metoda <code>___str___</code> zwraca reprezentacje stringową dla obiektu"""
        return "({},{}),{},{}".format(self.get_a()[0], self.get_a()[1], self.get_w(), self.get_h())


pro1 = Prostokat((20, 70), 50, 10)
pro1.wspWierzcholkow()
print(type((3, 1)))
