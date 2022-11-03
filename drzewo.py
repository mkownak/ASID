from typing import Any, List

class TreeNode:
    value: Any
    children: List['TreeNode']

    def __init__(self, value:Any):
        self.value=value
        self.children=[]

    def is_leaf(self)->bool:
        if self.children is None:
            return True
        else:
            return False

    def add(self,child:'TreeNode'):
        self.children.append(child)

    def for_each_deep_first(self,visit=set()): #dokoncz
        if self.value not in visit:
            print(self.value)
            visit.add(self.value)
            for child in self.children:
                 self.for_each_deep_first()




root=TreeNode(10)
root.add(5)
root.add(2)
root.for_each_deep_first()
