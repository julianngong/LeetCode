import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k==len(nums):
            return nums
        #this counter function gives key values pairs of the number followed by its count
        count =Counter(nums)
        #note the last input is a function which is the values use which will be a function called on each of the values
        return(heapq.nlargest(k,count.keys(),key=count.get))
           