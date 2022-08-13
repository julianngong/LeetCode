class Solution:
    def removeDuplicates1(self, nums: List[int]) -> int:
        j=0
        seen=[]
        for i in range(len(nums)):
            if nums[i] not in seen:
                nums[j]=nums[i]
                seen.append(nums[j])
                j+=1
        return(j)
    def removeDuplicates(self, nums: List[int]) -> int:
        if (len(nums) == 0):
            return 0
        i=0
        for j in range(1,len(nums)):
            if nums[j] != nums[i]:
                i+=1
                nums[i]=nums[j]
        return(i+1)