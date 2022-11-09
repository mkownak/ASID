from typing import Any, List

class TreeNode:
    value: Any
    children: List['TreeNode']

    def __init__(self, value:Any):
        self.value=value
        self.children=[]


    def is_leaf(self)->bool:
        if len(self.children)==0:
            return True
        else:
            return False

    def add(self,child:'TreeNode')->None:
        self.children.append(child)

    def print(self): #DFS print
        print(self.value)

        if len(self.children)!=0:
            for child in self.children:
                child.print()

    def FELO(self): #for_each_level_order
        return

    def search(self,value):
        if self.value==value:
            return True

        if len(self.children)!=0:
            for child in self.children:
                temp=child.search(value)

                if temp!=0:
                    return temp
        return False


root=TreeNode("F")
root.add(TreeNode("B"))
root.add(TreeNode("G"))
root.children[0].add(TreeNode("A"))
root.children[0].add(TreeNode("D"))
root.children[1].add(TreeNode("I"))
root.children[0].children[1].add(TreeNode("C"))
root.children[0].children[1].add(TreeNode("E"))
root.children[1].children[0].add(TreeNode("H"))
