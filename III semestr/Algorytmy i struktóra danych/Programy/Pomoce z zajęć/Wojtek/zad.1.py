# coding: utf-8
# Prosta implementacja stosu jako Abstrakcyjnej Struktury Danych (ADT-Abstract Data Type)
# stos zaimplementowany jako lista dowiazana (linked list)
# materialy do wykladu AiSD, Michal Baczynski

class _StackNode():
    """prywatna klasa wezel"""
    def __init__(self, item):
        self.dane = item
        self.next = None

class LinkedList():
    """Implementacja stosu za pomoca listy dowiazanej z wykorzystaniem klasy wezel"""
    def __init__(self):
        """iicjalizacja"""
        self._head = None
        self._size = 0

    def insert(self, element):
        """wlozenie elementu na stos"""
        nowy = _StackNode(element)      # tworzymy nowy wezel
        nowy.next = self._head          # podwiazujemy pod niego aktualna glowe (czyli nasz stos)
        self._head = nowy               # glowa staje sie ten nowy wezel
        self._size += 1                 # zwiekszamy rozmiar stosu
        return

    def isEmpty (self):
        """sprawdzenie czy stos jest pusty"""
        return self._size == 0
        # lub
        # return self.head is None

    def size (self):
        """zwraca rozmiar stosu"""
        return self._size

    def push (self,element):
        """wlozenie elementu na stos"""
        nowy = _StackNode (element)
        nowy.next = self._head
        if self._head is None:
            self._head = nowy
        else:
            self._tail.next = nowy

        self._tail = nowy
        return

    def pop (self):
        """sciagniecie elementu ze stosu"""
        if self.isEmpty ():
            print ("operacja pop - Stos jest pusty!!!")
            return False  # ewentualnie wywolaj wyjatek np. assert
            # assert not self.isEmpty(), "Stos jest PUSTY!!!"
        self._head = self._head.next  # glowa staje sie nastepny wezel po aktualnej glowie
        # w niektorych jezykach programowania trzeba samodzielnie zwolnic pamiec, np. w C++ operacja delete
        self._size -= 1  # zmniejszamy rozmiar stosu
        return

    def top (self):
        """zwrocenie eleemntu ze szczytu stosu"""
        if self.isEmpty ():
            print ("operacja top - Stos jest pusty!!!")
            return False  # ewentualnie wywolaj wyjatek
        return self._head.dane  # zwracamy konkretna dane z naszej glowy

    def przesuniecie(self):
        print(self._head)
        zmienna = self._head
        poprzedni = None
        while zmienna.next is not None:  #Szukamy ostatniego elementu
            poprzedni = zmienna
            zmienna = zmienna.next
        poprzedni.next = None #Zmieniamy w ostatniej liczbie na None
        zmienna.next = self._head
        self._head = zmienna
        print(self._head)

s = LinkedList ()
for i in range(30):
    s.push(i)
#s.przesuniecie()