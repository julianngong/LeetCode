class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        seen={}
        current=(0,nums[0])
        seen[0]=True
        for i,num in enumerate(nums):
            index=(current[0]+k)%len(nums)
            temp=(index,nums[index])
            nums[temp[0]]=current[1]
            if temp[0] in seen:
                current=(temp[0]+1,nums[(temp[0]+1)%len(nums)])
                seen[temp[0]+1]=True
            else:
                current=(temp[0],temp[1])
                seen[temp[0]]=True

        """
        Do not return anything, modify nums in-place instead.
        """
        