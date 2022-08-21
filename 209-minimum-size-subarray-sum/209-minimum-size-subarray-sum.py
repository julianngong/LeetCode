class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans=10000000
        left=0
        currentsum=0
        for right in range(len(nums)):
            currentsum+=nums[right]
            while (currentsum>=target):
                ans = min(ans, right - left +1)
                currentsum -= nums[left]
                left += 1
        if ans != 10000000:
            return(ans)
        else:
            return(0)
        
        