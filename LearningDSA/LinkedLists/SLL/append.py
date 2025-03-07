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
        if self.head is None:                    # without this if condition, errors occurs as self.tail has no next property as it is null.
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
    
linked_list = LinkedList()
linked_list.append(10)
linked_list.append(20)
linked_list.append(30)
print(linked_list.length)
print(linked_list.tail.value)
