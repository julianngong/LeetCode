class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        front=0
        back=len(nums)-1
        new=[]
        while back>=front:
            first = abs(nums[front])
            last = abs(nums[back])
            if first>last:
                new.insert(0, first**2)
                front+=1
            else:
                new.insert(0, last**2)
                back-=1
        return(new)
            