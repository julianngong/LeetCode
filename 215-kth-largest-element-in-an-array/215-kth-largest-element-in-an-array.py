import heapq
class Solution:
    def findKthLargest1(self, nums, k):
        nums = [-x for x in nums]
        heapq.heapify(nums)
        for i in range (k-1):
            heapq.heappop(nums)
        return nums[0]*-1
    def findKthLargest(self, nums, k):
        return heapq.nlargest(k, nums)[-1]