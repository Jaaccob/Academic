class listqueue():
    def __init__(self):
        self.queue = []
        self.size = 0

    def insert(self, element):
        self.queue.append(element)

    def extract_max(self):
        zmienna = self.queue[0]

        if len(self.queue) == 1:
            y = self.queue[0]
            self.queue = []
            self.size = 0
            return y
        else:
            for i in range(len(self.queue)):
                if self.queue[i][1] > zmienna[1]:
                    zmienna = self.queue[i]
                    xyz = i
            self.queue = self.queue[:xyz] + self.queue[xyz + 1:]
            self.size = self.size - 1
        return zmienna

    def is_Empty(self):
        if self.size == 0:
            return True
        else:
            return False


lista = listqueue()
lista.insert([1, 1])
lista.insert([1, 3])
lista.insert([1, 2])

print(lista.extract_max())
