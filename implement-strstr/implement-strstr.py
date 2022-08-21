class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        front=0
        back=len(needle)
        if back==0:
            return 0
        while back<=len(haystack):
            window = haystack[front:back]
            if window == needle:
                return(front)
            front+=1
            back+=1
        return(-1)