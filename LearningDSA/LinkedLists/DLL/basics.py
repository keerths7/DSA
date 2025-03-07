class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

# class DLinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.length = 0

class DLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1


# dlinked_list = DLinkedList()
dlinked_list = DLinkedList(10)
print(dlinked_list.head.value)

