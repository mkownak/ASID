from typing import Any


class BinaryNode:
    value: Any
    left_child: 'BinaryNode'
    right_child: 'BinaryNode'

    def __init__(self, value, left_child=None, right_child=None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child

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
