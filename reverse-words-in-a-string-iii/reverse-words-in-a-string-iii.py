class Solution:
    def reverseWords(self, s: str) -> str:
        words=s.split()
        output=''
        for i in range(len(words)):
            string=''
            output+= ' ' + string.join(list(reversed(list(words[i])))) 
        return(output[1:])