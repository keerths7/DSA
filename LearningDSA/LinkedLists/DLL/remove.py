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

    def remove(self, index):
        if index >= self.length or index < 0:
            return None
        temp_node = self.head
        if index == 0:
            popped_node = self.head
            if self.length == 1:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                temp_node.next = None
                self.head.prev = None       
        elif index == self.length - 1:
            popped_node = self.tail
            while temp_node.next is not self.tail:
                temp_node = temp_node.next
            temp_node.next = None
            self.tail.prev = None
            self.tail = temp_node    
        else:
            for _ in range(index-1):
                temp_node = temp_node.next
            popped_node = temp_node.next
            temp_node.next = popped_node.next
            popped_node.next.prev = temp_node
            popped_node.next = None
            popped_node.prev = None
        self.length -= 1 

    def __str__(self):
        result = ""
        temp_node = self.head
        while temp_node:
            result += str(temp_node.value)
            if temp_node.next:
                result += "<-->"
            temp_node = temp_node.next
        return result

dlinked_list = DLinkedList()
print(dlinked_list)
dlinked_list.append(10)
dlinked_list.append(20)
dlinked_list.append(30)
dlinked_list.append(40)
dlinked_list.append(50)
print(dlinked_list)
dlinked_list.remove(3)
print(dlinked_list)
dlinked_list.remove(0)
print(dlinked_list)
dlinked_list.remove(2)
print(dlinked_list)
