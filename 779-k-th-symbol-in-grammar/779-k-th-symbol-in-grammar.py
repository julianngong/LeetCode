class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n==1:
            return(0)
        newk=round((k/2)+0.01)
        result=self.kthGrammar(n-1,newk)
        if result == 0:
            if k%2==0:
                return(1)
            else:
                return(0)
        else:
            if k%2==0:
                return(0)
            else:
                return(1)