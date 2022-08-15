class Solution:
    def findDisappearedNumbers1(self, nums: List[int]) -> List[int]:
        notin = set()
        for i in range(len(nums)):
            if (i+1) not in nums and (i+1) not in notin:
                notin.add(i+1)
        return(list(notin))
    #note dont ever wanna check if element is in list as this is too slow, if you need to do this use a hashmap
    def findDisappearedNumbers2(self, nums: List[int]) -> List[int]:
        hash_table = {}
        for num in nums:
            hash_table[num]=1
        result=[]
        for i in range(len(nums)):
            if (i+1) not in hash_table:
                result.append(i+1)
        return(result)
    def findDisappearedNumbers(self, nums): #we can inplace mark a element of string as seen by multiplying by -1 but when inspecting elements, only look at the absolute value
        for i in range(len(nums)):
            indexmatchingseennum = abs(nums[i]) - 1
            if nums[indexmatchingseennum] > 0:
                nums[indexmatchingseennum] *= -1
        
        result = []    
        for i in range(1, len(nums) + 1):
            if nums[i - 1] > 0:
                result.append(i)     
        return result   