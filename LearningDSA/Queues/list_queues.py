class Queue:
    def __init__(self):
        self.list = []
        self.length = 0 

    def is_empty(self):
        return self.length == 0 

    def enqueue(self, value):
        self.list.append(value)
        self.length += 1 
    
    def dequeue(self):
        if self.is_empty():
            return None 
        popped = self.list.pop(0)
        self.length -= 1
        return popped

    def peek(self):
        if self.is_empty():
            return None
        return self.list[0]
    
    def __str__(self):
        return "\n".join(map(str, self.list))

queue = Queue()
print(queue.is_empty())
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.enqueue(50)
print(queue)
print(queue.is_empty())
print(queue.dequeue())
print(queue)
print(queue.peek())