from typing import Any

class Node:
    def __init__(self, value=None, next=None):
        self.value=value
        self.next=next

class LinkedList:
    def __init__(self, head=None):
        self.head=head
        self.tail=Node()

    def Push(self, value)->None:
        node=Node(value)

        if self.head is None:
            self.head=node
            self.tail=node
            return

        tempNode=self.head
        self.head=node
        node.next=tempNode

    def Append(self, value)->None:
        node=Node(value)
        if self.head is None:
            self.head=node
            self.tail=node
            return

        currentNode=self.head
        while True:
            if currentNode.next is None:
                currentNode.next=node
                self.tail=node
                break
            currentNode=currentNode.next

    def NodePos(self,at:int)->Node:
        i=0
        currentNode=self.head
        while(i<at):
            currentNode=currentNode.next
            i=i+1
        return currentNode.value

    def InsertNode(self,value:Any,after):
        node=Node(value)
        currentNode=self.head
        i=0

        while(i<after):
            currentNode=currentNode.next
            i=i+1
        temp=currentNode.next
        currentNode.next=node
        currentNode=currentNode.next
        currentNode.next=temp

    def Pop(self):
        if self.head is None:
            print("lista jest pusta, nie mozna pop")
            return

        wynik=self.head.value
        self.head=self.head.next

        return wynik

    def RemoveLast(self):
        if self.head is None:
            print("lista jest pusta, nie mozna Remove Last")
            return

        tail=self.tail.value
        currentNode=self.head

        while True:
            if currentNode.next.value == self.tail.value:
                currentNode.next=None
                break
            currentNode=currentNode.next

        return tail

    def Remove(self,after):
        currentNode=self.head
        i=0

        while(i<after):
            currentNode=currentNode.next
            i=i+1

        currentNode.next=currentNode.next.next

    def Len(self):
        node=self.head
        len=0

        while node is not None:
            len=len+1
            node=node.next
        return len


    def Print(self)->None:
        node=self.head

        while node is not None:
            print(node.value,"-> ", end="")
            node=node.next
        print("None")

list_=LinkedList()
list_.Append(3)
list_.Append(4)
list_.Push(5)
#print(list_.NodePos(0))
list_.Print()
list_.InsertNode(8,1)
list_.Print()
print(list_.Pop())
print(list_.RemoveLast())
list_.Print()
list_.Append(6)
list_.Append(10)
list_.Print()
list_.Remove(1)
list_.Print()
print(list_.Len())





