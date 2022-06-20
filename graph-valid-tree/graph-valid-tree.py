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
            
    def connected(self):
        uniques = set(self.roots)
        if len(uniques)==1:
            return(True)
        else:
            return(False)
        
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != (n-1):
            return(False)
        else:
            tree = UnionFind(n)
            for i in range(len(edges)):
                tree.union(edges[i][0],edges[i][1])
            return(tree.connected())
                
        