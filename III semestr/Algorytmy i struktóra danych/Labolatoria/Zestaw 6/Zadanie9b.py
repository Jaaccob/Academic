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


class LinkedList():
    """
    Klasa <code>LinkedList</code> reprezentuje listę dowiązaną dwukierunkową, która umożliwia przechowywanie elementów
    w pamięci. Klasa ma możliwość zwalniania i dodawanie elementów z 2 stron kolejki.
    """

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def addFirst(self, item):
        """
        Funkcja klasy <code>LinkedList</code> dodaje element na początek listy
        """
        newNode = Node(item)  # Zmienna z nowym "pudełkiem" przechowującym nowy item
        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
        else:
            current = self.head
            self.head = newNode
            current.previous = newNode
            newNode.next = current
        self.size += 1

    def addLast(self, item):
        """
        Funkcja klasy <code>LinkedList</code> dodaje element na koniec listy
        """
        newNode = Node(item)  # Zmienna z nowym "pudełkiem" przechowującym nowy item
        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
        else:
            current = self.tail
            self.tail = newNode
            current.next = newNode
            newNode.previous = current
        self.size += 1

    def delFirst(self):
        """
        Funkcja klasy <code>LinkedList</code> usuwa element z poczatku listy
        """
        try:
            if self.isEmpty():
                raise ValueError("Lista jest pusta !!")
            current = self.head
            self.head = current.next
            self.size -= 1
            if self.isEmpty():
                self.tail = None
            return current.item
        except ValueError:
            return False

    def delLast(self):
        """
        Funkcja klasy <code>LinkedList</code> usuwa element z konca listy
        """
        try:
            if self.isEmpty():
                raise ValueError("Lista jest pusta !!")
            current = self.tail
            self.tail = current.previous
            self.tail.next = None
            if self.isEmpty():
                self.head = None
            return current.item
        except ValueError:
            return False

    def isEmpty(self):
        """
        Funkcja sprawdza czy lista jest pusta
        """
        return self.size == 0

    def print(self):
        """
        Funkcja wypisuje wszystlie elementy listy dowiązanej
        """
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


list = LinkedList()
list.addFirst(5)
list.addFirst(4)
list.print()
list.addLast(7)
list.addLast(12)
list.print()
print(list.delFirst())
list.print()
print(list.delFirst())
print(list.delFirst())
print(list.delFirst())
print("Lista zawiera :")
print(list.isEmpty())
list.addFirst(5)
list.addFirst(4)
list.print()
list.addLast(7)
list.addLast(12)
list.print()
print(list.delLast())
list.print()