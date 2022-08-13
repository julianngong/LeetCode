from collections import defaultdict
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        table = defaultdict()
        zeroseen = False
        for num in arr:
            if num == 0 and arr.count(0)>1:
                return(True)
            if num not in table.keys():
                table[num]=index
                print(table)
                print(zeroseen)
                if ((2*num) in table) or ((num/2) in table):
                    if num == 0:
                        if zeroseen==True:
                            return(True)
                        else:
                            zeroseen=True
                    else:
                        return(True)
        return(False)