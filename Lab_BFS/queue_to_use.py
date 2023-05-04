class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        

class Linked_lst:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0

    def add(self,value):
        new_node=Node(value)
        self.size+=1
        if self.head==None:
            self.head=new_node
            self.tail=new_node

        else:
            self.tail.next=new_node
            self.tail=new_node


    def pop(self):
        if self.head==None:
            print("nothing to pop")
        else:
            self.head=self.head.next
            self.size-=1

    def header(self):
        return self.head

    def length(self):
        return self.size


    def display(self):
        x=self.head
        while x:
            print(x.value)
            x=x.next

