class Stack:
    def __init__(self):
        self.list = []
        self.length = 0

    def is_empty(self):
        if self.length == 0:
            return True
        return False

    def push(self,x):
        self.list.append(x)
        self.length += 1 

    def peek(self):
        return self.list[-1]
    
    def pop(self):
        popped = self.list.pop()
        self.length -= 1 
        return popped
    
    def __str__(self):
        reverse = reversed(self.list)
        str_list = [str(x) for x in reverse]
        return "\n".join(str_list)
    
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
print(stack)
print(stack.pop())
print(stack)
print(stack.peek())