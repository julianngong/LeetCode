class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        p={}
        p[0]=nums[0]
        for i in range(1,len(nums)):
            p[i]=p[i-1]+nums[i]
        if p[len(nums)-1]-nums[0]==0:
            return(0)
        for i in range(1,len(nums)):
            if p[i-1]==p[len(nums)-1]-p[i]:
                return(i)
        return(-1)
        