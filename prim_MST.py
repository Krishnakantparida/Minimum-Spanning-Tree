class Graph:
    def __init__(self,vertices):
        self.v = vertices
        self.graph = [[0 for columns in range(vertices)] for row in range(vertices)]
    def Prim_MST(self):
        key = [999]*self.v
        key[0] = 0
        parent = [None]*self.v
        parent[0] = -1
        main = [False]*self.v
        for j in range(self.v):
            a = self.least_key(key,main)
            main[a] = True
            for b in range(self.v):
                if self.graph[a][b] > 0 and main[b] == False and key[b] > self.graph[a][b]:
                    key[b] = self.graph[a][b]
                    parent[b] = a
        self.display_MST(parent)

    def least_key(self,key,main):
        least = 999
        for i in range(self.v):
            if key[i] < least and main[i] == False:
                least = key[i]
                least_index = i
        return least_index
    def display_MST(self,parent):
        #in this graph, adjacency matrix is made..
        print "Edge\tWeight"
        total = 0
        for i in range(1,self.v):
            print parent[i], '-', i, "\t", self.graph[i][parent[i]]
            total += self.graph[i][parent[i]]
        print "Total weight of the MST =", total

graph = Graph(7)
graph.graph = [[0,4,6,9,2,999,999],
               [4,0,999,5,999,1,999],
               [6,999,0,999,7,3,999],
               [9,5,999,0,999,999,8],
               [2,999,7,999,0,999,1],
               [999,1,3,999,999,0,999],
               [999,999,999,8,1,999,0]]
graph.Prim_MST()
