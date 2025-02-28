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
        popped_element = self.head
        if self.length == 0 :
            return None
        elif self.length == 1:                # since self.tail would still point to the popped element
            popped_element = self.head
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            popped_element.next = None
        self.length -= 1
        return popped_element
    
    def __str__(self):
        result = ""
        temp_head = self.head
        while temp_head:
            result += str(temp_head.value)
            if temp_head.next:
                result += " --> "
            temp_head = temp_head.next
        return result 
    
linked_list =  LinkedList()
linked_list.prepend(10)
print(linked_list.head.value)
        