class Node():
    def __init__(self, dana, left=None, right=None):
        self.dana = dana
        self._right = right
        self._left = left


class PriorityQueueN():
    def __init__(self):
        self.size = 0
        self._head = None
        self._end = None

    def insert(self, element):
        if self.size == 0:
            wezel = Node(element)
            self._head = wezel
            self._end = wezel
            self.size += 1
        elif self.size == 1:
            wezel = Node(element, self._end)
            self._end._right = wezel
            self._head = wezel
            self.size += 1
        else:
            wezel = Node(element, self._head)
            self._head._right = wezel
            self._head = wezel
            self.size += 1

    def extract_max(self):
        zmienna = self._end
        schowek = self._end

        if self.size == 0:
            raise ValueError("Pusta kolejka")

        while schowek._right != None:
            schowek = schowek._right
            if schowek.dana[1] > zmienna.dana[1]:
                zmienna = schowek

        if self.size == 1:
            self._head = None
            self._end = None
            self.size = 0
        elif self.size == 2:
            if zmienna == self._end:
                self._end = self._head
                self._head._right = None
                self._head._left = None
                self.size -= 1
            elif zmienna == self._head:
                self._head = self._end
                self._end._right = None
                self._end._left = None
                self.size -= 1

        if self.size > 2:
            if zmienna == self._end:
                self.end = self.end._right
                self.end._left = None
                self.size -= 1
            elif zmienna == self._head:
                self._head = self._head._left
                self._head._right = None
                self.size -= 1
            else:
                zmienna._left = zmienna._right
                zmienna._right = zmienna._left
                self.size -= 1
        return (zmienna.dana)


kolejka = PriorityQueueN()
kolejka.insert([1, 3])
kolejka.insert([1, 2])
kolejka.insert([1, 4])
# print(kolejka._head._left.dana)
# print(kolejka._end.dana)
# print(kolejka._end._right.dana)
# print(kolejka._end._right._right.dana)
print(kolejka.extract_max())
# print(kolejka._head.dana)
print(kolejka.extract_max())
# print(kolejka._head.dana)
# print(kolejka._end.dana)
print(kolejka.extract_max())
# print(kolejka.extract_max())
