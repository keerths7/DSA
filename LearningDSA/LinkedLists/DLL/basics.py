class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0


dlinked_list = DLinkedList(10, 20)
print(dlinked_list.head.value)
print(dlinked_list.head.next.value)
print(dlinked_list.head.prev)
print(dlinked_list.tail.value)
print(dlinked_list.tail.prev.value)
print(dlinked_list.tail.next)