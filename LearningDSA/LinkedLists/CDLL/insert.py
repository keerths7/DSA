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
        temp_node = self.head 
        result = ""
        while temp_node:
            result += str(temp_node.value)
            temp_node = temp_node.next
            if temp_node is self.head:
                break
            result += " <--> "
        return result 

    def insert(self, index, value):
        if index > self.length or index < 0:
            return False
        new_node = Node(value)
        if index == 0:
            if self.length == 0:
                self.head = new_node
                self.tail = new_node
                new_node.next = new_node
                new_node.prev = new_node
            else:
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node
                new_node.prev = self.tail
                self.tail.next = new_node
        elif index == self.length:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            new_node.next = self.head
            self.head.prev = new_node
        else:
            temp_node = self.head 
            for _ in range(index-1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next.prev = new_node
            new_node.prev = temp_node
            temp_node.next = new_node
        self.length += 1
        return True
    
cdlinkedlist = CDLinkedList()
cdlinkedlist.append(10)
cdlinkedlist.append(20)
cdlinkedlist.append(30)
cdlinkedlist.append(40)
cdlinkedlist.append(50)
print(cdlinkedlist)
cdlinkedlist.insert(3, 25)
print(cdlinkedlist)
cdlinkedlist.insert(0, 5)
print(cdlinkedlist)
cdlinkedlist.insert(7, 55)
print(cdlinkedlist)