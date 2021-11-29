class Node:
    def __init__(self, item=None):
        self.item = item
        self.children = []

    def addChild(self, item):
        self.children.append(Node(item))


class BinaryTree:
    def __init__(self):
        self.root = Node()


tree = BinaryTree()
tree.root.item = "T"
tree.root.addChild("X")

print(tree.root.item)
print(tree.root.children[0].item)
