import FIFO

Fifo = FIFO


class Node:
    """
    Klasa <code>Node</code> ma reprezentować pojemnik do przechowywania danych w abstralcyjnej strukturze danych
    (ADT-Abstract Data Type), która jest wykorzystywana przez klasę <code>BinaryTree</code> jako drzewo binarne.
    @author Jakub Kozubek
    @version 1.0
    @see <a href="https://sites.google.com/site/topinfo12/home/drzewo-licznikowe-i-przedzialowe">Więcej o liście dowiązanej</a>
    """

    def __init__(self, item=None, right=None, left=None, parent=None):
        """
        Konstruktor klasy <code>Node</code> ma 3 parametry startowe:
        <code>item</code>  (dana) reprezentuje pojemnik z konkretną daną do przechowania
        <code>rightNode</code> (prawy korzeń) reprezentuje wskaźnik na prawy pojemnik do przechowywania danych
        <code>leftNode</code> (lewy korzeń) reprezentuje wskaźnik na lewy pojemnik do przechowywania danych
        """
        self.item = item
        self.rightNode = right
        self.leftNode = left
        self.parent = parent

    def __str__(self):
        """
        Funkcja wbudowana w pythona zwracająca element w postaci stringa
        """
        return str(self.item)


class BinaryTree:
    """
    Klasa <code>BinaryTree</code> ma reprezentować abstralcyjnej strukture danych (ADT-Abstract Data Type). Drzewo
    binarne to jeden z rodzajów drzewa (struktury danych), w którym liczba synów każdego wierzchołka wynosi nie więcej
    niż dwa. Wyróżnia się wtedy lewego syna i prawego syna danego wierzchołka. Drzewo binarne, w którym liczba synów
    każdego wierzchołka wynosi albo zero albo dwa, nazywane jest drzewem regularnym.
    @author Jakub Kozubek
    @version 1.0
    @see <a href="https://pl.wikipedia.org/wiki/Drzewo_binarne">Więcej o liście dowiązanej</a>
    """

    def __init__(self):
        """
        Konstruktor klasy <code>BinaryTree</code> ma 1 parametry:
        <code>root</code> (korzeń) reprezentuje wskaźnik na korzeń drzewa czyli pierwszy element klasy <code>Node</code>
        """
        self.root = None

    def insert(self, item):
        """
        Funkcja klasy <code>BinaryTree</code> odpowiedzialna za dodanie nowego elementu do drzewa.
        Procedura zewnętrzna
        """
        if self.root is None:
            self.root = Node(item)
        else:
            self._insert(item, self.root)

    def _insert(self, item, tree):
        """
        Funkcja klasy <code>BinaryTree</code> odpowiedzialna za dodanie nowego elementu do drzewa.
        Procedura wewnętrzna
        """
        if tree.item > item:
            # Przechodzimy do lewej części korzenia
            if tree.leftNode is not None:
                # Jeśli lewa część korzenia nie jest pusta przechodzimy rekurencyjnie
                self._insert(item, tree.leftNode)
            else:
                # Wpisujemy item do lewej części korzenia
                tree.leftNode = Node(item)
                tree.leftNode.parent = tree
        else:
            # Przechodzimy do prawej części korzenia
            if tree.rightNode is not None:
                # Jeśli prawa część korzenia nie jest pusta przechodzimy rekurencyjnie
                self._insert(item, tree.rightNode)
            else:
                # Wpisujemy item do prawej części korzenia
                tree.rightNode = Node(item)
                tree.rightNode.parent = tree

    def breadthFirst(self):
        """
        Funkcja klasy <code>BinaryTree</code> odpowiedzialna za wypisywanie elementów drzewa według przeszukiwania wszerz  tzn
        Wiersz po wierszu
        Procedura zewnętrzna
        """
        self._breadthFirst(self.root)
        print("")

    def _breadthFirst(self, tree):
        """
        Funkcja klasy <code>BinaryTree</code> odpowiedzialna za wypisywanie elementów drzewa według przeszukiwania wszerz tzn
        Wiersz po wierszu
        Procedura wenwętrzna
        """
        fifo = Fifo.FIFO()
        fifo.addLast(tree)
        while not fifo.isEmpty():
            node = fifo.delFirst()
            print(node.item, end="|")
            if node.leftNode is not None:
                fifo.addLast(node.leftNode)
            if node.rightNode is not None:
                fifo.addLast(node.rightNode)


tree = BinaryTree()
tree.insert("T")  # 84
tree.insert("X")  # 88
tree.insert("B")  # 66
tree.insert("G")  # 71
tree.insert("Z")  # 90
tree.insert("C")  # 67
tree.insert("J")  # 74
tree.insert("R")  # 82
tree.insert("K")  # 75
tree.insert("A")  # 65
tree.insert("M")  # 77

tree.breadthFirst()


