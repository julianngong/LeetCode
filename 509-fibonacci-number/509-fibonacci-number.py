class Solution:
    def __init__(self):
        self.seen = {}
    def fib(self, n: int) -> int:
        if n in self.seen:
            return(self.seen[n])
        else:
            if n ==1 or n==2:
                self.seen[n]=1
            elif n==0:
                self.seen[n]=0
            else:
                self.seen[n]=self.fib(n-1)+self.fib(n-2)
        return(self.seen[n])