class Solution:
    def moveZeroes1(self, nums): #more efficient but dont get it
        zero = 0  # records the position of "0"
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1
    def moveZeroes(self, nums):
        lastnonzero = 0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[lastnonzero] = nums[i]
                lastnonzero+=1
        for i in range(lastnonzero,len(nums),++1):
            nums[i]=0
        print(nums)