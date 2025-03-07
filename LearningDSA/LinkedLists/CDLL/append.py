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
            new_node.next = self.head
            self.tail = new_node
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

cdinked_list = CDLinkedList()
cdinked_list.append(10)
cdinked_list.append(20)
cdinked_list.append(30)
cdinked_list.append(40)
cdinked_list.append(50)
print(cdinked_list)
