class UnionFind:
    def __init__(self, size):
        self.roots = []
        for i in range(size):
            self.roots.append(i)
    
    def findroot(self,x):
        return(self.roots[x])
    
    def union(self,x,y):
        if (self.roots.count(x) <= self.roots.count(y)):
            self.roots = [self.roots[y] if elem==self.roots[x] else elem for elem in self.roots]
        else:
            self.roots = [self.roots[x] if elem==self.roots[y] else elem for elem in self.roots]
    
    def connected(self,x,y):
        return(self.roots[x]==self.roots[y])
    
    def getroots(self):
        return(self.roots)

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        provinces = UnionFind(len(isConnected[0]))
        for i in range(len(isConnected[0])):
            for j in range(i+1,len(isConnected[0])):
                if(isConnected[i][j] == 1):
                    provinces.union(i,j)
        roots = provinces.getroots()
        return(len(set(roots)))
                    