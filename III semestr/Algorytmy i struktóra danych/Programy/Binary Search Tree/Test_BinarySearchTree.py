import BinarySearchTree

binarySearchTree = BinarySearchTree.BinarySearchTree

tree = binarySearchTree()
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

tree.inOrder()

# --------------------------
# Test funkcji <code>search</code>
print("\n\nTest funkcji <code>search</code>\n")
print(tree.search("A"))  # True
print(tree.search("B"))  # True
print(tree.search("C"))  # True
print(tree.search("S"))  # False
print(tree.search("Y"))  # False
print(tree.search("Z"))  # True
print(tree.search("AW"))  # False
print(tree.search("W"))  # False

# --------------------------
# Test funkcji <code>minimum</code>
print("\n\nTest funkcji <code>minimum</code>\n")
print(tree.minimum())  # A

# --------------------------
# Test funkcji <code>successor</code>
print("\n\nTest funkcji <code>successor</code>\n")
print(tree.successor(tree.root.leftNode.rightNode.rightNode.rightNode))  # R następnik to T
print(tree.successor(tree.root.leftNode.leftNode))  # A następnik to B
print(tree.successor(tree.root.leftNode))  # B nastepnik to C
print(tree.successor(tree.root.rightNode.rightNode))  # Z nastepnik to None
print(tree.successor(tree.search("B")))

# --------------------------
# Test funkcji <code>delete</code>
print("\n\nTest funkcji <code>delete</code>\n")
tree.delete("A")
tree.inOrder()
tree.delete("J")
tree.inOrder()
tree.delete("Z")
tree.inOrder()
tree.delete("B")
tree.inOrder()
