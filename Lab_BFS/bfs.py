import queue_to_use as qc
import file_handling as fh

class bfs:
    def __init__(self,matrix):
        self.matrix=matrix

    def path(self,source,destination):
        self.source=source
        self.destination=destination

        lst=qc.Linked_lst()
        visited=[]
        lst.add(self.source)
        flag=0
        
        while lst.length()!=0:

            queue_head=lst.header().value
            lst.pop()
            visited.append(queue_head)
            if self.destination==visited[-1]:
                flag=1
                print("Path Found")
                break
            else:
                for neighbor in self.matrix[queue_head]:
                    if neighbor not in visited:
                        lst.add(neighbor)

        if flag==0:
            print("Path not found")



adj=fh.file_handling()
adj.data_fetch('input.txt')
for iteration in range(adj.no_query):
    bfs_obj=bfs(adj.adj)
    bfs_obj.path(adj.source[iteration], adj.destination[iteration])