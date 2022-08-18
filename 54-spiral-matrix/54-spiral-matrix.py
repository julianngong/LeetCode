class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        counter=0
        top=0
        bottom=len(matrix)-1
        right=len(matrix[0])-1
        left=0
        i,j=0,0
        forwards=True
        result=[]
        while counter<len(matrix)*len(matrix[0]):
            counter+=1
            result.append(matrix[i][j])
            if forwards == True:
                if j<right:
                    j+=1
                elif i<bottom:
                    i+=1
                else:
                    j-=1
                    forwards=False
                    top+=1
                    right-=1
            else:
                if j>left:
                    j-=1
                elif i>top:
                    i-=1
                else:
                    j+=1
                    forwards=True
                    bottom-=1
                    left+=1
        return(result)
