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
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        tree = UnionFind(n)
        for i in range(len(edges)):
            tree.union(edges[i][0],edges[i][1])
        return(tree.connecteds())

        