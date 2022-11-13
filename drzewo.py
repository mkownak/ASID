from typing import Any, List, Callable, Union
import FIFO
import graphviz

class TreeNode:
    value: Any
    children: List['TreeNode']

    def __init__(self, value:Any)->None:
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

    def for_each_level_order(self,visit: Callable[['TreeNode'], None]): #POPRAW
        que=FIFO.Queue()
        que.enqueue(self)

        while len(que)!=0:
            d=len(que)

            while d>0:
                p=que.peek()
                que.dequeue()
                p.value.visit() #print(p.value.value)

                for i in p.value.children:
                    que.enqueue(i)
                d-=1


    def search(self,value:Any)->Union['TreeNode', None]:
        if self.value==value:
            return self

        if len(self.children)!=0:
            for child in self.children:
                temp=child.search(value)

                if temp!=0:
                    return temp
        return False

    def print(self)->None: #DFS
        print(self.value)

        if len(self.children) != 0:
            for child in self.children:
                child.print()



class Tree:
    root: TreeNode

    def __init__(self,root:Any=None):
        self.root=root

    def add(self,value:Any,parent_name:Any)->None:
        if TreeNode.search(root,parent_name)==False:
            print("Nie mozna dodac dziecka do nieistniejacego rodzica")
            return
        else:
            node=TreeNode(value)
            parent=TreeNode.search(root,parent_name)
            TreeNode.add(parent,node)

    def for_each_level_order(self, visit: Callable[['TreeNode'], None]) -> None:
        TreeNode.for_each_level_order(root,visit)

    def for_each_deep_first(self, visit: Callable[['TreeNode'], None]) -> None:
        TreeNode.for_each_deep_first(root,visit)

    def show(self): #dokoncz
        dot = graphviz.Digraph("Tree",format="png")

        dot.node('root',str(self.root.value))

        if len(self.root.children)!=0:
            for child in self.root.children:
                dot.node(str(child),str(child.value))
                dot.edge('root',str(child))


        dot.render(directory='doctest-output').replace('\\', '/')



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
#root.print()

tree=Tree(root)
#tree.add("K","A")
#root.print()
tree.show()
#tree.for_each_level_order(tree.root.visit)
#tree.for_each_deep_first(tree.root.visit)

