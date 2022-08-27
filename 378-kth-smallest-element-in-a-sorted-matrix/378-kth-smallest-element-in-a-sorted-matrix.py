import heapq
class Solution:
    def kthSmallest1(self, matrix: List[List[int]], k: int) -> int:
        total =[]
        for i in range(len(matrix)):
            total+=matrix[i]
        heapq.heapify(total)
        for i in range (k-1):
            heapq.heappop(total)
        return(heapq.heappop(total))
    
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap=[]
        for i in range(len(matrix)):
            heap.append((matrix[i][0],i,0)) #heapify will sort by first value given in triplet
        heapq.heapify(heap)
        found=0
        while found<k-1:
            val,row,col =  heapq.heappop(heap)
            found+=1
            if col<len(matrix[0])-1:
                heapq.heappush(heap,(matrix[row][col+1],row,col+1))
        return(heapq.heappop(heap)[0])


            