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
        result = ""
        temp_head = self.head
        # while temp_head is not None:
        while temp_head:               # this is more pythonic
            result += str(temp_head.value)
            if temp_head.next:
                result += " --> "
            temp_head = temp_head.next
        return result

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