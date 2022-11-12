from typing import Any, List, Callable
import FIFO

class TreeNode:
    value: Any
    children: List['TreeNode']

    def __init__(self, value:Any):
        self.value=value
        self.children=[]


        def is_leaf(self)->bool:
            return len(self.children) == 0
           # return True
        # return False

    def add(self,child:'TreeNode')->None:
        self.children.append(child)

     def visit(self): #zaimplementuj jako funkcja, a nie metoda
        print(self.value)

    def for_each_deep_first(self,visit: Callable[['TreeNode'], None]):
        self.visit()

        if len(self.children) != 0:
            for child in self.children:
                child.for_each_deep_first(visit)

    def for_each_level_order(self, visit: Callable[['TreeNode'],None]): #POPRAW
        que=FIFO.Queue()
        que.enqueue(self.value)

        while len(que) !=0 :
            d=len(que)

            while d>0:
                p=que.peek()
                que.dequeue()
                p.visit()

            for i in range(len(p.children)):
                que.enqueue(p.children[i])
                d-=1

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

#root.for_each_deep_first(root.visit)
#root.for_each_level_order(root.visit)

