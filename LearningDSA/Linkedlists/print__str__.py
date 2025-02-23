class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0 
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        
        self.length += 1 

    def __str__(self):
       

linked_list = LinkedList()
print(linked_list)
linked_list.append(10)
print(linked_list)
linked_list.append(20)
print(linked_list)
linked_list.append(30)
print(linked_list)
linked_list.append(40)
print(linked_list)