class weight_edge:
    def __init__(self):
        self.edge_weight={}

    def connect(self,source,destination,weight):
        if source not in self.edge_weight:
            self.edge_weight[source]={}
            if destination not in self.edge_weight[source]:
                self.edge_weight[source][destination]=weight

        else:
            self.edge_weight[source][destination]=weight

    def display(self):
        for keys,values in self.edge_weight.items():
            for weight in values:
                print('{}{}:{}'.format(keys,weight,self.edge_weight[keys][weight]))
        # print(self.edge_weight)