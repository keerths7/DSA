class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class CDLinkedList:
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
            new_node.prev = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            new_node.next = self.head
            self.head.prev = new_node
        self.length += 1
    
    def __str__(self):
        result = ""
        temp_node = self.head
        while temp_node:
            result += str(temp_node.value)
            temp_node = temp_node.next
            if temp_node is self.head:
                break
            result += " <--> "
        return result

    def pop(self):
        if self.length == 0:
            return None
        popped_node = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev 
            self.tail.next = self.head
            self.head.prev = self.tail
            popped_node.prev = None
            popped_node.next = None
        self.length -= 1 
        return popped_node

cdlinked_list = CDLinkedList()
cdlinked_list.append(10)
cdlinked_list.append(20)
cdlinked_list.append(30)
cdlinked_list.append(40)
cdlinked_list.append(50)
print(cdlinked_list)
popped_node = cdlinked_list.pop()
if popped_node:
    print(popped_node.value)
print(cdlinked_list)