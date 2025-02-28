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
            self.head = None
            self.tail = None
        else:
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node
        self.length += 1
    
    def insert(self, index, value):
        new_node = Node(value)
        if index > self.length or index < 0:
            return False
        if self.length == 0:                    # temp_node points to self.head which is None, then when we set new_node.next to temp_node.next, None has no next attribue.
            self.head = new_node 
            self.tail = new_node
        elif index == 0 :                       # index is 0 means, the temp_node remains self.head, and new_node gets inserted at 1st index instead
            new_node.next = self.head
            self.head = new_node
        else:
            temp_node = self.head
            for _ in range(index-1):
                temp_node =  temp_node.next
            new_node.next =  temp_node.next
            temp_node.next = new_node
        self.length += 1
        return True

    def __str__(self):
        result = ""
        temp_head = self.head
        while temp_head:
            result += str(temp_head.value)
            if temp_head.next:
                result += " --> "
            temp_head = temp_head.next
        return result


linked_list = LinkedList()
linked_list.append(10)
linked_list.append(20)
linked_list.append(30)
linked_list.append(40)
linked_list.insert(3, 35)
linked_list.insert(10, 35)
linked_list.insert(0, 5)
linked_list.insert(6, 45)
print(linked_list)