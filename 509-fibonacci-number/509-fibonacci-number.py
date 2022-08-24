seen={0:0,1:1}
class Solution:
    def fib(self, n: int) -> int:
        if n in seen:
            return(seen[n])
        else:
            seen[n]=self.fib(n-1)+self.fib(n-2)
            return(seen[n])