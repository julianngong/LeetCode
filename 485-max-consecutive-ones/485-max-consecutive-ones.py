class Solution:
    def findMaxConsecutiveOnes2(self, nums: List[int]) -> int:
        back = 0
        front = 0
        longest = 0
        while front != len(nums):
            if nums[back] != 1:
                back+=1
                front=back
            else:
                if nums[front]!=1:
                    front+=1
                    back=front
                else:
                    if front-back+1>longest:
                        longest = front-back+1
                    front+=1
        return(longest)
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        currentmax = 0
        finalmax = 0
        for num in nums:
            if num == 1:
                currentmax+=1
            else:
                finalmax = max(finalmax,currentmax)
                currentmax=0 
        finalmax = max(finalmax,currentmax)
        return(finalmax)
            