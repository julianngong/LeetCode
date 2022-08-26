seen={1:1,2:2}
class Solution:
    def climbStairs(self, n: int) -> int:
        if n in seen.keys():
            return(seen[n])
        seen[n] = self.climbStairs(n-1)+self.climbStairs(n-2)
        return(seen[n])
        