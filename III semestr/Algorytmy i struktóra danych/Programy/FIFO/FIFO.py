class Node():
    """
    Klasa <code>Node</code> ma reprezentować pojemnik do przechowywania danych w abstralcyjnej strukturze danych
    (ADT-Abstract Data Type), która jest wykorzystywana przez klasę <code>FIFO</code> jako listę dowiązaną.
    @author Jakub Kozubek
    @version 1.0
    @see <a href="http://www.ift.uni.wroc.pl/~zkoza/dydaktyka/ksiazka/pointer/6list.html">Więcej o liście dowiązanej</a>
    """

    def __init__(self, item=None, nextNode=None, previousNode=None):
        """
        Konstruktor klasy <code>Node</code> ma 3 parametry startowe:
        <code>item</code>  (dana) reprezentuje pojemnik z konkretną daną do przechowania
        <code>nextNode</code> (następny korzeń) reprezentuje wskaźnik na następny pojemnik do przechowywania danych
        <code>previousNode</code> (poprzedni korzeń) reprezentuje wskaźnik na poprzedni pojemnik do przechowywania danych
        """
        self.item = item
        self.nextNode = nextNode
        self.previousNode = previousNode

    def __str__(self):
        """
        Funkcja wbudowana w pythona zwracająca element w postaci stringa
        """
        return str(self.item)


class FIFO():
    """
    Klasa <code>FIFO</code> ma reprezentować abstralcyjnej strukture danych (ADT-Abstract Data Type). Jest to akronim od
     słów First in, First out. Ta struktura to metoda organizowania manipulacji strukturą danych.
    @author Jakub Kozubek
    @version 1.0
    @see <a href="https://en.wikipedia.org/wiki/FIFO_(computing_and_electronics)">Więcej o liście dowiązanej</a>
    """
    def __init__(self):
        """
        Konstruktor klasy <code>FIFO</code> ma 3 parametry:
        <code>head</code> (głowa) reprezentuje pierwszy element wskazujący na klase <code>Node</code>
        <code>tail</code> (tył) reprezentuje ostatni element wskazujący na klase <code>Node</code>
        <code>size</code> (wielkość) reprezentuje ilość pojemników w liście dowiązanej
        """
        self.head = None
        self.tail = None
        self.size = 0

    def isEmpty(self):
        """
        Funkcja sprawdza czy lista jest pusta
        """
        return self.size == 0

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
            current.previousNode = newNode
            newNode.nextNode = current
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
            current.nextNode = newNode
            newNode.previousNode = current
        self.size += 1

    def delFirst(self):
        """
        Funkcja klasy <code>LinkedList</code> usuwa element z poczatku listy
        """
        try:
            if self.isEmpty():
                raise ValueError
            current = self.head
            self.head = current.nextNode
            self.size -= 1
            if self.isEmpty():
                self.tail = None
            return current.item
        except ValueError:
            return "Lista jest pusta !!"

    def delLast(self):
        """
        Funkcja klasy <code>LinkedList</code> usuwa element z konca listy
        """
        try:
            if self.isEmpty():
                raise ValueError
            current = self.tail
            if current.previousNode is None:
                self.head = None
                self.title = None
            self.size -= 1
            if self.isEmpty():
                self.head = None
            return current.item
        except ValueError:
            return "Lista jest pusta !!"

    def printFIFO(self):
        """
        Funkcja wypisuje wszystlie elementy listy dowiązanej
        """
        try:
            if self.isEmpty():
                raise ValueError
            current = self.head
            while current.nextNode is not None:
                print(" {} ".format(current.item), end="|")
                current = current.nextNode
            print(" {} ".format(current.item))
        except ValueError:
            return "Lista jest pusta !!!"
