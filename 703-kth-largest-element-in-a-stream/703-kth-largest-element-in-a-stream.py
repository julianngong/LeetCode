import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        heapq.heapify(nums)
        while len(nums)>k:
            heapq.heappop(nums)
        self.heap = nums
        self.k = k

    def add(self, val: int) -> int: #kth largest is the same as keeping k elements of a min heap and taking the first element rathert thn using the k biggest elements function
        heapq.heappush(self.heap,val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)