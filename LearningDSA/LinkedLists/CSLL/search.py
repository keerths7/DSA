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
        temp_node = self.head
        result = ""
        while temp_node:
            result += str(temp_node.value)
            temp_node = temp_node.next
            if temp_node == self.head:
                break
            result += " --> "
        return result

    def search(self, value):
        current_node = self.head
        index = 0 
        while current_node:
            if current_node.value == value:
                return True, index
            current_node = current_node.next
            index += 1 
            if current_node is self.head:
                return False, -1
        
cslinked_list = CSLinkedList()
cslinked_list.append(10)
cslinked_list.append(20)
cslinked_list.append(30)
cslinked_list.append(40)
cslinked_list.append(50)
print(cslinked_list)
print(cslinked_list.search(80))