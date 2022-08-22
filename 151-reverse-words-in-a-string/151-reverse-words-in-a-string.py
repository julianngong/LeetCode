class Solution:
    def reverseWords1(self, s: str) -> str:
        n=len(s)
        s+=' '
        output = ''
        front=0
        back=0
        while back<len(s):
            if s[front]==' ':
                front+=1
                back=front
            else:
                if back==len(s)-1 or s[back]==' ':   
                    word=s[front:back]
                    if output == '':
                        output = word + output
                    else:
                        output = word + ' ' + output
                    front=back+1
                    back+=1
                else:
                    back+=1
        return(output)
    def reverseWords(self, s: str) -> str:
        x = s.split()
        x.reverse()
        y = " ".join(x)
        return y
        