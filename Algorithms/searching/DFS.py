from DataStructures.non_linear.binary_search_tree import BinarySearchTree

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
    
    # Visit the root node
    print(root.value, end=" ")
    
    # Traverse the left subtree
    dfs(root.left)
    
    # Traverse the right subtree
    dfs(root.right)
