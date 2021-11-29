class Node:
    def __init__(self, item, parent=None, rightNode=None, leftNode=None):
        """
        Konstruktor klasy <code>Node</code> odpowiedzialny za przechowywanie informacji o lewym i prawym dziecku, danej
        w drzewie binarnym oraz wskaźnik na rodzica
        - self.item = dana
        - self.parent = wskaźnik na rodzica
        - self.rightNode = prawe dziecko korzenia
        - self.leftNode = lewe dziecko korzenia
        """
        self.item = item
        self.parent = parent
        self.rightNode = rightNode
        self.leftNode = leftNode

    def setItem(self, item):
        """
        Seter ustawiający item
        """
        self.item = item

    def setRightNode(self, rightNode):
        """
        Seter ustawiający prawe dziecko
        """
        self.rightNode = rightNode

    def setLeftNode(self, leftNode):
        """
        Seter ustawiający lewe dziecko
        """
        self.leftNode = leftNode

    def __str__(self):
        return str(self.item)


class BinaryTree:
    def __init__(self):
        self.root = None
        self.size = 0

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
                tree.leftNode = Node(item, tree)
        else:
            # Przechodzimy do prawej części korzenia
            if tree.rightNode is not None:
                # Jeśli prawa część korzenia nie jest pusta przechodzimy rekurencyjnie
                self._insert(item, tree.rightNode)
            else:
                # Wpisujemy item do prawej części korzenia
                tree.rightNode = Node(item, tree)

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
