"""
tree.py (for class27)
"""

class Tree:
    """
    A Tree is a data structure where nodes have
    zero or more children, and one parent (except
    the root which has no parent).

    All the children and parents are Tree objects or None.
    """
    def __init__(self, value):
        self._parent = None
        self._children = []
        self._value = value

    def add_child(self, child):
        assert isinstance(child, Tree) 
        self._children.append(child)
        child._parent = self

    def get_value(self):
        return self._value

    def get_parent(self):
        return self._parent

    def get_children(self):
        return self._children

    def height(self):
        return 1 + max([subtree.height()
                        for subtree in self._children if subtree],
                       default = 0)
            
    def has_children(self):
        if self._children:
            for child in self._children:
                if child:
                    return True
        return False

    def traverse(self):
        """
        Returns a list of all Tree objects in this tree.
        """
        result = [self]
        for subtree in self._children:
            if subtree:
                result += subtree.traverse()
            else:
                result += [None]
        return result

    def leaves(self):
        return [node for node in self.traverse() if not node.has_children()]
    
    def __str__(self):
        return str(self._value) + "<" + \
                     ", ".join([str(child) for child in self._children]) \
                     + ">"
        

def test_tree():
    t = Tree("root")
    print(str(t))
    t.add_child(Tree("a"))
    t.add_child(Tree("b"))
    t.add_child(Tree("c"))
    print(str(t))
    nodes = t.traverse()
    print("Nodes: " + ', '.join([str(node.get_value()) for node in nodes]))
    anode = nodes[1]
    assert anode.get_value() == "a"
    anode.add_child(Tree("aa"))
    anode.add_child(Tree("ab"))
    print("Tree: " + str(t))
    leaves = t.leaves()
    assert len(leaves) == 4    
    print("Leaves: " + ', '.join([str(node.get_value()) for node in leaves]))    

    
if __name__ == "__main__":
    test_tree()
    

