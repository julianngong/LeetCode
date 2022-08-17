class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        maximum = [-1,0]
        secondmax = [-1,0]
        for i, num in enumerate(nums):
            if num*2>maximum[1]:
                secondmax=maximum
                maximum=[i,num*2]
            elif num*2>secondmax[1]:
                secondmax=[i,num*2]
            print(num)
            print(secondmax)
            print(maximum)
        if maximum[1]/2>=secondmax[1]:
            return(maximum[0])
        else:
            return(-1)
            
        