class Node:
    def __init__(self, item=None, parent=None, leftNode=None, rightNode=None, bf=None):
        self.item = item
        self.leftNode = leftNode
        self.rightNode = rightNode
        self.parent = parent
        self.bf = bf
        self.height = 1

    def __str__(self):
        return str(self.item)


class AVL:
    def __init__(self):
        self.root = None

    def _get_height(self, tree):
        if not tree:
            return 0
        else:
            return tree.height

    def insert(self, item):
        self.root = self._insert(item, self.root)

    def _insert(self, item, tree):
        if not tree:
            return Node(item)
        if item < tree.item:
            left_sub_root = self._insert(item, tree.leftNode)
            tree.leftNode = left_sub_root
            left_sub_root.parent = tree
        elif item > tree.item:
            right_sub_root = self._insert(item, tree.rightNode)
            tree.rightNode = right_sub_root
            right_sub_root.parent = tree
        else:
            return tree
        tree.height = max(self._get_height(tree.leftNode), self._get_height(tree.rightNode)) + 1
        tree.bf = self._get_height(tree.leftNode) - self._get_height(tree.rightNode)
        return self.rebalance(tree)

    def rebalance(self, tree):
        if tree.bf == 2:
            if tree.leftNode.bf < 0:  # L-R
                tree.leftNode = self.rotate_left(tree.leftNode)
                return self.rotate_right(tree)
            else:  # L-L
                return self.rotate_right(tree)
        elif tree.bf == -2:
            if tree.rightNode.bf > 0:  # R-L
                tree.rightNode = self.rotate_right(tree.rightNode)
                return self.rotate_left(tree)
            else:  # R-R
                return self.rotate_left(tree)
        else:
            return tree

    def rotate_left(self, tree):
        pivot = tree.rightNode  # set up pointers
        tmp = pivot.leftNode
        # 1st Move: reassign pivot's right child to root and update parent pointers
        pivot.leftNode = tree
        pivot.parent = tree.parent  # pivot's parent now root's parent
        tree.parent = pivot  # root's parent now pivot
        # 2nd Move: use saved right child of pivot and assign it to root's left and update its parent
        tree.rightNode = tmp
        if tmp:  # tmp can be null
            tmp.parent = tree

        # update pivot's parent (manually check which one matches the root that was passed)
        if pivot.parent:
            if pivot.parent.rightNode == tree:  # if the parent's left subtree is the one to be updated
                pivot.parent.rightNode = pivot  # assign the pivot as the new child
            else:
                pivot.parent.leftNode = pivot  # vice-versa for right child

        # update heights and bf's using tracked heights
        tree.height = max(self._get_height(tree.leftNode), self._get_height(tree.rightNode)) + 1
        tree.bf = self._get_height(tree.leftNode) - self._get_height(tree.rightNode)
        pivot.height = max(self._get_height(pivot.leftNode), self._get_height(pivot.rightNode)) + 1
        pivot.bf = self._get_height(pivot.leftNode) - self._get_height(pivot.rightNode)
        return pivot  # return root of new tree

    def rotate_right(self, tree):
        pivot = tree.leftNode  # set up pointers
        tmp = pivot.rightNode
        # 1st Move: reassign pivot's right child to root and update parent pointers
        pivot.rightNode = tree
        pivot.parent = tree.parent  # pivot's parent now root's parent
        tree.parent = pivot  # root's parent now pivot
        # 2nd Move: use saved right child of pivot and assign it to root's left and update its parent
        tree.leftNode = tmp
        if tmp:  # tmp can be null
            tmp.parent = tree

        # update pivot's parent (manually check which one matches the root that was passed)
        if pivot.parent:
            if pivot.parent.leftNode == tree:  # if the parent's left subtree is the one to be updated
                pivot.parent.leftNode = pivot  # assign the pivot as the new child
            else:
                pivot.parent.rightNode = pivot  # vice-versa for right child

        # update heights and bf's using tracked heights
        tree.height = max(self._get_height(tree.leftNode), self._get_height(tree.rightNode)) + 1
        tree.bf = self._get_height(tree.leftNode) - self._get_height(tree.rightNode)
        pivot.height = max(self._get_height(pivot.leftNode), self._get_height(pivot.rightNode)) + 1
        pivot.bf = self._get_height(pivot.leftNode) - self._get_height(pivot.rightNode)
        return pivot  # return root of new tree

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
