from DataStructures.linked_queue import LinkedQueue
from DataStructures.matrix import SuperMatrix
from DataStructures.array import SuperArray
from DataStructures.queues import Queue
from DataStructures.stack import Stack
from DataStructures.binary_search_tree import BinarySearchTree
from DataStructures.linked_list import LinkedList
from DataStructures.graph import Graph

# # Example usage of LinkedQueue (Queue)
# queue = LinkedQueue()
# queue.enqueue(10)
# queue.enqueue(20)
# queue.enqueue(30)
# print("Dequeued from queue:", queue.dequeue())
# queue.enqueue(40)
# queue.print()

# # Example usage of Pilha (Stack)
# stack = Pilha()
# stack.push(5)
# stack.push(15)
# stack.push(25)
# print("Popped from stack:", stack.pop())
# stack.push(35)
# stack.print()

# # Example usage of BinarySearchTree
# bst = BinarySearchTree()
# bst.insert(50)
# bst.insert(30)
# bst.insert(70)
# bst.insert(20)
# bst.insert(40)
# bst.insert(60)
# bst.insert(80)
# print("In-order traversal of BST:", bst.in_order_traversal())
# print("Search for 40 in BST:", bst.search(40))
# print("Search for 100 in BST:", bst.search(100))

# # Example usage of LinkedList
# linked_list = LinkedList()
# linked_list.append(1)
# linked_list.append(2)
# linked_list.append(3)
# linked_list.insert(0, 0)  # Insert at the beginning
# linked_list.insert(2, 1.5)  # Insert at index 2
# linked_list.remove(3)  # Remove element at index 3
# linked_list.print()


# l = LinkedQueue()
# l.enqueue(1)
# l.enqueue(20)
# l.enqueue(15)
# l.dequeue()
# l.enqueue(500)

# l.dequeue()
# l.print()

g = Graph()
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(3, 4)

print("Neighbors of 1:", g.get_neighbors(1))
print("Neighbors of 2:", g.get_neighbors(2))
print("Neighbors of 3:", g.get_neighbors(3))
print("Neighbors of 4:", g.get_neighbors(4))

g.remove_edge(1, 2)
print("Neighbors of 1 after removing edge (1,2):", g.get_neighbors(1))