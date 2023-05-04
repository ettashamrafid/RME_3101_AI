#minheap
class minheap:
    def __init__(self):
        self.lst=[]

    def reheapup(self):
        i=len(self.lst)-1
        parent = (i-1)//2
        while i!=0:
            parent=(i-1)//2
            if self.lst[parent]>self.lst[i]:
                self.lst[parent],self.lst[i]=self.lst[i],self.lst[parent]
                i = parent
            else:
                break
        


    def reheapdown(self, current):
        smallest = current
        left=(2*current)+1
        right=(2*current)+2

        if left < len(self.lst) and self.lst[left] < self.lst[smallest]:
            smallest = left
        if right < len(self.lst) and self.lst[right] < self.lst[smallest]:
            smallest = right

        if current != smallest:
            self.lst[current], self.lst[smallest] = self.lst[smallest], self.lst[current]
            self.reheapdown(smallest)
        
        
    def enqueue(self,value):        
        self.lst.append(value)
        self.reheapup()

    def dequeue(self):
        if len(self.lst)==0:
            print("Nothing to dequeue")
        else:
            self.lst[0],self.lst[len(self.lst)-1]=self.lst[len(self.lst)-1],self.lst[0]
            temp=self.lst.pop()
            self.reheapdown(0)

        return temp

    def display(self):
        [print(i) for i in self.lst]

    def top(self):
        return self.lst[0]



