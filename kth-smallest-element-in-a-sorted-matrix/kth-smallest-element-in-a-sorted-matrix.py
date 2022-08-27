import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        total =[]
        for i in range(len(matrix)):
            total+=matrix[i]
        heapq.heapify(total)
        for i in range (k-1):
            heapq.heappop(total)
        return(heapq.heappop(total))
            