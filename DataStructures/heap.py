import heapq

li = [5, 7, 9, 1, 3]

#Converts a regular list into a valid heap-in-place
heapq.heapify(li)
 # [1, 3, 9, 7, 5]

#Adds an element to the heap while maintaining the heap property
heapq.heappush(li, 4)

#Removes the smallest element from the heap
heapq.heappop(li)

#View the smallest element on the heap without removing it
heapq.peek(li)

#Finding the n largest elements in a heap
heapq.nlargest(n, li)

#Finding the n smallest elements in a heap
heapq.nsmallest(n, li)

#Pops the smallest and inserts a new element
heapq.heapreplace(li, 2)

li2 = [8, 6, 2, 4]
heapq.heapify(li2)

li3 = [10, 12, 14, 11]
heapq.heapify(li3)

#Merges multiple heaps into a single heap
heapq.merge(li, li2, li3)