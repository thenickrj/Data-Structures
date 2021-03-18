class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def sumBinary(temp):
    if temp == None:
        return 0
    return (temp.data + sumBinary(temp.left) + sumBinary(temp.right))


def inorder(temp):
    if not temp:
        return
    inorder(temp.left)
    print(temp.data)
    inorder(temp.right)


root = Node(15)
root.left = Node(10)
root.right = Node(20)
root.left.left = Node(8)
root.left.right = Node(12)
root.right.left = Node(16)
root.right.right = Node(25)
# inorder(root)
print(sumBinary(root))