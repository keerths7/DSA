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

    def __str__(self):
        result = ""
        temp_node = self.head
        while temp_node:
            result += str(temp_node.value)
            if temp_node.next:
                result += " <--> "
            temp_node = temp_node.next
        return result

    def insert(self, index, value):
        if index > self.length or index < 0:
            return False
        new_node = Node(value)
        if index == 0:
            if self.length == 0:
                self.head = new_node
                self.tail = new_node
            else:
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node
        elif index == self.length:
            self.tail.next = new_node
            new_node.prev = self.tail 
            self.tail = new_node
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

dlinked_list = DLinkedList()
print(dlinked_list)
dlinked_list.append(10)
dlinked_list.append(20)
dlinked_list.append(30)
dlinked_list.append(40)
dlinked_list.append(50)
print(dlinked_list)
dlinked_list.insert(2, 25)
print(dlinked_list)
dlinked_list.insert(0, 5)
print(dlinked_list)
dlinked_list.insert(7, 55)
print(dlinked_list)