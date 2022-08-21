class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        total=0
        for i in range(int(len(nums)/2)):
            total+=min(nums[2*i],nums[2*i+1])
        return(total)