class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def append(self,value):
        new_node = Node(value)
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
    
    def pop(self):
        temp_node = self.head
        if self.length == 0:
            return None
        elif self.length == 1:
            popped_node = self.head
            self.head = None
            self.tail = None
        else:
            while temp_node.next is not self.tail:
                temp_node = temp_node.next
            popped_node = self.tail
            temp_node.next = None
            self.tail = temp_node
        self.length -= 1
        return popped_node
        
    def __str__(self):
        result = ""
        temp_node = self.head 
        while temp_node:
            result += str(temp_node.value)
            if temp_node.next:
                result += " --> "
            temp_node = temp_node.next
        return result

linked_list = LinkedList()
linked_list.append(10)
linked_list.append(20)
linked_list.append(30)
linked_list.append(40)
print(linked_list)
popped_node = linked_list.pop()
if popped_node:
    print(popped_node.value)
print(linked_list)