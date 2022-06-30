class UnionFind:
    def __init__(self, nodes):
        self.roots = []
        for i in range(nodes):
            self.roots.append(i)
            
    def findroot(self, x):
        return(self.roots[x])
    
    def getroots(self):
        return(self.roots)
    
    def union(self,x,y):
        if self.roots.count(x)<=self.roots.count(y):
            self.roots = [self.roots[y] if elem==self.roots[x] else elem for elem in self.roots]
        else:
            self.roots = [self.roots[x] if elem==self.roots[y] else elem for elem in self.roots]
            
    def connecteds(self):
        uniques = set(self.roots)
        return(len(uniques))

class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int: #note this uses minimum spanning tree which invoves finding the n-1 smallest edges and joining them
        edges = list(pipes)
        edges = edges + [[ind+1,0,well] for ind, well in enumerate(wells)] #the wells list acts as a single extra node 0 which connects to each node and has the weight of having a well
        edges = sorted(edges, key=lambda x:x[2]) #sort the list based on the 3rd element
        unionfind = UnionFind(int(n+1)) #make union find because we need to determine if their exists a loop which will happen if we try to union together two elements in the same group
        numofedges =0
        total = 0
        for i in range(len(edges)):
            x,y,cost = edges[i]
            if unionfind.findroot(x) != unionfind.findroot(y): # go through the orderered set of edges and join together if edges are not in the same component
                unionfind.union(x,y)
                numofedges+=1
                total+=cost #sum the weight
                if numofedges == n:
                    return(total)   
