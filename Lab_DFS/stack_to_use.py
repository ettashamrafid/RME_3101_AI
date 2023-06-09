class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev=None

class Linked_lst:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0

    def push(self,value):
        new_node=Node(value)
        self.size+=1
        if self.head==None:
            self.head=new_node
            self.tail=new_node

        else:
            self.tail.next=new_node
            new_node.prev=self.tail
            self.tail=new_node

    def pop(self):
        if self.head==None:
            print("Nothing to pop")

        else:
            self.size-=1
            if self.tail.prev==None:
                self.tail=self.tail.prev
                self.head=self.head.prev
            else:
                self.tail=self.tail.prev
                self.tail.next=None


    def length(self):
        return self.size


    def display(self):
        x=self.head
        while x!=None:
            print(x.value)
            x=x.next


    def peek(self):
        if self.head==self.tail==None:
            return ("Nothing at top")
        return self.tail.value



