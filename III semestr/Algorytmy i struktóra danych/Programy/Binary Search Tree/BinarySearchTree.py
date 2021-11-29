import Programy.FIFO.FIFO

Fifo = Programy.FIFO.FIFO


class Node:
    """
    Klasa <code>Node</code> ma reprezentować pojemnik do przechowywania danych w abstralcyjnej strukturze danych
    (ADT-Abstract Data Type), która jest wykorzystywana przez klasę <code>BinaryTree</code> jako drzewo binarne.
    @author Jakub Kozubek
    @version 1.0
    @see <a href="https://sites.google.com/site/topinfo12/home/drzewo-licznikowe-i-przedzialowe">Więcej o liście dowiązanej</a>
    """

    def __init__(self, item=None, parent=None, right=None, left=None):
        """
        Konstruktor klasy <code>Node</code> ma 3 parametry startowe:
        <code>item</code>  (dana) reprezentuje pojemnik z konkretną daną do przechowania
        <code>rightNode</code> (prawy korzeń) reprezentuje wskaźnik na prawy pojemnik do przechowywania danych
        <code>leftNode</code> (lewy korzeń) reprezentuje wskaźnik na lewy pojemnik do przechowywania danych
        """
        self.item = item
        self.parent = parent
        self.rightNode = right
        self.leftNode = left

    def __str__(self):
        """
        Funkcja wbudowana w pythona zwracająca element w postaci stringa
        """
        return str(self.item)


class BinarySearchTree:
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

    """
    Funkcja klasy <code>BinaryTree</code> odpowiedzialna za dodanie nowego elementu do drzewa. Koszt takiego wyszukiwania 
    jest rzędu O(h), gdzie h oznacza wysokość drzewa.
    Procedura wewnętrzna
    """

    def _insert(self, item, tree):
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

    def delete(self, item):
        current = self.search(item)
        self._delete(current, item)

    def _delete(self, tree, item):
        if tree.leftNode is None and tree.rightNode is None:
            # Jeśli tree to liść
            current = tree.parent
            if current.leftNode is tree:
                current.leftNode = None
            else:
                current.rightNode = None
        elif tree.leftNode is None and tree.rightNode is not None:
            # Jeśli tree posiada prawe dziecko
            current = tree.parent
            if current.leftNode is tree:
                current.leftNode = tree.rightNode
            else:
                current.rightNode = tree.rightNode
            tree.rightNode = current
        elif tree.leftNode is not None and tree.rightNode is None:
            # Jeśli tree posiada lewe dziecko
            current = tree.parent
            if current.leftNode is tree:
                current.leftNode = tree.leftNode
            else:
                current.rightNode = tree.leftNode
            tree.leftNode = current
        elif tree.leftNode is not None and tree.rightNode is not None:
            # Jeśli tree posiada oboje dzieci
            current = self.successor(tree)
            if current.parent.rightNode == current:
                current.parent.rightNode = None
            else:
                current.parent.leftNode = None
            parent = tree.parent
            childOne = tree.leftNode
            childTwo = tree.rightNode
            current.leftNode = childOne
            current.rightNode = childTwo
            current.parent = parent
            if parent.leftNode is tree:
                parent.leftNode = current
            else:
                parent.rightNode = current

    """
    Funkcja wewnętrzna odpowiedzialna za wyszukiwanie konkretnego elementu w drzewie binarnym. Koszt takiego wyszkukiwania
    jest rzędu O(h), gdzie h oznacza wysokość drzewa. W najgorszym przypadku jest on liniowy ze względu na liczbę węzłów
    w drzewie
    """

    def search(self, item):

        if self.root is None:
            return False
        return self._search(item, self.root)

    """
    Funkcja wewnętrzna odpowiedzialna za wyszukiwanie konkretnego elementu w drzewie binarnym. Koszt takiego wyszkukiwania
    jest rzędu O(h), gdzie h oznacza wysokość drzewa. W najgorszym przypadku jest on liniowy ze względu na liczbę węzłów
    w drzewie
    """

    def _search(self, item, tree):
        if tree is None:
            return False
        elif tree.item == item:
            return tree  # return True
        elif tree.item > item:
            return self._search(item, tree.leftNode)
        elif tree.item < item:
            return self._search(item, tree.rightNode)

    def minimum(self):
        if self.root is None:
            return False
        else:
            return self._minimum(self.root)

    """
    Funkcja <code>_minimum</code> odpowiedzialna jest za znalezienie najmniejszego elementu w drzewie binarnym. Funkcja 
    jest funkcją wewnętrzną. Koszt wykonania funkcji jest rzęczy O(h), gdzie h oznacza wysokość drzewa. W najgorszym 
    przypadku jest on liniowy ze względu na liczbę węzłów w drzewie.
    """

    def _minimum(self, tree):
        if tree.leftNode is not None:
            return self._minimum(tree.leftNode)
        else:
            return tree

    """
    Funkcja <code>successor</code> odpowiada za znalezienie następnego elementu w wyszukiwaniu in-Order. Koszt wykonania
    funkcji jest rzęczy O(h), gdzie h oznacza wysokość drzewa. W najgorszym przypadku jest on liniowy ze względu na 
    liczbę węzłów w drzewie. 
    """

    def successor(self, tree):
        if tree is False:
            return False
        if tree.rightNode is not None:
            return self._minimum(tree.rightNode)
        tree_tmp = tree.parent
        while tree_tmp is not None:
            if tree is not tree_tmp.rightNode:
                break
            tree = tree_tmp
            tree_tmp = tree_tmp.parent
        if tree_tmp is None:
            return None
        return tree_tmp

    def preOrder(self):
        """
        Funkcja klasy <code>BinaryTree</code> odpowiedzialna za wypisywanie elementów drzewa według porządku preOrder tzn
        Środek - Lewy - Prawy
        Procedura zewnętrzna
        """
        self._preOrder(self.root)
        print("")

    def _preOrder(self, tree):
        if tree is not None:
            print(tree.item, end="|")
            self._preOrder(tree.leftNode)
            self._preOrder(tree.rightNode)

    def inOrder(self):
        """
        Funkcja klasy <code>BinaryTree</code> odpowiedzialna za wypisywanie elementów drzewa według porządku inorder tzn
        Lewy - Środek - Prawy
        Procedura zewnętrzna
        """
        self._inOrder(self.root)
        print("")

    def _inOrder(self, tree):
        """
        Funkcja klasy <code>BinaryTree</code> odpowiedzialna za wypisywanie elementów drzewa według porządku inorder tzn
        Lewy - Środek - Prawy
        Procedura wenwętrzna
        """
        if tree is not None:
            self._inOrder(tree.leftNode)
            print(tree.item, end="|")
            self._inOrder(tree.rightNode)

    def postOrder(self):
        """
        Funkcja klasy <code>BinaryTree</code> odpowiedzialna za wypisywanie elementów drzewa według porządku post order tzn
        Lewy - Prawy - Środek
        Procedura zewnętrzna
        """
        self._postOrder(self.root)
        print("")

    def _postOrder(self, tree):
        """
        Funkcja klasy <code>BinaryTree</code> odpowiedzialna za wypisywanie elementów drzewa według porządku post order tzn
        Lewy - Prawy - Środek
        Procedura wenwętrzna
        """
        if tree is not None:
            self._postOrder(tree.leftNode)
            self._postOrder(tree.rightNode)
            print(tree.item, end="|")

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

    def h(self):
        return self._h(self.root)

    def _h(self, tree=None):
        if tree.leftNode is None and tree.rightNode is None:
            return 0

        if tree.leftNode is None:
            return self._h(tree.rightNode) + 1
        if tree.rightNode is None:
            return self._h(tree.leftNode) + 1

        return max(self._h(tree.leftNode), self._h(tree.rightNode)) + 1
