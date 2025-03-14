class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous

class DLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def search(self, target):
        temp_node = self.head
        index = 0
        while not temp_node.next:
            temp_node = temp_node.next
            index += 1
        if temp_node.value == target:
            return True, index
        return False