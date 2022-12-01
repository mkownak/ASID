from typing import Any


class BinaryNode:
    value: Any
    left_child: 'BinaryNode'
    right_child: 'BinaryNode'

    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def min(self, min_node=None) -> 'BinaryNode':
        if min_node is None:
            min_node = self

        if self.left_child:
            if self.left_child.value < min_node.value:
                min_node = self.left_child
                return self.left_child.min(min_node)

        if self.right_child:
            if self.right_child.value < min_node.value:
                min_node = self.right_child
                return self.right_child.min(min_node)

        return min_node


class BinarySearchTree:
    root: BinaryNode

    def __init__(self, root:'BinaryNode'):
        self.root = root

    def _insert(self, node: 'BinaryNode', value: Any) -> BinaryNode:
        if node.value < value:
            node.left_child = BinaryNode(value)
        else:
            node.right_child = BinaryNode(value)










root=BinaryNode(8)
root.left_child=BinaryNode(3)
root.right_child=BinaryNode(10)
print(root)
print(root.left_child)
print(root.right_child)
print(root.min())
