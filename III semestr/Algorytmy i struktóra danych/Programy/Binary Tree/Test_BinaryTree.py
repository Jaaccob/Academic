import BinaryTree

binaryTree = BinaryTree.BinaryTree
node = BinaryTree.Node

# Przykładowe drzewo
tree = binaryTree()
tree.insert("T")
tree.insert("X")
tree.insert("B")
tree.insert("G")
tree.insert("Z")
tree.insert("C")
tree.insert("J")
tree.insert("R")
tree.insert("K")
tree.insert("A")
tree.insert("M")

"""print(tree.root.item)  # T
print(tree.root.leftNode.item)  # B
print(tree.root.leftNode.leftNode.item)  # A
print(tree.root.leftNode.rightNode.item)  # G
print(tree.root.leftNode.rightNode.leftNode.item)  # C
print(tree.root.leftNode.rightNode.rightNode.item)  # J
print(tree.root.leftNode.rightNode.rightNode.rightNode.item)  # R
print(tree.root.leftNode.rightNode.rightNode.rightNode.leftNode.item)  # K
print(tree.root.leftNode.rightNode.rightNode.rightNode.leftNode.rightNode.item)  # M
print(tree.root.rightNode.item)  # X
print(tree.root.rightNode.rightNode.item)  # Z

print("Porzadek Preorder")
tree.preOrder()  # T|B|A|G|C|J|R|K|M|X|Z
# Czas odwiedzenia drzewa w porządku Preorder wynosi O(n)

print("Porzadek Inorder")
tree.inOrder()  # A|B|C|G|J|K|M|R|T|X|Z
# Czas odwiedzenia drzewa w porządku Inorder wynosi O(n)

print("Porzadek Postorder")
tree.postOrder()  # A|C|M|K|R|J|G|B|Z|X|T
# Czas odwiedzenia drzewa w porządku Preorder wynosi O(n)

print("Przeszukiwanie wszerz")
tree.breadthFirst()"""

print("Wysokość drzewa")
print(tree.h)