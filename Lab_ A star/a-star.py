import priority_queue as pq
import weight_edge as we

class Node:
    def __init__(self,name):
        self.name=name
        self.priority=0

    def __eq__(self,other):
        return self.priority==other.priority
    def __gt__(self,other):
        return self.priority>other.priority
    def __lt__(self,other):
        return self.priority<other.priority



class A_star:
    def __init__(self,source,destination,adj,heurestics):
        self.source=source
        self.destination=destination
        self.adj=adj
        self.heu=heurestics
        self.parent={}
        self.node_cost={}
        self.flag=0

    def execution(self):
        
        priority_queue=pq.minheap()
        new_node=Node(self.source)
        self.node_cost[self.source]=0
        new_node.priority=self.node_cost[self.source]
        priority_queue.enqueue(new_node)
        while len(priority_queue.lst)!=0:
            visited=priority_queue.dequeue()
            if visited.name==self.destination:
                self.flag=1
                break

            for neighbor in self.adj[visited.name]:
                if neighbor not in self.parent:
                    
                    self.parent[neighbor]=visited.name
                    self.node_cost[neighbor]=self.node_cost[visited.name] + self.adj[visited.name][neighbor]
                    over_node=Node(neighbor)
                    over_node.priority=self.node_cost[neighbor]+self.heu[neighbor]
                    priority_queue.enqueue(over_node)
                
                else:
                    if self.node_cost[visited.name]+self.adj[visited.name][neighbor]<self.node_cost[neighbor]:
                        self.node_cost[neighbor]=self.node_cost[visited.name] + self.adj[visited.name][neighbor]
                        self.parent[neighbor]=visited.name
                        over_node=Node(neighbor)
                        over_node.priority=self.node_cost[neighbor]+self.heu[neighbor]
                        priority_queue.enqueue(over_node)


    def print_path(self):
        if self.flag==0:
            print("Path Not Found")
        else:
            path_lst=[]
            node=self.destination
            path_lst.append(node)
            while node!=self.source:
                node=self.parent[node]
                path_lst.append(node)

            print(path_lst)
            print(self.node_cost[self.destination])




heurastics1={
    'S': 8,
    'A': 3,
    'B': 7,
    'C': 2,
    'G': 0
}
graph = we.weight_edge()
graph.connect('S','A',2)
graph.connect('S','B',4)
graph.connect('A','B',1)
graph.connect('A','C',4)
graph.connect('B','C',2)
graph.connect('B','G',6)
graph.connect('C','G',3)
g1=A_star('S','G',graph.edge_weight,heurastics1)
g1.execution()
g1.print_path()




