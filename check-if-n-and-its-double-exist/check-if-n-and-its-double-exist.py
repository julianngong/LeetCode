from collections import defaultdict
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        table = defaultdict()
        zeroseen = False
        for num in arr:
            if num == 0 and arr.count(0)>1:
                return(True)
            elif num != 0 and num not in table.keys():
                table[num]=index
                if ((2*num) in table) or ((num/2) in table):
                        return(True)
        return(False)