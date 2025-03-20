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
        temp_node = self.head
        while temp_node:
            result += str(temp_node.value)
            if temp_node.next:
                result += " --> "
            temp_node = temp_node.next
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
        else:
            while temp_node.next is not self.tail:
                temp_node = temp_node.next
            popped_node = temp_node.next
            temp_node.next = None
            self.tail = temp_node
        self.length -= 1
        return popped_node
        
    def remove(self, index):
        if index >= self.length or index < 0 :
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
        elif index == self.length - 1:
            popped_node = self.tail
            while temp_node.next is not self.tail:
                temp_node = temp_node.next
            self.tail = temp_node
            temp_node.next = None
        else:
            for _ in range(index-1):
                temp_node = temp_node.next 
            popped_node = temp_node.next
            temp_node.next = popped_node.next
            popped_node.next = None
        self.length -= 1
        return popped_node

    def remove_simplified(self, index):
        if index >= self.length or index < 0 :
            return None
        elif index == 0:
            popped_node = self.pop_first()
        elif index == self.length - 1:
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
linked_list.append(60)
print(linked_list)
# popped_node = linked_list.remove(2)
# if popped_node:
#     print(popped_node.value)
# print(linked_list)
# popped_node = linked_list.remove(4)
# if popped_node:
#     print(popped_node.value)
# print(linked_list)
# popped_node = linked_list.remove(0)
# if popped_node:
#     print(popped_node.value)

popped_node = linked_list.remove_simplified(2)
if popped_node:
    print(popped_node.value)
print(linked_list)
popped_node = linked_list.remove_simplified(4)
if popped_node:
    print(popped_node.value)
print(linked_list)
popped_node = linked_list.remove_simplified(0)
if popped_node:
    print(popped_node.value)
print(linked_list)