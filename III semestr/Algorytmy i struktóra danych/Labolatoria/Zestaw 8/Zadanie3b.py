import Stack

Stos = Stack.Stack


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
            if tree.leftNode is not None:
                self._insert(item, tree.leftNode)
            else:
                tree.leftNode = Node(item)
        else:
            if tree.rightNode is not None:
                self._insert(item, tree.rightNode)
            else:
                tree.rightNode = Node(item)

    def preOrder(self):
        """
        Funkcja klasy <code>BinaryTree</code> odpowiedzialna za wypisywanie elementów drzewa według porządku preOrder tzn
        Środek - Lewy - Prawy
        Procedura zewnętrzna
        """
        self._preOrder(self.root)
        print("")

    def _preOrder(self, tree):
        stack = Stos()
        stack.push(tree)
        while not stack.isEmpty():
            tree = stack.pop()
            print(tree.item, end="|")
            if tree.rightNode is not None:
                stack.push(tree.rightNode)
            if tree.leftNode is not None:
                stack.push(tree.leftNode)

    def inOrder(self):
        self._inOrder(self.root)
        print("")

    def _inOrder(self, tree):
        stack = Stos()
        while not stack.isEmpty() or tree is not None:
            if tree is not None:
                stack.push(tree)
                tree = tree.leftNode
            else:
                tree = stack.pop()
                print(tree.item, end="|")
                tree = tree.rightNode

    def postOrder(self):
        self._postOrder(self.root)
        print("")


    #Nie działa !
    def _postOrder(self, tree):
        stack = Stos()
        stack.push(tree)
        current = Node()
        while not stack.isEmpty():
            tree = stack.pop()
            print(tree.item)
            if current is None or current.leftNode == tree or current.rightNode == tree:
                if tree.leftNode is not None:
                    stack.push(tree.leftNode)
                elif tree.rightNode is not None:
                    stack.push(tree.rightNode)
            elif tree.leftNode == current:
                if tree.rightNode is not None:
                    stack.push(tree.rightNode)
            else:
                print(tree.item, end="|")
            current = tree


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

# tree.preOrder()  # T|B|A|G|C|J|R|K|M|X|Z|
# tree.inOrder()  # A|B|C|G|J|K|M|R|T|X|Z|
tree.postOrder()  # A|C|M|K|R|J|G|B|Z|X|T|
