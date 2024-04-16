class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def plus(self, x):
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
        return value
    
    def peek(self):
        return self.head.value if self.head else None
    
    def is_empty(self):
        return self.head is None

class MyStack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()
    
    def push(self, x):
        self.q1.plus(x)
        while not self.q2.is_empty():
            self.q1.plus(self.q2.pop())
        self.q1,self.q2=self.q2,self.q1
    
    def pop(self):
        return self.q2.pop()
    
    def top(self):
        return self.q2.peek()
    
    def empty(self):
        return self.q2.is_empty()

# Example usage:
stack = MyStack()
stack.push(1)
stack.push(2)
# stack.push(3)
# stack.push(4)
# stack.push(2)
print(stack.top())   # Output: 2
print(stack.pop())   # Output: 2
# print(stack.top())   # Output: 4
print(stack.pop())
print(stack.empty())#True
