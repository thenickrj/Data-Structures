# Insertion in Binary Tree

class Node:
    def __init__(self, key):
        self.data = key
        self.right = None
        self.left = None


def inorder(temp):
    if not temp:
        return

    inorder(temp.left)
    print(temp.data, end=" ")
    inorder(temp.right)


def insert(temp, key):
    if not temp:
        root = Node(key)
        return
    q = []
    q.append(temp)

    # Do level order traversal untill we find
    # an empty place.
    while (len(q)):
        temp = q[0]
        q.pop(0)

        if not temp.left:
            temp.left = Node(key)
            break
        else:
            q.append(temp.left)

        if not temp.right:
            temp.right = Node(key)
            break
        else:
            q.append(temp.right)


if __name__ == "__main__":
    root = Node(10)
    root.left = Node(11)
    root.right = Node(9)
    root.left.left = Node(7)
    root.right.left = Node(15)
    root.right.right = Node(8)

    print("Inorder traversal before Insertion:", end=" ")
    inorder(root)

    key = 12
    insert(root, key)

    print()
    print("Inorder traversal after Insertion", end=" ")
    inorder(root)