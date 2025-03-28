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
    
    def search(self, target):
        temp_node = self.head
        index = 0 
        while temp_node:
            if temp_node.value == target:
                return True, index 
            temp_node = temp_node.next
            if temp_node is self.head:
                break
            index += 1 
        return False

cd_linkedlist = CDLinkedList()
cd_linkedlist.append(10)
cd_linkedlist.append(20)
cd_linkedlist.append(30)
cd_linkedlist.append(40)
cd_linkedlist.append(50)
print(cd_linkedlist)
print(cd_linkedlist.search(34))
print(cd_linkedlist.search(30))
print(cd_linkedlist.search(10))
print(cd_linkedlist.search(50))