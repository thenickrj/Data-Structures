# Reverse Level Order Traversal

class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def reverseLevelOrder(temp):
    h = height(temp)
    for i in reversed(range(1, h + 1)):
        printGivenLevel(root, i)

    # Print nodes at a given level


# The function printGivenLevel will traverse the node
# level by level and will print the nodes in left to right fashion
def printGivenLevel(root, level):
    if root is None:
        return
    if level == 1:
        print
        root.data,

    elif level > 1:
        printGivenLevel(root.left, level - 1)
        printGivenLevel(root.right, level - 1)


def height(temp):
    if node is None:
        return 0
    else:
        # Compute the height of each subtree
        lheight = height(node.left)
        rheight = height(node.right)

        # Use the larger one
        if lheight > rheight:
            return lheight + 1
        else:
            return rheight + 1


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
reverseLevelOrder(root)
