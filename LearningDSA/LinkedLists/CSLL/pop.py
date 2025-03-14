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
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:       
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        self.length += 1 
    
    def __str__(self):
        result = ""
        temp_head = self.head
        while temp_head:
            result += str(temp_head.value)
            temp_head = temp_head.next 
            if temp_head is self.head:
                break
            result += " --> "
        return result

    def pop(self):
        temp_node = self.head
        if self.length == 0:
            return None
        elif self.length == 1:
            popped_node = self.head
            self.head = None
            self.tail = None
        else:
            while temp_node.next is not self.tail:
                temp_node = temp_node.next 
            popped_node = self.tail
            temp_node.next = self.head
            popped_node.next = None

        self.length -= 1
        return popped_node
        

cslinked_list = CSLinkedList()
cslinked_list.append(10)
cslinked_list.append(20)
cslinked_list.append(30)
cslinked_list.append(40)
cslinked_list.append(50)
print(cslinked_list)
cslinked_list.pop()
print(cslinked_list)
