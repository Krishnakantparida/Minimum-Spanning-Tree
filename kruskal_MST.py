class Graph:
    def __init__(self,vertices):
        self.v = vertices
        self.graph = []
    def add_edge(self,x,y,z):
        self.graph.append([x,y,z])
    def find(self,parent,i):
        if parent[i] == i:
            return i
        return self.find(parent,parent[i])
    def union(self,parent,rank,j,k):
        j_root = self.find(parent,j)
        k_root = self.find(parent,k)
        if rank[j_root] < rank[k_root]:
            parent[j_root] = k_root
        elif rank[j_root] > rank[k_root]:
            parent[k_root] = j_root
        else:
            parent[k_root] = j_root
            rank[j_root] += 1
    def Kruskal_MST(self):
        result = []
        a = 0
        b = 0
        self.graph = sorted(self.graph,key = lambda item: item[2])
        parent = []
        rank = []
        for node in range(self.v):
            parent.append(node)
            rank.append(0)
        while b < self.v - 1:
            x,y,z = self.graph[a]
            a += 1
            p = self.find(parent,x)
            q = self.find(parent,y)
            if p != q:
                b += 1
                result.append([x,y,z])
                self.union(parent,rank,x,y)
        print "Following are the edges in the constructed MST"
        print "Edge\tWeight"
        total = 0
        for node1,node2,weight in result:
            print node1, "-", node2, "\t", weight
            total += weight
        print "Total weight of the MST =", total
graph = Graph(6)
graph.add_edge(0,1,4)
graph.add_edge(0,2,1)
graph.add_edge(0,3,3)
graph.add_edge(0,4,6)
graph.add_edge(1,3,2)
graph.add_edge(2,4,9)
graph.add_edge(3,4,7)
graph.add_edge(3,5,8)
graph.add_edge(4,5,5)
graph.Kruskal_MST()
