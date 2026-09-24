class node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(root, key):
        if root is None:
            return node(key)
        else:
            if root.key < key:
                root.right = insert(root.right, key)
            else:
                root.left = insert(root.left, key)
        return root
def inorder(root):
        if root:
            inorder(root.left)
            print(root.key, end=" ")
            inorder(root.right)

def preorder(root):
        if root:
            print(root.key, end=" ")
            preorder(root.left)
            preorder(root.right)

def postorder(root):
        if root:
            postorder(root.left)
            postorder(root.right)
            print(root.key, end=" ")

root = None

values = [50, 30, 20, 40, 70, 60, 80]

for value in values:
    root = insert(root, value)

print("Inorder traversal of the binary search tree:")
inorder(root)

print("\nPreorder traversal of the binary search tree:")
preorder(root)

print("\nPostorder traversal of the binary search tree:")
postorder(root)