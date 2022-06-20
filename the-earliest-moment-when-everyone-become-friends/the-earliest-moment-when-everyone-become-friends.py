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
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs.sort(key=lambda x: x[0])
        tree = UnionFind(n)
        print(tree.getroots())
        for i in range(len(logs)):
            tree.union(logs[i][1],logs[i][2])
            print(tree.getroots())
            if (tree.connected()==True):
                return(logs[i][0])
        return(-1)
        