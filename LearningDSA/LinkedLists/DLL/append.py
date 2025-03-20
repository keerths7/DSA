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
    
    def __str__(self):
        result = ""
        temp_node = self.head
        while temp_node:
            result += str(temp_node.value)
            if temp_node.next:
                result += " <--> "
            temp_node = temp_node.next
        return result

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

dlinked_list = DLinkedList()
print(dlinked_list)
dlinked_list.append(10)
dlinked_list.append(20)
dlinked_list.append(30)
dlinked_list.append(40)
dlinked_list.append(50)
print(dlinked_list)


