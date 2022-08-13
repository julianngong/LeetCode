from collections import defaultdict
class Solution:
    def checkIfExist1(self, arr: List[int]) -> bool:
        table = defaultdict()
        for num in arr:
            if num == 0 and arr.count(0)>1:
                return(True)
            elif num != 0 and num not in table.keys():
                table[num]=index
                if ((2*num) in table) or ((num/2) in table):
                        return(True)
        return(False)
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()
        for n in arr:
            if 2*n in seen or n%2==0 and n//2 in seen: 
                return True
            else: 
                seen.add(n)
        return False
    
    