class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def push(self, x):
        new_node = Node(x)
        if not self.head:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
    
    def pop(self):
        if not self.head:
            return None
        value = self.head.value
        self.head = self.head.next
        if not self.head:
            self.tail = None
        return value
    
    def top(self):
        return self.head.value if self.head else None
    
    def empty(self):
        return self.head is None

class MyStack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()
    
    def push(self, x):
        self.q1.push(x)
    
    def pop(self):
        while self.q1.top() is not None and self.q1.top() != self.q1.tail.value:
            self.q2.push(self.q1.pop())
        top = self.q1.pop()
        self.q1, self.q2 = self.q2, self.q1
        return top
    
    def top(self):
        while self.q1.top() is not None and self.q1.top() != self.q1.tail.value:
            self.q2.push(self.q1.pop())
        top = self.q1.top()
        self.q2.push(self.q1.pop())
        self.q1, self.q2 = self.q2, self.q1
        return top
    
    def empty(self):
        return self.q1.empty() and self.q2.empty()

# Example usage:
stack = MyStack()
stack.push(1)
stack.push(2)
print(stack.top())   # Output: 2
print(stack.pop())   # Output: 2
print(stack.empty()) # Output: False
