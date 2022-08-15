class Solution:
    def findDisappearedNumbers1(self, nums: List[int]) -> List[int]:
        notin = set()
        for i in range(len(nums)):
            if (i+1) not in nums and (i+1) not in notin:
                notin.add(i+1)
        return(list(notin))
    #note dont ever wanna check if element is in list as this is too slow, if you need to do this use a hashmap
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        hash_table = {}
        for num in nums:
            hash_table[num]=1
        result=[]
        for i in range(len(nums)):
            if (i+1) not in hash_table:
                result.append(i+1)
        return(result)