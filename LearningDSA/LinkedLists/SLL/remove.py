class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0 
    
    def append(self, value):
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
        new_node.next = self.head
        self.head = new_node
        self.length += 1
    
    def __str__(self):
        result = ""
        temp_head = self.head
        while temp_head:
            result += str(temp_head.value)
            if temp_head.next:
                result += " --> "
            temp_head = temp_head.next
        return result
    
    def get(self, index):
        current_node = self.head
        if index >= self.length or index < -1:
            return None
        elif index == -1:
            return self.tail
        else:
            for _ in range(index):
                current_node = current_node.next
        return current_node
    
    def pop_first(self):
        popped_node = self.head
        if self.length == 0:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
            return popped_node
        else:
            self.head = self.head.next
            popped_node.next = None
            self.length -= 1
            return popped_node

    def pop(self):
        temp_node = self.head
        if self.length == 0:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
            return temp_node
        else:
            while temp_node.next is not self.tail:
                temp_node = temp_node.next
            popped_node = temp_node.next
            temp_node.next = None
            self.tail = temp_node
            self.length -= 1
        return popped_node
        
    def remove(self, index):
        temp_node = self.head 
        if self.length == 0:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
            self.length = 0
        elif index == 0:
            popped_node = temp_node
            self.head = temp_node.next
            temp_node.next = None
            self.length -= 1
        else:
            for _ in range(index-1):
                temp_node = temp_node.next 
            popped_node = temp_node.next 
            temp_node.next = popped_node.next
            popped_node.next = None
            self.length -= 1
        return popped_node
    
    def remove_simplified(self, index):
        if index >= self.length or index < -1 :
            return None
        elif index == 0:
            popped_node = self.pop_first()
        elif index == -1 or index == self.length - 1:
            popped_node = self.pop()
        else:
            temp_node = self.get(index-1)
            popped_node = temp_node.next 
            temp_node.next = popped_node.next
            popped_node.next = None
            self.length -= 1
        return popped_node


linked_list = LinkedList()
linked_list.append(10)
linked_list.append(20)
linked_list.append(30)
linked_list.append(40)
linked_list.append(50)
removed_node = linked_list.remove(3)
if removed_node:
    print(removed_node.value)
print(linked_list)
