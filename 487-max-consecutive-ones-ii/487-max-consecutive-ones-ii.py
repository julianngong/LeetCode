class Solution:
    def findMaxConsecutiveOnes1(self, nums: List[int]) -> int:
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
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxcount = 0
        left,right=0,0
        num0 = 0
        while right<len(nums):
            if nums[right]==0:
                num0+=1
            while num0==2:
                if nums[left]==0:
                    num0-=1
                left+=1
            maxcount = max(maxcount,right-left+1)
            right+=1
        return(maxcount)
            