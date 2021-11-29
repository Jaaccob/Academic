import
class Heap:
    def __init__(self):
        """
        # Konstruktor
        -do reprezentacji kopca używamy pythonowych list
        -w konstruktorze wstawiamy 0 jako pierwszy element listy
        -element ten nie będzie później używany
        """
        self.heaplist = [None]
        self.heapsize = 0

    def insert(self, item):
        """
        Wstawienie elementu do kopca zupełnego polega na umieszczeniu elementu w pierwszym wolnym miejscu ostatniego
        poziomu i przywrócenia zachodzenia warunku kopca jeżeli wstawiony element jest większy niż element znajdujący
        się w poprzedniku.
        """
        self.heaplist.append(item)
        self.heapsize += 1
        self.fix_up()  # procedura "do góry", zajmuje się przywróceniem w stercie porządku po dadaniu elementu na koniec"

    def fix_up(self):
        k = self.heapsize
        while k > 1 and self.heaplist[k // 2] < self.heaplist[k]:
            self.heaplist[k // 2], self.heaplist[k] = self.heaplist[k], self.heaplist[k // 2]
            k //= 2

    def printList(self):
        return self.heaplist[1:]

    def buildHeap(self, new_list):
        for i in new_list:
            self.heaplist.append(i)
            self.heapsize += 1
        self._buildHeap()

    def _buildHeap(self):
        for i in range(self.heapsize // 2, 0, -1):
            self.fix_down(i, self.heapsize)

    def fix_down(self, i, size):
        left = 2 * i
        right = 2 * i + 1
        largest = i
        if left <= size and self.heaplist[largest] < self.heaplist[left]:
            largest = left
        if right <= size and self.heaplist[largest] < self.heaplist[right]:
            largest = right
        if largest != i:
            self.heaplist[largest], self.heaplist[i] = self.heaplist[i], self.heaplist[largest]
            self.fix_down(largest, size)

    def extractMax(self):
        maximum = self.heaplist[1]
        self.heaplist[1] = self.heaplist[-1]
        self.heapsize -= 1
        self.heaplist.pop()
        self.fix_down(1, self.heapsize)
        return maximum

    def heapSort(self, new_list):
        """
        Po utworzeniu kopca następuje właściwe sortowanie. Polega ono na usunięciu wierzchołka kopca, zawierającego
        element maksymalny (minimalny), a następnie wstawieniu w jego miejsce elementu z końca kopca i odtworzenie
        porządku kopcowego. W zwolnione w ten sposób miejsce, zaraz za końcem zmniejszonego kopca wstawia się usunięty
        element maksymalny. Operacje te powtarza się aż do wyczerpania elementów w kopcu. ## część posortowana i niepos.
        """
        self.buildHeap(new_list)
        size = self.heapsize
        while size > 1:
            self.heaplist[1], self.heaplist[size] = self.heaplist[size], self.heaplist[1]
            size -= 1
            self.fix_down(1, size)
        return self.heaplist[1:]


c = Heap()

l = [6, 5, 4, 3, 2, 1]
c.buildHeap(l)
print("Heap sort on list:", l, "==> ", c.heapSort(l))
