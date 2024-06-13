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


def sum_of_bst(root):
    if root is None:
        return 0
    return root.val + sum_of_bst(root.left) + sum_of_bst(root.right)

# Find the sum of all values in the BST
total_sum = sum_of_bst(root)
print("Sum of all values in the BST:", total_sum)