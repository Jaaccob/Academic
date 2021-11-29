import Stack

Stos = Stack.Stack


class Queue():
    def __init__(self):
        self.stackOne = Stos()
        self.stackTwo = Stos()

    def enQueue(self, item):
        """
        Funkcja <code>enQueue</code> dodaje element do kolejki,
        Funkcja ma złożoność O(1)
        :param item: element, który chcemy dodać do kolejki
        """
        currentOne = self.stackOne
        currentOne.push(item)

    def deQueue(self):
        """
        Funkcja <code>deQueue</code> zwraca pierwszy element w kolejce
        Funkcja działa na zasadzie 2 stosów czyli za każdym razem gdy chcemy ściągnąć 1 element z stosu musimy przenieść
        wszystkie elementy na 2 stos. Złożoność tego algorytmu wynosi O(n+1+n-1) = O(2n)
        :return: Zwraca 1 element z kolejki
        """
        currentOne = self.stackOne
        currentTwo = self.stackTwo
        while currentOne.isEmpty() is False:
            currentTwo.push(currentOne.pop())
        x = currentTwo.pop()
        while currentTwo.isEmpty() is False:
            currentOne.push(currentTwo.pop())
        return x


kolejka = Queue()
kolejka.enQueue(3)
kolejka.enQueue(2)
kolejka.enQueue(5)
print(kolejka.deQueue())
print(kolejka.deQueue())
print(kolejka.deQueue())
