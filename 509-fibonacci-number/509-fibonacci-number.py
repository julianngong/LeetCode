seen={0:0}
class Solution:
    def fib(self, n: int) -> int:
        if n in seen:
            return(seen[n])
        else:
            if n ==1 or n==2:
                seen[n]=1
            else:
                seen[n]=self.fib(n-1)+self.fib(n-2)
        return(seen[n])