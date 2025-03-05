class Node():
    def __init__(self,value):
        self.value = value
        self.next = None

class CSLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def append(self,value):
        ...
    def __str__(self):
        ...
    def prepend(self,value):
        ...

cslinked_list = CSLinkedList()
cslinked_list.append(10)
cslinked_list.append(20)
cslinked_list.append(30)
cslinked_list.append(40)
cslinked_list.prepend(5)
print(cslinked_list)