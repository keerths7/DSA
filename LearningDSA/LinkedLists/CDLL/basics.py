class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

# class CDLinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.length = 0 

class CDLinkedList:
    def __init__(self, value):
        new_node = Node(value) 
        self.head = new_node
        self.tail = new_node
        new_node.next = new_node
        new_node.prev = new_node
        self.length = 1

cdinked_list = CDLinkedList(10)
print(cdinked_list.head.value)
print(cdinked_list.tail.value)
print(cdinked_list.head.next.value)
print(cdinked_list.head.prev.value)
