class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result=[]
        for i in range(numRows):
            if i==0:
                result.append([1])
            elif i==1:
                result.append([1,1])
            else:
                temp=[1]
                for j in range(0,len(result[i-1])-1):
                    temp.append(result[i-1][j]+result[i-1][j+1])
                temp.append(1)
                result.append(temp)
        return(result)
                    
            