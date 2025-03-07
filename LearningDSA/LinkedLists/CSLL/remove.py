class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
class CSLinkedList:
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
        else:
            self.tail.next = new_node
            new_node.next = self.head
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
                popped_node.next = None
                self.tail.next = self.head
        elif index == self.length - 1:
            while temp_node.next is not self.tail:
                temp_node = temp_node.next
            popped_node = temp_node.next
            temp_node.next = self.head
            self.tail = temp_node 
        else:
            for _ in range(index-1):
                temp_node = temp_node.next
            popped_node = temp_node.next
            temp_node.next = popped_node.next 
            popped_node.next = None
        self.length -= 1
        return popped_node.value

    def __str__(self):
        result = ""
        temp_node = self.head
        while temp_node:
            result += str(temp_node.value)
            temp_node = temp_node.next
            if temp_node is self.head:
                break
            result += " --> "
        return result 

cslinked_list = CSLinkedList()
cslinked_list.append(10)
cslinked_list.append(20)
cslinked_list.append(30)
cslinked_list.append(40)
cslinked_list.append(50)
print(cslinked_list)