class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.length = 0 
    
    def is_empty(self):
        return self.length == 0
    
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.length += 1 

    def pop(self):
        if self.is_empty():
            return None
        popped_node = self.top
        self.top = self.top.next
        popped_node.next = None
        self.length -= 1 
        return popped_node.value
    
    def peek(self):
        if self.is_empty():
            return None
        return self.top.value
    
    def __str__(self):
        result = ""
        temp_node = self.top
        while temp_node:
            result += str(temp_node.value) + "\n"
            temp_node = temp_node.next
        return result.rstrip()

stack = Stack()
print(stack.is_empty())
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)
print(stack)
print(stack.is_empty())
print(stack.pop())
print(stack)
print(stack.peek())

    