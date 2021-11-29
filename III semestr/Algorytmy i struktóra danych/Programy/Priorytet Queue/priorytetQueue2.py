class listqueue():
    def __init__(self):
        self.queue = []
        self.size = 0

    def insert(self, element):

        if self.size == 0:
            self.queue.append(element)
            self.size = self.size + 1
        elif self.size == 1:
            if self.queue[0][1] > element[1]:
                self.queue = self.queue + [element]
            else:
                self.queue = [element] + self.queue
        else:
            for i in range(len(self.queue)):
                if self.queue[i] < element[1]:
                    self.queue = self.queue[:i] + [element] + self.queue[i:]
                    break

    def extract_max(self):
        zmienna = self.queue[0]
        self.queue = self.queue[1:]
        return zmienna

    def is_Empty(self):
        if self.size == 0:
            return True
        else:
            return False


lista = listqueue()
lista.insert([1, 1])
lista.insert([1, 2])
lista.insert([1, 3])
lista.insert([2, 1])
print(lista.queue)
print(lista.extract_max())
print(lista.queue)
