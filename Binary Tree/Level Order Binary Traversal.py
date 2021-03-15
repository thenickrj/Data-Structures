# Level Order Binary Tree Traversal

# A node Structure
class Node:
    # A utilty function to create a new node
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


# the function printLevelOrder will divide
# the Binary Tree w.r.t level in this example it is (1,2,3) levels
def printLevelOrder(root):
    h = height(root)
    for i in range(1, h + 1):
        printGivenLevel(root, i)


# The function printGivenLevel will traverse the node
# level by level and will print the nodes in left to right fashion
def printGivenLevel(root, level):
    if root is None:
        return
    if level == 1:
        print(root.data, end=" ")
    elif level > 1:
        printGivenLevel(root.left, level - 1)
        printGivenLevel(root.right, level - 1)


# The height function will calculate the height of the tree recursively.
# In this case the height is 3
def height(node):
    if node is None:
        return 0
    else:
        lheight = height(node.left)
        rheight = height(node.right)

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

print("Level order traversal of binary tree")
printLevelOrder(root)

# Time Complexity: O(n^2) in worst case.
# Space Complexity: O(n) in worst case.
