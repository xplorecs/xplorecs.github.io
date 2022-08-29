"""
orderedbinarytree.py
"""

from binarytree import BinaryTree

class OrderedBinaryTree(BinaryTree):
    """
    A tree where the ordered invariant is preserved:
        if left_node is left of current_node,
            fcompare(left_node.value, current_node.value)
        must be True
    """

    def __init__(self, value, fcompare = lambda a, b: a < b):
        super().__init__(value)
        self._fcompare = fcompare
        
    def add_child(self, child):
        raise RuntimeError("Cannot add children directly!")

    def add_node(self, node):
        """Inserts this child in a proper location."""
        assert isinstance(node, OrderedBinaryTree)
        
        if self._fcompare(node._value, self._value):
            if self.left_child():
                self.left_child().add_node(node)
            else:
                self.set_left_child(node)
        else:
            if self.right_child():
                self.right_child().add_node(node)
            else:
                self.set_right_child(node)

    def find_match(self, value):
        """
        Returns a node of self where node.value == value,
        or None if no such node exists.
        """
        if self._value == value:
            return self
        if self._fcompare(value, self._value):
            if self.left_child():
                return self.left_child().find_match(value)
            else:
                return None
        else:
            if self.right_child():
                return self.right_child().find_match(value)
            else:
                return None
            
        
  
def test_obt():
    import random
    t = OrderedBinaryTree(0)
    for i in range(1, 50):
        t.add_node(OrderedBinaryTree(i))
    print(str(t))
    print("Height: " + str(t.height()))
    nodes = t.traverse()
    print("Nodes: " + ', '.join([str(node.get_value()) for node in nodes]))
    leaves = t.leaves()
    print("Leaves: " + ', '.join([str(node.get_value()) for node in leaves]))
    val = t.find_match(25)
    assert val.get_value() == 25
    val = t.find_match(52)
    assert not val
    t = OrderedBinaryTree(0)
    for i in range(1, 50):
        t.add_node(OrderedBinaryTree(random.randint(0, 100)))
    print(str(t))
    print(str(t.find_match(30)))
    print(str(t.find_match(29)))
    print(str(t.find_match(88)))
    print("Height: " + str(t.height()))
    nodes = t.traverse()
    print("Nodes: " + ', '.join([str(node.get_value()) for node in nodes]))
    leaves = t.leaves()
    print("Leaves: " + ', '.join([str(node.get_value()) for node in leaves]))    
    return t
    
if __name__ == "__main__":
    test_obt()
