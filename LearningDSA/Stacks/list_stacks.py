class Stack:
    def __init__(self):
        self.list = []
        self.length = 0
    
    def is_empty(self):
        return self.length == 0 
    
    def push(self, value):
        self.list.append(value)
        self.length += 1 
    
    def pop(self):
        if self.is_empty():
            return None
        popped = self.list.pop()
        self.length -= 1
        return popped
    
    def peek(self):
        if self.is_empty():
            return None 
        return self.list[-1]
    
    def __str__(self):
        # reversed_list = reversed(self.list)
        # reversed_str_list = map(str, reversed_list)
        # return "\n".join(reversed_str_list)
        return "\n".join(map(str, self.list[::-1]))
    
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