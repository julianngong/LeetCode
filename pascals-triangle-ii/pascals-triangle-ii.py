class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
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
                    
                
                