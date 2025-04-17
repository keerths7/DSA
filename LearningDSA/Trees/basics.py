class Tree:
    def __init__(self, value = None):
        self.value = value
        self.children =  []
    
    def append(self, value):
        child = Tree(value)
        self.children.append(child)
        return child

    def __str__(self):
        result = self.value + "\n"
        for i in self.children:
            result +=  " -" + i.value + "\n"
            if len(i.children) > 0:
                for i in i.children:
                    result += "  -" + i.value + "\n"
        return result.rstrip()

tree = Tree("Root")
child1 = tree.append("Child 1")
child2 = tree.append("Child 2")
grandchild1 = child1.append("Grandchild 1")
print(tree)