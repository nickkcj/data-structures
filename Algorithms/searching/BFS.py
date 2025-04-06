from DataStructures.non_linear.binary_search_tree import BinarySearchTree

#Breadth First Search/Traversal
# O(n)
# Good at finding the shortest path in an unweighted graph, closer nodes.
# It is not as memory efficient as DFS.

#Start at the root node (selecting some arbitrary node as the root in the case of a graph)
#Explore all the neighboring nodes at the present depth prior to moving on to nodes at the next depth level.
#Left to right traversal of the tree/graph.


    
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

#Using BSF to traverse the tree
def bfs(root):
    if root is None:
        return
    
    queue = [root]
    
    while queue:
        current = queue.pop(0)
        print(current.value, end=" ")
        
        if current.left:
            queue.append(current.left)
        
        if current.right:
            queue.append(current.right)


#Example usage
bfs(b.root)  # Output: 10 5 15 3

