class Element:
    def __init__(self, value):
        self.value = value
        self.next = None

    def setNext(self, next):
        self.next = next

    def getNext(self):
        return self.next
    
class LinkedStack:
    def __init__(self):
        self.top = None

    def isEmpty(self):
        return self.top is None

    def push(self, value):
        new_element = Element(value)
        new_element.setNext(self.top)
        self.top = new_element

    def pop(self):
        if self.isEmpty():
            raise Exception("Stack is empty")
        
        popped_value = self.top.value
        self.top = self.top.getNext()
        return popped_value