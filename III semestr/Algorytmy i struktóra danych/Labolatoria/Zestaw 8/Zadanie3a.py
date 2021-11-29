class Node:
    def __init__(self, item=None, rightNode=None, leftNode=None):
        self.item = item
        self.rightNode = rightNode
        self.leftNode = leftNode


class BinaryTree:
    def __init__(self):
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
            if tree.rightNode is not None:
                self._insert(item, tree.rightNode)
            else:
                tree.rightNode = Node(item)
        else:
            if tree.leftNode is not None:
                self._insert(item, tree.leftNode)
            else:
                tree.leftNode = Node(item)

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
        self._inOrder(self.root)
        print("")

    def _inOrder(self, tree):
        if tree is not None:
            self._inOrder(tree.leftNode)
            print(tree.item, end="|")
            self._inOrder(tree.rightNode)

    def postOrder(self):
        self._postOrder(self.root)
        print("")

    def _postOrder(self, tree):
        if tree is not None:
            self._postOrder(tree.leftNode)
            self._postOrder(tree.rightNode)
            print(tree.item, end="|")


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

print(tree.root.item)
tree.preOrder()
tree.inOrder()
tree.postOrder()
