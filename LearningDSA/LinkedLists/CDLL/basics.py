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
        new_node.next = new_node        # self.tail.next = new_node                                    
        new_node.prev = new_node        # self.head.prev = new_node
        self.length = 1

cdlinkedlist = CDLinkedList(10)
print(cdlinkedlist.head.value)
print(cdlinkedlist.head.next.value)
print(cdlinkedlist.tail.next.value)