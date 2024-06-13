class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

root = Node(5)
root = insert(root, 3)
root = insert(root, 2)
root = insert(root, 4)
root = insert(root, 7)
root = insert(root, 6)
root = insert(root, 8)

def find_minimum_value(node):
    current = node
    
    # Loop down to find the leftmost leaf
    while current.left is not None:
        current = current.left
    
    return current.val

# Finding the smallest value
min_value = find_minimum_value(root)
print("The smallest value in the BST is:", min_value)