import math


class TriangleExcept(Exception):
    pass


class Trojkat:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        try:
            if self.a > self.b + self.c:
                raise TriangleExcept("Długość a jest niepoprawna względem b i c")
            if self.b > self.a + self.c:
                raise TriangleExcept("Długość b jest niepoprawna względem a i c")
            if self.c > self.a + self.b:
                raise TriangleExcept("Długość c jest niepoprawna względem a i b")
        except TriangleExcept as error:
            print(error)
            print(f"Wartość jest niepoprawna")

    def circuit(self):
        return self.a + self.b + self.c

    def area(self):
        p = (self.a + self.b + self.c) / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))


triangle1 = Trojkat(7, 5, 1)
triangle2 = Trojkat(7, 5, 3)
print(triangle2.area())
print(triangle2.circuit())
