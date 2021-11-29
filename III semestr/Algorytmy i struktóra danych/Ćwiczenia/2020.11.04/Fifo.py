class NiedomiarException(Exception):
    pass


class NadmiarException(Exception):
    pass


class Kolejka_Fifo():
    """
    Klasa <code>Kolejka_Fifo</code> reprezentuje kolejke First In First Out
    Implementacja tej kolejki posiada wcześniej zadeklarowaną wielkość listy cyklicznej
    Złożoność czasowa tego algorytmu wynosi :
    Przy dodawaniu nowego elementu = O(1);
    Przy ściąganiu elementu = O(1);
    """

    def __init__(self, number):
        self.table = ["" for i in range(number)]
        self.tail = 0
        self.head = 0
        self.size = 0
        self.tailBool = True
        self.headBool = False

    def enQueue(self, element):
        try:
            if self.tail == self.head and self.tailBool == self.headBool:
                raise NadmiarException
            self.table[self.tail] = element
            if self.tail == len(self.table) - 1:
                self.tail = 0
                self.size += 1
                if self.tailBool:
                    self.tailBool = False
                else:
                    self.tailBool = True
            else:
                self.tail += 1
        except NadmiarException:
            print("Kolejka jest zapełniona, nie mogę dodać kolejnego elementu")

    def deQueue(self):
        x = self.table[self.head]
        try:
            if self.tail == self.head and self.tailBool != self.headBool:
                raise NiedomiarException
            elif self.head == len(self.table) - 1:
                self.head = 0
                self.size -= 1
                if self.headBool:
                    self.headBool = False
                else:
                    self.headBool = True
            else:
                self.head += 1
            return x
        except NiedomiarException:
            print("Kolejka nie posiada więcej elementów do zwrócenia ")
            return False