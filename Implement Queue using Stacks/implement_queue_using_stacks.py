class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class Stack:
    def __init__(self):
        self.top = None
    
    def push(self, x):
        new_node = Node(x)
        new_node.next = self.top
        self.top = new_node
    
    def pop(self):
        if self.top is None:
            return None
        value = self.top.value
        self.top = self.top.next
        return value
    
    def peek(self):
        return self.top.value if self.top is not None else None
    
    def empty(self):
        return self.top is None

class MyQueue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()
    
    def push(self, x):
        self.stack1.push(x)

    def pop(self):
        if self.stack2.empty():
            while not self.stack1.empty():
                self.stack2.push(self.stack1.pop())
        return self.stack2.pop()
    
    def peek(self):
        if self.stack2.empty():
            while not self.stack1.empty():
                self.stack2.push(self.stack1.pop())
        return self.stack2.peek()
    
    def empty(self):
        return self.stack1.empty() and self.stack2.empty()
# myQueue = MyQueue()
# myQueue.push(1)
# myQueue.push(2)
# myQueue.peek()
# myQueue.pop()
# myQueue.empty()