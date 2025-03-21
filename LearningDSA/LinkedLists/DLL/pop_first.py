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

    def pop_first(self):
        if self.length == 0:
            return None
        popped_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            popped_node.next = None
        self.length -= 1
        return popped_node
    
    def __str__(self):
        result = ""
        temp_node = self.head
        while temp_node:
            result += str(temp_node.value)
            if temp_node.next:
                result += "<-->"
            temp_node = temp_node.next
        return result
    
dlinked_list = DLinkedList()
dlinked_list.append(10)
dlinked_list.append(20)
dlinked_list.append(30)
dlinked_list.append(40)
dlinked_list.append(50)
dlinked_list.append(60)
print(dlinked_list)
popped_node = dlinked_list.pop_first()
if popped_node:
    print(popped_node.value)
print(dlinked_list)