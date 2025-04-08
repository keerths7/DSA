class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue: 
    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0
    
    def enqueue(self, value):
        new_node = Node(value)
        if not self.front:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.length += 1

    def dequeue(self):
        if not self.front:
            return None
        popped_node = self.front
        if self.length == 1:
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next
            popped_node.next = None
        self.length -= 1 
        return popped_node.value
    
    def is_empty(self):
        return self.length == 0

    def peek(self):
        return self.front.value if self.front else None
    
    def end(self):
        return self.rear.value if self.rear else None
    
    def __str__(self):
        temp_node = self.front
        result = ""
        while temp_node:
            result += str(temp_node.value) + "\n"
            temp_node = temp_node.next
        return result.rstrip()

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
print(queue.end())
print(queue.dequeue())
print(queue)
print(queue.dequeue())
print(queue)
print(queue.dequeue())
print(queue)
print(queue.dequeue())
print(queue)