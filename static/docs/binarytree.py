"""
binarytree.py
"""

from tree import Tree

class BinaryTree(Tree):
    """
    A tree where there are at most 2 children per node.
    """

    def __init__(self, value):
        super().__init__(value)
        self._children = [None, None]
        
    def add_child(self, child):
        raise RuntimeError("Add child not allowed!")

    def set_left_child(self, child):
        assert isinstance(child, BinaryTree)
        assert not self.left_child()
        self._children[0] = child

    def set_right_child(self, child):
        assert isinstance(child, BinaryTree)
        assert not self.right_child()
        self._children[1] = child
        
    def left_child(self):
        return self._children[0]
        
    def right_child(self):
        return self._children[1]

    def traverse(self):
        nodes = []
        if self.left_child():
            nodes += self.left_child().traverse()
        nodes.append(self)
        if self.right_child():
            nodes += self.right_child().traverse()
        return nodes

