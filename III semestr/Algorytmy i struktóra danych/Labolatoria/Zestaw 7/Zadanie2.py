class Node():
    def __init__(self, item=None):
        """Klasa <code>Node</code> reprezentuje pojedyncze pudełko w pamięci, które umozliwia przechowywanie 1 elementu.

                Klasa składa się z 3 zmiennych lokalnych:
                - self.item = reprezentuje konkretny element w liście do przechowania
                - self.next = reprezentuje wskaźnik na następny element w liście, jeśli lista kończy się na tym elemencie
                wskaźnik self.next wskazuje na None, jeśli lista ma więcej elementów wskaźnik self.next wskazuje na następną
                klasę Node()
                - self.previous = reprezentuje wskaźnik na poprzedni element w liście"""
        self.item = item
        self.next = None
        self.previous = None


class Stos():
    """Klasa <code>Stos</code> reprezentuje listę jednokierunkową z możliwością wyznaczenia minimalnego elementu w
    liście"""

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        self.minimum = None

    def push(self, item):
        """Funkcja klasy <code>Stos</code> dodaje element na koniec stosu"""
        newNode = Node(item)
        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
            self.minimum = item
            newNode.previous = newNode
            self.size += 1
        else:
            newNode.previous = self.tail
            self.tail.next = newNode
            self.tail = newNode
            self.min(item)
            self.size += 1

    def pop(self):
        """Funkcja klasy <code>Stos</code> usuwa element z końca stosu"""
        if self.isEmpty():
            raise ValueError("Lista jest pusta !!")
        current = self.tail
        self.tail = current.previous
        self.tail.next = None
        self.size -= 1
        if self.isEmpty():
            self.head = None
            self.tail = None
        return current.item

    def top(self):
        """Funkcja klasy <code>Stos</code> zwraca element z końca stosu nie usuwając go"""
        current = self.pop()
        self.push(current)
        return current

    def min(self, item):
        """ Funcka klasy <code>Stos</code> sprawdza jaki element listy jest najmniejszy za każdym razem gdy dodajemy nowy
        element do stosu"""
        if self.minimum > item:
            self.minimum = item

    def getMin(self):
        """Funkcja klasy <code>Stos</code> zwraca minimalny element z stosu"""
        return self.minimum

    def isEmpty(self):
        """Funkcja sprawdza czy lista jest pusta"""
        return self.size == 0

    def print(self):
        """Funkcja wypisuje wszystlie elementy listy dowiązanej"""
        try:
            if self.isEmpty():
                raise ValueError("Lista jest pusta !!!")
            current = self.head
            while current.next is not None:
                print(" {} ".format(current.item), end="|")
                current = current.next
            print(" {} ".format(current.item))
        except ValueError:
            return False


stos = Stos()
stos.push(5)
stos.push(2)
stos.push(3)
stos.print()
print(stos.pop())
print(stos.pop())
print(stos.pop())
stos.push(4)
print(stos.top())
stos.push(5)
stos.push(2)
stos.push(3)
stos.print()
print(stos.getMin())
