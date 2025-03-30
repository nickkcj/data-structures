class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, root, key):
        if root is None:
            return Node(key)
        
        if root.value == key:
            return root
        
        if root.value < key:
            root.right = self.insert(root.right, key)
        else:
            root.left = self.insert(root.left, key)

        return root

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.value, end=" ")
            self.inorder(root.right)

    def search(self, root, v):
        if root is None or root.value == v:
            return root
        
        if root.value < v:
            return self.search(root.right, v)
        
        return self.search(root.left, v)

    def get_successor(self, current):
        current = current.right
        while current is not None and current.left is not None:
            current = current.left
        return current

    def delete_node(self, root, x):
        if root is None:
            return root
        
        if root.value > x:
            root.left = self.delete_node(root.left, x)

        elif root.value < x:
            root.right = self.delete_node(root.right, x)

        else:
            # If root matches with the given key
            # Cases when root has 0 children or only right child
            if root.left is None:
                return root.right
            
            if root.right is None:
                return root.left
            
            successor = self.get_successor(root)
            root.value = successor.value
            root.right = self.delete_node(root.right, successor.value)

        return root


