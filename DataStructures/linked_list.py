class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None  # Add tail reference for O(1) append
        self.size = 0     # Track size for O(1) length lookup

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def prepend(self, data):
        new_head = Node(data)
        new_head.next = self.head
        self.head = new_head
        if self.tail is None:  # If list was empty
            self.tail = self.head
        self.size += 1

    def delete(self, data):
        if self.head is None:
            return
            
        if self.head.data == data:
            self.head = self.head.next
            self.size -= 1
            if self.head is None:  # List is now empty
                self.tail = None
            return
            
        current = self.head
        while current.next:
            if current.next.data == data:
                if current.next == self.tail:  # If removing the last node
                    self.tail = current
                current.next = current.next.next
                self.size -= 1
                return
            current = current.next

    def get_size(self):
        return self.size
        
    def is_empty(self):
        return self.head is None

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next

    def __repr__(self):
        if self.head is None:
            return "Empty"
        
        result = ""
        current = self.head
        while current:
            result += str(current.data)
            if current.next:
                result += "->"
            current = current.next
        return result