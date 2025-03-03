class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

# CSLL without any elements
# class CSLinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.length = 0
    
# CSLL with single element
class CSLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        new_node.next = new_node
        self.length = 1

# cslinked_list = CSLinkedList()
# print(cslinked_list.head)
cslinked_list = CSLinkedList(10)
print(cslinked_list.head.value)
print(cslinked_list.head.next.value)