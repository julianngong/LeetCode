class Solution:
    def getRow1(self, rowIndex: int) -> List[int]:
        if rowIndex==0:
            return[1]
        elif rowIndex==1:
            return[1,1]
        else:
            result=[1,1]
            for i in range(2,rowIndex+1):
                temp=result
                result=[1]
                for j in range(i-1):
                    result=result + [temp[j]+temp[j+1]]
                result=result +[1]
            return(result)
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        for i in range(rowIndex):
            for j in range(i, 0, -1):
                row[j] = row[j] + row[j-1]
            row.append(1)
        return row          
                