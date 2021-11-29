import math


class Prostokat():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_a(self):
        return self.a

    def get_b(self):
        return self.b

    def set_a(self, a):
        self.a = a

    def set_b(self, b):
        self.b = b

    def długoscBokow(self):
        bokA = math.sqrt(math.pow(self.a[0] - self.b[0], 2) + math.pow(self.a[1] - self.a[1], 2))
        bokB = math.sqrt(math.pow(self.a[0] - self.a[0], 2) + math.pow(self.a[1] - self.b[1], 2))
        return (bokA, bokB)

    def wspWierzcholkow(self):
        print("Wierzchołek C wynosi ({},{})".format(self.b[0], self.a[1]))
        print("Wierzchołek D wynosi ({},{})".format(self.a[0], self.b[1]))

    def area(self):
        return self.długoscBokow()[0] * self.długoscBokow()[1]

    def circuit(self):
        return (2 * self.długoscBokow()[0]) + (2 * self.długoscBokow()[1])

    def diagonal(self):
        return math.sqrt(math.pow(self.długoscBokow()[0], 2) + math.pow(self.długoscBokow()[1], 2))

    def middle(self):
        return (self.a[0] + (self.długoscBokow()[0]) / 2, self.a[1] + (self.długoscBokow()[1]) / 2)

    def __str__(self):
        return "({},{}),({},{})".format(self.a[0], self.a[1], self.b[0], self.b[1])

    def __eq__(self, other):
        if self.długoscBokow()[0] == other.długoscBokow()[0] and self.długoscBokow()[1] == other.długoscBokow()[1]:
            return True
        elif self.długoscBokow()[0] == other.długoscBokow()[1] and self.długoscBokow()[1] == other.długoscBokow()[0]:
            return True
        else:
            return False


pro = Prostokat((1, 2), (5, 7))
print(pro)
pro.długoscBokow()
pro.wspWierzcholkow()
print(pro.area())
print(pro.middle())
print(str(pro))
pro1 = Prostokat((2, 4), (5, 7))
print(pro.__eq__(pro1))
print(pro == pro1)
print(pro.a)
