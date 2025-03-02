class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0 
    
    def append(self, value):
        new_node =  Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
    
    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else: 
            new_node.next = self.head
            self.head = new_node
        self.length += 1 
    
    def pop_first(self):
        popped_node = self.head
        if self.length == 0:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
            return popped_node
        else:
            self.head = self.head.next
            popped_node.next = None
            self.length -= 1
            return popped_node
    
    def __str__(self):
        result = ""
        temp_head = self.head
        while temp_head:
            result += str(temp_head.value)
            if temp_head.next:
                result += " --> "
            temp_head = temp_head.next
        return result 
    
linked_list = LinkedList()
linked_list.append(10)
linked_list.append(20)
linked_list.append(30)
linked_list.append(40)
print(linked_list)
print(linked_list.pop_first())
print(linked_list)