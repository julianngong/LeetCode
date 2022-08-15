class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxcount = 0
        count=0
        j=0
        flipped = False
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                nums[i]=1
                while i+j<len(nums) and nums[i+j] == 1:
                    count+=1
                    j+=1
                maxcount = max(count,maxcount)
                count=0
                j=0
        maxcount = max(count,maxcount)
        return(maxcount)
            