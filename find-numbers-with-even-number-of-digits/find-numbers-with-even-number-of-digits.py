class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        evens=0
        powers=[10,1000,100000]
        for num in nums:
            for power in powers:
                if 1<=num/power<10:
                    evens+=1
        return(evens)
                
        