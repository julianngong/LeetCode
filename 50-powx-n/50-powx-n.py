
class Solution:
    def __init__(self):
        self.memo={}
    def myPow(self, x: float, n: int) -> float:
        if n==0:
            self.memo[n]=1
        if n==1:
            self.memo[n]=x
        if n==-1:
            self.memo[n]=1/x
        if n not in self.memo.keys():
            temp1=round(n/2)
            temp2=n-temp1
            self.memo[n]=(self.myPow(x,temp1))*(self.myPow(x,temp2))
        return(self.memo[n])
            

