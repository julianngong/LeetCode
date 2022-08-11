class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        front=0
        back=len(nums)-1
        new=[0]*len(nums)
        for i in range(len(nums)-1,-1,-1):
            first = abs(nums[front])
            last = abs(nums[back])
            if first>last:
                new[i]=first**2
                front+=1
            else:
                new[i]=last**2
                back-=1
        return(new)
            