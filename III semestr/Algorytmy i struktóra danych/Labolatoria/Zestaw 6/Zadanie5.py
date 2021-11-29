import Zadanie3

Linked_List = Zadanie3.LinkedList


class OrderedList(Linked_List):
    def __init__(self):
        self.linked_list = Linked_List()

    def isEmpty(self):
        """
        Funkcja <code>isEmpty</code> sprawdza czy stos zawiera dane
        :return funkcja zwraca prawdę jeśli linked_list.tail wskazuje na None, w przeciwnym razię jeśli parametr
        linked_list.tail wskazuje na kolejny element funkcja zwraca False
        """
        currentTail = self.linked_list.tail
        currentHead = self.linked_list.head
        return True if currentHead != currentTail else False

    def push(self, item):
        """
        Funkcja <code>push</code> dodaje nowy element do stosu
        """
        self.linked_list.append(item)

    def pop(self):
        """
        Funkcja <code>pop</code> usuwa ostatni element z stosu
        """
        current = self.linked_list.remove_end()
        return current

    def size(self):
        """
        Funkcja <code>size</code> sprawdza ile elementów zawiera stos
        """
        current = self.linked_list.head
        i = 1
        while current.next is not None:
            i += 1
            current = current.next
        return i

    def peek(self):
        """Funkcja <code>peek</code> pobiera ostatni element z stosu nie usuwając go"""
        item = self.linked_list.pop()
        self.linked_list.append(item)
        return item

    def wypisz(self):
        print("Tail = {}".format(self.linked_list.getTail()))
        print("Previous = {}".format(self.linked_list.getPrevious()))
        print("Tablica : |", end="")
        self.linked_list.print()


order_List = OrderedList()
print(order_List.isEmpty())
order_List.push(7)
print(order_List.size())
print(order_List.pop())
print(order_List.isEmpty())
order_List.push(7)
order_List.push(3)
order_List.push(1)
order_List.push(6)
order_List.push(2)
order_List.push(6)
order_List.push(71)
print(order_List.isEmpty())
order_List.wypisz()
print(order_List.size())
print(order_List.peek())
order_List.wypisz()
