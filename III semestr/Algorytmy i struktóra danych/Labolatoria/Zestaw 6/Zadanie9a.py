class NiedomiarException(Exception):
    pass


class NadmiarException(Exception):
    pass


class CircularTable():
    def __init__(self, number):
        self.table = ["" for i in range(number)]
        self.tail = 0
        self.head = 0
        self.size = 0
        self.tailBool = True
        self.headBool = False

    def addFirst(self, item):
        try:
            if self.tail == self.head and self.tailBool == self.headBool:
                raise NadmiarException
            else:
                zmienna1 = self.head
                zmienna2 = self.headBool
                if zmienna1 == 0:
                    zmienna1 = len(self.table) - 1
                    if zmienna2 == True: zmienna2 = False
                    else: zmienna2 = True
                self.table[zmienna1] = item



        except NadmiarException:
            print("Kolejka jest zapełniona, nie mogę dodać kolejnego elementu")
