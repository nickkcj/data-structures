class Pilha:
    def __init__(self, size):
        self.size = size
        self.stack = [0 for i in range(size)]
        self.top = 0

    def push(self, value):
        if self.top == self.size: raise Exception("Stack is full")
        self.stack[self.top] = value
        self.top += 1

    def pop(self):
        if self.top == 0: raise Exception("Stack is empty")
        self.top -= 1
        self.stack.pop()