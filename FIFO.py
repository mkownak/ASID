from typing import Any

class Node:
    def __init__(self, value:Any, next=None):
        self.value=value
        self.next=next

class Queue:
    def __init__(self):
        self.front=None
        self.back=None
        self.size=0

    def peek(self)->Any:
        return self.front

    def enqueue(self,element:Any)->None:
        node=Node(element)

        if self.size==0:
            self.front=self.back=node

        self.back.next=node
        self.back=self.back.next
        self.size=self.size+1

    def dequeue(self)->Any:
        if self.size==0:
            print("kolejka jest pusta")
            return

        element=self.front.value
        self.front=self.front.next
        self.size=self.size-1

        return element

    def print(self)->None:
        node=self.front

        while node is not None:
            print(node.value)
            node=node.next

    def __len__(self):
        return self.size
