import heapq

li = [5, 7, 9, 1, 3]

#Converts a regular list into a valid heap-in-place
heapq.heapify(li)

print(li) # [1, 3, 9, 7, 5]

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

#Merges two heaps
li1 = [1, 3, 5]
li2 = [2, 4, 6]
h3 = heapq.merge(li1, li2)
print(h3)