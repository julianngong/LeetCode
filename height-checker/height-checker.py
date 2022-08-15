class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        unsorted = heights.copy()
        heights.sort()
        j=0
        count=0
        for i in range(len(heights)):
            if unsorted[j]!=heights[i]:
                count+=1
            j+=1
        return(count)
                
        