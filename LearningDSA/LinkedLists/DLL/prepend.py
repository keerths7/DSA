class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
    
class DLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0 

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1 
        
    def __str__(self):
        temp_node = self.head
        result = ""
        while temp_node:
            result += str(temp_node.value)
            if temp_node.next:
                result += "<-->"
            temp_node = temp_node.next 
        return result 
    
    def prepend(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
    
dllinked_list = DLinkedList()
dllinked_list.append(10)
dllinked_list.append(20)
dllinked_list.append(30)
dllinked_list.append(40)
dllinked_list.append(50)
print(dllinked_list)
dllinked_list.prepend(5)
print(dllinked_list)