class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
    
    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
    
    def __str__(self):
        result = ""
        temp_node = self.head
        while temp_node:
            result += str(temp_node.value)
            if temp_node.next:
                result += " --> "
            temp_node = temp_node.next
        return result

    def get(self, index):
        if index >= self.length or index < 0:
            return None
        current = self.head
        for _ in range(index):
            current = current.next
        return current.value

linked_list = LinkedList()
linked_list.append(10)
linked_list.append(20)
linked_list.append(30)
linked_list.append(40)
print(linked_list)
print(linked_list.get(0))
print(linked_list.get(-1))
print(linked_list.get(7))