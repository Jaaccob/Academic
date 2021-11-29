class Node():
    def __init__(self, item=None):
        self.item = item  # 2 atrybuty,dane,połączenie(droga do następnego pudełka)
        self.next = None  # połączenie; jaką daną mamy mieć, jaka jest droga do następnego pudełka


class LinkedList():  # Połączenie ze sobą elementów
    def __init__(self):
        self.head = Node()

    def append(self, item):
        newNode = Node(item)
        if self.head.item is None:
            self.head = newNode
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = newNode

    # Złożoność dodawania elementu na koniec listy wynosi  = O(n)

    def pop(self):
        currentOne = self.head
        while currentOne.next is not None:
            currentTwo = currentOne
            currentOne = currentOne.next
        currentTwo.next = None
        return currentOne.item

    # Złożoność usuwania elementu z konca listy wynosi  = O(n)

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
list.print()
print(list.pop())
list.print()
