class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def appending_node(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1
    
linked_list = LinkedList()
linked_list.appending_node(10)
linked_list.appending_node(20)
linked_list.appending_node(30)
print(linked_list.length)
print(linked_list.tail.value)
