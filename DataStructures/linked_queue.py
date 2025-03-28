class Element:
    def __init__(self, value):
        self.value = value
        self.next = None

    def setNext(self, next):
        self.next = next

    def getNext(self):
        return self.next
    
class LinkedQueue:
    def __init__(self):
        self.head = None
        self.tall = None
        self.size = 0

    def enqueue(self, value):
        if self.head is None:
            self.head = Element(value)
            self.tall = self.head

        else:
            new_element = Element(value)
            self.tall.setNext(new_element)
            self.tall = new_element
        self.size += 1

    def dequeue(self):
        if self.head is None:
            raise Exception("Queue is empty")
        
        dequeued_value = self.head.value
        self.head = self.head.getNext()
        self.size -= 1

        return dequeued_value
    
    def isEmpty(self):
        return self.head is None
    
    def getSize(self):
        return self.size
    
    def print(self):
        current = self.head
        while current is not None:
            print(current.value, end=" ")
            current = current.getNext()
        print()

