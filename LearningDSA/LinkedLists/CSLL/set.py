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
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            self.length = 0
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        self.length += 1 
    
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
    
    def get(self, index):
        if index >= self.length or index < 0:
            return None
        else:
            current_node = self.head
            for _ in range(index):
                current_node = current_node.next
            return current_node
    
    def set(self, index, value):
        current_node = self.get(index)
        if current_node:
            current_node.value = value
            return True
        return False
    
cslinked_list = CSLinkedList()
cslinked_list.append(10)
cslinked_list.append(20)
cslinked_list.append(30)
cslinked_list.append(40)
cslinked_list.append(50)
print(cslinked_list)
cslinked_list.set(3, 35)
print(cslinked_list)
print(cslinked_list.set(0, 5))
print(cslinked_list.set(-2, 35))
print(cslinked_list.set(6, 35))
print(cslinked_list)