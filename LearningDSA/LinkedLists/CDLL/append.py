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

    def __str__(self):
        temp_node = self.head
        result = ""
        while temp_node:
            result += str(temp_node.value)
            temp_node = temp_node.next
            if temp_node is self.head:
                break
            result += "<-->"
        return result
    
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
                self.tail.next = self.head
                self.head.prev = new_node
        self.length += 1 

cdlinked_list = CDLinkedList()
cdlinked_list.append(10)
cdlinked_list.append(20)
cdlinked_list.append(30)
cdlinked_list.append(40)
cdlinked_list.append(50)
print(cdlinked_list)
print(cdlinked_list.head.prev.value)
print(cdlinked_list.tail.next.value)
