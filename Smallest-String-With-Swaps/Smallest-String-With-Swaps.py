 class UnionFind:
    def __init__(self,size):
        self.roots = []
        for i in range(size):
            self.roots.append(i)
    def Findroot(self,x):
        return(self.roots[x])
    def getroots(self):
        return(self.roots)
    def Union(self,x,y):
        if self.roots.count(x)<=self.roots.count(y):
            self.roots = [self.roots[y] if elem==self.roots[x] else elem for elem in self.roots]
        else:
            self.roots = [self.roots[x] if elem==self.roots[y] else elem for elem in self.roots]

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        graph = UnionFind(len(s))
        for i in range(len(pairs)):
            graph.Union(pairs[i][0],pairs[i][1])
        roots = graph.getroots()
        componentandletters = defaultdict(lambda: [[],[]])
        for i in range(len(s)):
            componentandletters[roots[i]][1].append(s[i])
            componentandletters[roots[i]][0].append(i)
        output=''
        for key in componentandletters.keys():
            componentandletters[key][1].sort()
        for i in range(len(s)):
            output = output + componentandletters[roots[i]][1][0]
            componentandletters[roots[i]][1] = componentandletters[roots[i]][1][1:]
        return output
