from typing import Any, Callable

def visit(a):
    print(a)

class BinaryNode:
    value: Any
    left_child: "BinaryNode"
    right_child: "BinaryNode"

    def __init__(self,value:Any):
        self.value=value
        self.left_child=None
        self.right_child=None

    def is_leaf(self):
        if self.left_child is None and self.right_child is None:
            return True
        return False

    def add_left_child(self,value:Any):
        self.left_child=BinaryNode(value)

    def add_right_child(self,value:Any):
        self.right_child=BinaryNode(value)

    def traverse_in_order(self, visit:Callable[[Any],None]):
        if self.left_child is not None:
            self.left_child.traverse_in_order(visit)

        visit(self.value)

        if self.right_child is not None:
            self.right_child.traverse_in_order(visit)

    def traverse_post_order(self, visit:Callable[[Any],None]):
        if self.left_child is not None:
            self.left_child.traverse_post_order(visit)

        if self.right_child is not None:
            self.right_child.traverse_post_order(visit)

        visit(self.value)

    def traverse_pre_order(self, visit:Callable[[Any],None]):
        visit(self.value)

        if self.left_child:
            self.left_child.traverse_pre_order(visit)

        if self.right_child:
            self.right_child.traverse_pre_order(visit)

    def __str__(self,l1=None, napis=None):
        if l1 is None:
            l1=[]
            napis=""
        l1.append(self.value)

        if self.left_child:
            self.left_child.__str__(l1,napis)

        if self.right_child:
            self.right_child.__str__(l1,napis)

        for i in l1:
            napis+=str(i)+" "
        return napis






root=BinaryNode(10)
root.add_left_child(9)
root.add_right_child(2)

root.left_child.add_left_child(1)
root.left_child.add_right_child(3)

root.right_child.add_left_child(4)
root.right_child.add_right_child(6)

#root.traverse_in_order(visit)
#root.traverse_post_order(visit)
#root.traverse_pre_order(visit)

print(root)
