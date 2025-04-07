import sys
sys.path.append('c:/Users/NickC/OneDrive/Área de Trabalho/Python Projects/Python 100 Projects - Udemy/Data Structures (UFSC)')
try:
    from DataStructures.non_linear.binary_search_tree import BinarySearchTree
except ModuleNotFoundError:
    raise ModuleNotFoundError("Ensure the 'DataStructures' module exists in the specified path and is correctly structured.")

# Depth First Search/Traversal 
# O(n)
# Good at finding a path in a graph, but not necessarily the shortest one.
# It is more memory efficient than BFS.

# Start at the root node and explore as far as possible along each branch before backtracking.
# This can be implemented using recursion or a stack.

    
#Example usage
b = BinarySearchTree()
b.root = b.insert(b.root, 10)
b.insert(b.root, 5)
b.insert(b.root, 15)
b.insert(b.root, 3)
#How is that tree structured?
#       10
#      /  \
#     5    15
#    /
#   3

# Below is a recursive implementation of DFS for a binary tree.

def dfs(root):
    if root is None:
        return
    
    print(root.value, end=" ")
    
    # Traverse the left subtree
    dfs(root.left)
    
    # Traverse the right subtree
    dfs(root.right)


# We can actually return a list of nodes in three orders:
# Pre-order: Visit the root, then left subtree, then right subtree.
def DFS_preorder(root):
    if root is None:
        return
    
    print(root.value, end=" ")
    
    # Traverse the left subtree
    DFS_preorder(root.left)
    
    # Traverse the right subtree
    DFS_preorder(root.right)


# In-order: Visit the left subtree, then root, then right subtree.
def DFS_inorder(root):
    if root is None:
        return
    
    # Traverse the left subtree
    DFS_inorder(root.left)
    
    print(root.value, end=" ")
    
    # Traverse the right subtree
    DFS_inorder(root.right)


# Post-order: Visit the left subtree, then right subtree, then root.
def DFS_postorder(root):
    if root is None:
        return
    
    # Traverse the left subtree
    DFS_postorder(root.left)
    
    # Traverse the right subtree
    DFS_postorder(root.right)
    
    print(root.value, end=" ")

dfs(b.root) # 10 5 3 15
print()
DFS_inorder(b.root) # 3 5 10 15
print()
DFS_preorder(b.root) # 10 5 3 15
DFS_postorder(b.root) # 3 5 15 10
print()