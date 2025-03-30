class Stack:
    def __init__(self, size):
        self.size = size
        self.stack = [None for _ in range(size)]
        self.top = 0

    def push(self, value):
        if self.top == self.size: raise Exception("Stack is full")
        self.stack[self.top] = value
        self.top += 1

    def pop(self):
        if self.top == 0: raise Exception("Stack is empty")
        self.top -= 1
        self.stack.pop()

    def top(self):
        if self.top == 0: raise Exception("Stack is empty")
        return self.stack[self.top - 1]
    
    def full(self):
        return self.top == self.size
    
    def empty(self):
        return self.top == 0
    
    def size(self):
        return len(self.stack)
    
    def print(self):
        print(self.stack)