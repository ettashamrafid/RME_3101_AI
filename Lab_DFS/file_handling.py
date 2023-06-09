class file_handling:
    def __init__(self):
        self.adj={}
        self.source=[]
        self.destination=[]
        self.no_query=0

    def data_fetch(self,f_name):
        self.f_name=f_name
        with open(self.f_name) as inputs:
            temp=inputs.readline().split()
            for i in range(int(temp[1])):
                edge=inputs.readline().split()
                if edge[0] not in self.adj:
                    self.adj[edge[0]]=[edge[1]]
                else:
                    self.adj[edge[0]].append(edge[1])


            self.no_query=int(inputs.readline())
            for i in range(self.no_query):
                checker=inputs.readline().split()
                self.source.append(checker[0])
                self.destination.append(checker[1])

