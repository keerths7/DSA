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
    
    def pop(self):
        if self.length == 0:
            return False
        popped_node = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = self.head
            self.head.prev = self.tail
            popped_node.next = None
            popped_node.prev = None
        self.length -= 1
        return popped_node

    def pop_first(self):
        if self.length == 0:
            return False
        popped_node = self.head
        if self.length == 1: 
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = self.tail
            self.tail.next = self.head
            popped_node.next = None
            popped_node.prev = None
        self.length -= 1
        return popped_node

    def remove(self, index):
        if index >= self.length or index < 0:
            return False 
        if index == 0:
            popped_node = self.head 
            if self.length == 1:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next 
                self.head.prev = self.tail
                self.tail.next = self.head
                popped_node.next = None
                popped_node.prev = None
        elif index == self.length - 1:
            popped_node = self.tail 
            self.tail = self.tail.prev 
            self.tail.next = self.head
            self.head.prev = self.tail
            popped_node.next = None
            popped_node.prev = None
        else:
            temp_node = self.head
            for _ in range(index-1):
                temp_node = temp_node.next
            popped_node = temp_node.next
            temp_node.next = popped_node.next
            popped_node.next.prev = temp_node
            popped_node.prev = None
            popped_node.next = None
        self.length -= 1
        return popped_node

    def remove_simplified(self, index):
        if index >= self.length or index < 0:
            return False 
        temp_node = self.head
        if index == 0:
            return self.pop_first()
        elif index == self.length - 1:
            return self.pop()
        else:
            for _ in range(index-1):
                temp_node = temp_node.next 
            popped_node = temp_node.next
            temp_node.next = popped_node.next
            popped_node.next.prev = temp_node
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
cdlinked_list.prepend(5)
print(cdlinked_list)