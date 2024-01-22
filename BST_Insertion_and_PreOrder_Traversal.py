class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        elif root.val > key:
            root.left = insert(root.left, key)
    return root

def preorder(root):
    if root:
        print(root.val, end=' ')
        preorder(root.left)
        preorder(root.right)

root = None
while True:
    command = input().strip()
    if command == '#':
        break
    _, k = command.split()
    k = int(k)
    if root is None:
        root = insert(root, k)
    else:
        insert(root, k)

preorder(root)
