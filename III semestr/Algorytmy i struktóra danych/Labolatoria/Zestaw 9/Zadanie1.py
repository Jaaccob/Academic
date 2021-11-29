class HeapMaxPQ:
    """
    warunki Heap:
    - drzewo kompletne
    - uporzątkowane

    lewy potomek i-tego węzła jest schowany  pod indeksem 2*i
    prawy potomek i-tego węzła jest schowany pod indeksem 2*i+1
    """

    def __init__(self):
        self.heap = [None]
        self.heapsize = 1

    def isEmpty(self):
        return len(self.heap) == 1

    def fix_UP(self, k):
        while (k > 1) and (self.heap[k // 2] < self.heap[k]):
            self.heap[k // 2], self.heap[k] = self.heap[k], self.heap[k // 2]
            k = k // 2

    def insert(self, x):
        self.heap.append(x)
        self.heapsize += 1
        self.fix_UP(len(self.heap) - 1)

    def print(self):
        return self.heap[1:]

    def build_heap(self, new_list):
        for i in new_list:
            self.heap.append(i)
            self.heapsize += 1
        self._build_heap()

    def _build_heap(self):
        for i in range(len(self.heap) // 2, 0, -1):
            self.fix_DOWN(i)

    def sort(self, new_list):
        self.build_heap(new_list)
        size = len(self.heap)
        while size > 1:
            self.heap[1], self.heap[size] = self.heap[size], self.heap[1]
            size -= 1
            self.fix_DOWN(size)
        return self.heap[1:]

    def fix_DOWN(self, k):
        l = 2 * k
        r = 2 * k + 1
        largest = k
        n = len(self.heap) - 1  # indeks ostatniego elementu
        if l <= n and self.heap[l] > self.heap[largest]:
            largest = l
        if r <= n and self.heap[r] > self.heap[largest]:
            largest = r
        if largest != k:
            self.heap[k], self.heap[largest] = self.heap[largest], self.heap[k]
            self.fix_DOWN(largest)

    def extract_MAX(self):
        if self.isEmpty():
            return "Kolejka pusta"
        m = self.heap[1]
        n = len(self.heap) - 1
        self.heap[1] = self.heap[n]
        self.heap.pop()
        self.fix_DOWN(1)
        return m


mypq = HeapMaxPQ()
mypq.insert(30)
mypq.insert(100)
mypq.insert(25)
mypq.insert(40)


print("Poping out elements ...")
while not mypq.isEmpty():
    print(' ', mypq.extract_MAX())



table = [71, 66, 24, 32, 27, 23, 8, 5, 22, 25, 18]
mypq.build_heap(table)
