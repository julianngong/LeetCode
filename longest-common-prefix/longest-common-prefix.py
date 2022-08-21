class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest = len(min(strs, key=len))
        i=0
        result=''
        while i<shortest:
            current=strs[0][i]
            for string in strs:
                if string[i]!=current:
                    return(result)
            result+=current
            i+=1
        return(result)
                
            