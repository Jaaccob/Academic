class Node():
    def __init__(self, item=None):
        self.item = item  # 2 atrybuty,dane,połączenie(droga do następnego pudełka)
        self.next = None  # połączenie; jaką daną mamy mieć, jaka jest droga do następnego pudełka


class LinkedList():  # Połączenie ze sobą elementów
    """
    Klasa <code>LinkedList</code> reprezentuje stos przedstawiony za pomocą tablic dowiązanych
    Implementacja tego stosu nie posiada wcześniej zadeklarowanej wielkości. Istnieje więc możliwość nadpisania
    elementu przez inny gdy pamięć operacyjna komputera zostanie przepełniona.
    Złożoność czasowa tego algorytmu wynosi :
    Przy dodawaniu nowego elementu = O(1);
    Przy ściąganiu elementu = O(1);
    """

    def __init__(self):
        self.head = Node()
        self.tail = None
        self.size = 0

    def append(self, item):
        newNode = Node(item)
        if self.head.item == None:
            self.head = newNode
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = newNode

    def pop(self):
        currentOne = self.head
        while currentOne.next != None:
            currentTwo = currentOne
            currentOne = currentOne.next
        currentTwo.next = None
        return currentOne.item

    def print(self):
        current = self.head
        while current.next != None:
            print(" {} ".format(current.item), end="|")
            current = current.next
        print(" {} ".format(current.item))
