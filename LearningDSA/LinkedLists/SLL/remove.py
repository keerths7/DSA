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
        new_node.next = self.head
        self.head = new_node
        self.length += 1
    
    def __str__(self):
        result = ""
        temp_head = self.head
        while temp_head:
            result += str(temp_head.value)
            if temp_head.next:
                result += " --> "
            temp_head = temp_head.next
        return result
    
    def remove(self, index):
        temp_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        elif index == 0:
            self.head = self.head.next
            temp_node.next = None
        else:
            for _ in range(index-1):
                temp_node = temp_node.next
            temp_node.next = temp_node.next.next
            temp_node.next.next = None
        self.length -= 1

linked_list = LinkedList()
linked_list.append(10)
linked_list.append(20)
linked_list.append(30)
linked_list.append(40)
linked_list.append(50)
linked_list.remove(0)
print(linked_list)