class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j=0
        seen=[]
        for i in range(len(nums)):
            if nums[i] not in seen:
                nums[j]=nums[i]
                seen.append(nums[j])
                j+=1
        return(j)