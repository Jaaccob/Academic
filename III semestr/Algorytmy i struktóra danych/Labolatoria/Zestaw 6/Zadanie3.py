class Node():
    def __init__(self, item=None):
        self.item = item  # 2 atrybuty,dane,połączenie(droga do następnego pudełka)
        self.next = None  # połączenie; jaką daną mamy mieć, jaka jest droga do następnego pudełka
        self.previous = None  # połączenie; jaka jest droga do poprzedniego pudełka


class LinkedList():  # Połączenie ze sobą elementów
    def __init__(self):
        self.head = Node()  # Wskaznik na pierwszy element -> tutaj wskaźnik na obiekt klasy Node()
        self.tail = None  # Wskaznik na ostatni element

    def append(self, item):
        newNode = Node(item)
        if self.head.item is None:
            self.head = newNode
            self.tail = newNode
            newNode.previous = newNode
        else:
            current = self.tail
            current.next = newNode
            newNode.previous = self.tail
            self.tail = current.next

    # Złożoność dodawania elementu na koniec listy wynosi  = O(1)

    def remove_end(self):
        try:
            if self.tail.next is None:
                raise ValueError("Lista jest pusta!!!")
            else:
                current = self.tail
                self.tail = current.previous
                self.tail.next = None
                return current.item
        except ValueError:
            return False

    # Złożoność usuwania elementu z konca listy wynosi  = O(1)

    def getTail(self):
        current = self.tail
        return current.item

    def getPrevious(self):
        current = self.tail
        currentOne = current.previous
        return currentOne.item

    def print(self):
        current = self.head
        while current.next is not None:
            print(" {} ".format(current.item), end="|")
            current = current.next
        print(" {} ".format(current.item))


list = LinkedList()
list.append(3)
list.print()
list.append(2)
list.print()
list.append(2)
list.append(5)
list.append(76)
list.print()
list.append(1)
list.append(62)
list.append(11)
print("Lista ostateczna")
list.print()
print(list.remove_end())
list.print()
print(list.remove_end())
print(list.remove_end())
print(list.remove_end())
list.print()
print(list.remove_end())
print(list.remove_end())
print(list.remove_end())
print(list.remove_end())
print(list.remove_end())
print(list.remove_end())


