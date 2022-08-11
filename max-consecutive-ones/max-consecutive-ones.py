class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
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
            