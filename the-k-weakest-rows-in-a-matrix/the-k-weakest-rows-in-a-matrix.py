import heapq
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        counts={}
        for i,row in enumerate(mat):
            counts[i]=row.count(1)
        return(heapq.nsmallest(k,counts.keys(),counts.get))
            
        