import math


class liczbyZespolone():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_a(self):
        return self.a

    def get_b(self):
        return self.b

    def __add__(self, other):
        return self.get_a() + other.get_a(), self.get_b() + other.get_b()

    def __sub__(self, other):
        return self.get_a() - other.get_a(), self.get_b() - other.get_b()

    def __mul__(self, other):
        return (self.get_a() * other.get_a - self.get_b() * other.get_b,
                self.get_b() * other.get_a + self.get_a() * other.get_b)

    def __floordiv__(self, other):
        return ((self.get_a() * other.get_a + self.get_b() * other.get_b) / (pow(other.get_a, 2) + pow(other.get_b, 2)),
                (self.get_b() * other.get_a - self.get_a() * other.get_b) / (pow(other.get_a, 2) + pow(other.get_b, 2)))

    def modol(self):
        return math.sqrt(math.pow(self.get_a(), 2) + math.pow(self.get_b(), 2))

    def trygonometryczne(self):
        z = self.modol()*(math.cos(self.get_a()/self.modol())+(math.sin(self.get_b()/self.modol())))
        return z
