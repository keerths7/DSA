# Until now we have seen the built in data structures in python. Let us make custom data structures using oops concepts.
# In linked lists, each node requires extra memory to store a pointer to the next node, which increases memory usage compared to arrays.  
# Linked lists allow dynamic resizing at runtime since their size is not fixed initially, unlike arrays that require predefined sizes or costly resizing operations.  
# In arrays, accessing the 5th element is efficient and done using indexing (arr[4]) in O(1) time.  
# However, in linked lists, elements are stored at arbitrary memory locations, requiring traversal from the head node, making element access O(n) in the worst case.  


# Creating just a node
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

node = Node(10)
print(f"node's value: {node.value}")

# Creating a linked list with no nodes
# Time Complexity- 
# Space Complexity- 
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

empty_linked_list = LinkedList()
print(empty_linked_list.length)

# Creating a linked list with 1 node:
# Time Complexity- 
# Space Complexity- 
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

linked_list = LinkedList(10)
print(linked_list.length)