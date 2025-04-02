class Stack:
    def __init__(self):
        self.list = []
        self.length = 0
    
    def is_empty(self):
        if self.length == 0:
            return True
        return False
    
    def push(self, value):
        self.list.append(value)
        self.length += 1
    
    def pop(self):
        popped = self.list.pop()
        self.length -= 1
        return popped
    
    def peek(self):
        return self.list[-1]
    
    def __str__(self):
        reversed_list = reversed(self.list)
        str_reversed_list =  [str(i) for i in reversed_list]
        return "\n".join(str_reversed_list)

stack = Stack()
print(stack.is_empty())
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
print(stack.is_empty())
print(stack.peek())
print(stack.pop())
print(stack)