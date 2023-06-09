import stack_to_use as su
import file_handling as fh

class Dfs:
    def __init__(self,matrix):
        self.matrix=matrix

    def path(self,source,destination):
        self.source=source
        self.destination=destination

        lst=su.Linked_lst()
        lst.push(self.source)
        visited=[]
        flag=0
        
        
        while lst.length()!=0:
            temp=lst.peek()
            lst.pop()
            visited.append(temp)
            if visited[-1]==self.destination:
                flag=1
                print('Path Found')
                break
            else:
                
                for neighbor in self.matrix[temp]:
                    if neighbor not in visited:
                        lst.push(neighbor)

        if flag==0:
            print("Path Not Found")


adj=fh.file_handling()
adj.data_fetch('input.txt')

for iteration in range(adj.no_query):
    dfs_obj=Dfs(adj.adj)
    dfs_obj.path(adj.source[iteration],adj.destination[iteration])
