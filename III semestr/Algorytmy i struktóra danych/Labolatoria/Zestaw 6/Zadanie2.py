class Node():
    def __init__(self, item=None):
        self.item = item  # 2 atrybuty,dane,połączenie(droga do następnego pudełka)
        self.next = None  # połączenie; jaką daną mamy mieć, jaka jest droga do następnego pudełka


class LinkedList():  # Połączenie ze sobą elementów
    def __init__(self):
        self.head = Node()  # Wskaznik na pierwszy element -> tutaj wskaźnik na obiekt klasy Node()
        self.tail = None  # Wskaznik na ostatni element

    def append(self, item):
        newNode = Node(item)
        if self.head.item is None:
            self.head = newNode
            self.tail = newNode
        else:
            current = self.tail
            current.next = newNode
            self.tail = current.next

    # Złożoność dodawania elementu na koniec listy wynosi  = O(1)

    def pop(self):
        currentOne = self.head
        while currentOne.next is not None:
            currentTwo = currentOne
            currentOne = currentOne.next
        currentTwo.next = None
        return currentOne.item

    # Złożoność usuwania elementu z konca listy wynosi  = O(n)

    def getTail(self):
        return self.tail

    def print(self):
        current = self.head
        while current.next is not None:
            print(" {} ".format(current.item), end="|")
            current = current.next
        print(" {} ".format(current.item))


list = LinkedList()
list.append(3)
list.append(2)
list.append(2)
list.append(5)
list.append(76)
list.append(1)
list.append(62)
list.append(11)
list.print()
print(list.pop())
list.print()
print(list.pop())
print(list.pop())
print(list.pop())
list.print()
