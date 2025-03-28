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

    def pop(self):
        if self.length == 0:
            return None
        temp_node = self.head
        popped_node = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            while temp_node.next is not self.tail:
                temp_node = temp_node.next 
            temp_node.next = self.head
            self.tail = temp_node
        self.length -= 1
        return popped_node

    def pop_first(self):
        if self.length == 0:
            return None
        popped_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head
            popped_node.next = None
        self.length -= 1
        return popped_node
    
    def remove_simplified(self, index):
        if index >= self.length or index < 0:
            return None
        elif index == 0:
            return self.pop_first()
        elif index == self.length - 1:
            return self.pop()
        else:
            temp_node = self.head
            for _ in range(index-1):
                temp_node = temp_node.next
            popped_node = temp_node.next
            temp_node.next = popped_node.next 
            popped_node.next = None
        self.length -= 1
        return popped_node

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
                self.tail.next = self.head
                popped_node.next = None
        elif index == self.length - 1:
            while temp_node.next is not self.tail:
                temp_node = temp_node.next
            popped_node = self.tail
            temp_node.next = self.head
            self.tail = temp_node 
        else:
            for _ in range(index-1):
                temp_node = temp_node.next
            popped_node = temp_node.next
            temp_node.next = popped_node.next 
            popped_node.next = None
        self.length -= 1
        return popped_node

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
cslinked_list.append(60)
print(cslinked_list)
# popped_node = cslinked_list.remove(2)
# if popped_node:
#     print(popped_node.value)
# print(cslinked_list)
# popped_node = cslinked_list.remove(4)
# if popped_node:
#     print(popped_node.value)
# print(cslinked_list)
# popped_node = cslinked_list.remove(0)
# if popped_node:
#     print(popped_node.value)
popped_node = cslinked_list.remove_simplified(2)
if popped_node:
    print(popped_node.value)
print(cslinked_list)
popped_node = cslinked_list.remove_simplified(4)
if popped_node:
    print(popped_node.value)
print(cslinked_list)
popped_node = cslinked_list.remove_simplified(0)
if popped_node:
    print(popped_node.value)
print(cslinked_list)