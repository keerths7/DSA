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
    
    def get(self, index):
        if index >= self.length or index < 0:
            return None 
        else:
            temp_node = self.head
            for _ in range(index):
                temp_node = temp_node.next
            return temp_node.value

cdlinkedlist = CDLinkedList()
cdlinkedlist.append(10)
cdlinkedlist.append(20)
cdlinkedlist.append(30)
cdlinkedlist.append(40)
cdlinkedlist.append(50)
print(cdlinkedlist)
print(cdlinkedlist.get(2))
print(cdlinkedlist.get(-2))
print(cdlinkedlist.get(20))
print(cdlinkedlist)