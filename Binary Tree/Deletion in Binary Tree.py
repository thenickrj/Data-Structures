# Deletion in Binary Tree

class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


#Printing the values of the nodes in one of the methods of Depth First Search( Inorder)
def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)


#In this function we find the node that is be deleted
# which is passed as a parameter(d_node) and
# we check whether it is the rightmost node in the tree i.e, it shouldn't have any children nodes
def deleteDeepest(root, d_node):
    q = []
    q.append(root)
    while (len(q)):
        temp = q.pop(0)
        if temp is d_node:
            temp = None
            return
        if temp.right:
            if temp.right is d_node:
                temp.right = None
                return
            else:
                q.append(temp.right)
        if temp.left:
            if temp.left is d_node:
                temp.left = None
                return
            else:
                q.append(temp.left)

#In deletion function we find out the position of the element
# to be removed and that node value  will be replaced
# with the rightmost value of the tree,
# in this implementation it would be the last element stored in the queue
# and the original node value of that element will be set to None(deleted) in the deleteDeepest function
def deletion(root, key):
    if root == None:
        return None
    if root.left == None and root.right == None:
        if root.data == key:
            return None
        else:
            return root
    q = []
    key_node = None
    q.append(root)
    while (len(q)):
        temp = q.pop(0)
        if temp.data == key:
            key_node = temp
        if temp.left:
            q.append(temp.left)

        if temp.right:
            q.append(temp.right)
    if key_node:
        x = temp.data
        deleteDeepest(root, temp)
        key_node.data = x
        print(key_node.data)
    return root


if __name__ == '__main__':
    root = Node(10)
    root.left = Node(11)
    root.left.left = Node(7)
    root.left.right = Node(12)
    root.right = Node(9)
    root.right.left = Node(15)
    root.right.right = Node(8)
    print("The tree before the deletion:")
    inorder(root)
    key = 11
    root = deletion(root, key)
    print()
    print("The tree after the deletion;")
    inorder(root)
