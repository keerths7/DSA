class Node:
    def __init__(self, value):       
        self.next = None
        self.prev = None
        self.value = value

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
        result = ""
        temp_node = self.head
        while temp_node:
            result += str(temp_node.value)
            if temp_node.next:
                result += " <--> "
            temp_node = temp_node.next
        return result
    
    def pop(self):
        if self.length == 0:
            return None
        popped_node = self.tail 
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp_node = self.head
            while temp_node.next is not self.tail:
                temp_node = temp_node.next
            temp_node.next = None
            self.tail.prev = None
            self.tail = temp_node
        self.length -= 1 
        return popped_node 

dlinked_list = DLinkedList()
dlinked_list.append(10)
dlinked_list.append(20)
dlinked_list.append(30)
dlinked_list.append(40)
dlinked_list.append(50)
dlinked_list.append(60)
print(dlinked_list)
popped_node = dlinked_list.pop()
if popped_node:
    print(popped_node.value)
print(dlinked_list)

