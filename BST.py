from typing import Any,List
import graphviz


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

    def contains(self, value: Any):
        if self.value == value:
            return True

        if self.value > value:
            if self.left_child:
                return self.left_child.contains(value)
        else:
            if self.right_child:
                return self.right_child.contains(value)

        return False

    def show(self, dot=None):
        if dot is None:
            dot = graphviz.Digraph("BST_Tree", format="png")

        dot.node(str(self),str(self.value))

        if self.left_child:
            dot.node(str(self.left_child),str(self.left_child.value))
            dot.edge(str(self),str(self.left_child))
            self.left_child.show(dot)

        if self.right_child:
            dot.node(str(self.right_child),str(self.right_child.value))
            dot.edge(str(self),str(self.right_child))
            self.right_child.show(dot)

        dot.render(directory='doctest-output').replace('\\', '/')




class BinarySearchTree:
    root: BinaryNode

    def __init__(self, root: 'BinaryNode'):
        self.root = root

    def insert(self, value: Any):
        self.root = self._insert(root, value)

    def _insert(self, node: 'BinaryNode', value: Any) -> BinaryNode:
        if node.value > value:
            if node.left_child:
                return self._insert(node.left_child, value)
            else:
                node.left_child = BinaryNode(value)
        else:
            if node.right_child:
                return self._insert(node.right_child, value)
            else:
                node.right_child = BinaryNode(value)
        return self.root

    def insert_list(self, list_: List[Any]) -> None:
        for i in range(len(list_)):
            self.insert(list_[i])

    def contains(self, value: Any):
        return self.root.contains(value)

    def show(self):
        self.root.show()

    def remove(self,value):
        self.root=self._remove(self.root,value)

    def _remove(self, node: BinaryNode, value):
        if node is None:
            return node

        if node.value == value:
            if node.left_child is None and node.right_child is None:
                return None

            if node.left_child is not None and node.right_child is None:
                return node.left_child

            if node.right_child is not None and node.left_child is None:
                return node.right_child

            next=node.right_child
            while next.left_child:
                next=next.left_child
            node.value=next.value
            node.right_child=self._remove(node.right_child,node.value)

        if node.value>value:
            node.left_child=self._remove(node.left_child,value)
        else:
            node.right_child=self._remove(node.right_child,value)

        return node



root = BinaryNode(8)
tree = BinarySearchTree(root)
tree.insert_list([3,1,6,4,7,10,14,13])
tree.remove(8)
tree.show()
