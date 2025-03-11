class Node:
    def __init__(self):
        self.value = ValueError
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        self.length += 1

    def __str__(self):
        temp_node = self.head 
        while temp_node:
            result += str(temp_node.value)
            temp_node = temp_node.next
            if temp_node is not self.head:
                result += " --> "
            return result
    
    def pop_first(self):
        self.head = self.head.next 
        self.tail = self.head 
        