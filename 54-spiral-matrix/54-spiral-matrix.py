class Solution:
    def spiralOrder1(self, matrix: List[List[int]]) -> List[int]:
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
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        if len(matrix) == 0:
            return res
        row_begin = 0
        col_begin = 0
        row_end = len(matrix)-1 
        col_end = len(matrix[0])-1
        while (row_begin <= row_end and col_begin <= col_end):
            for i in range(col_begin,col_end+1):
                res.append(matrix[row_begin][i])
            row_begin += 1
            for i in range(row_begin,row_end+1):
                res.append(matrix[i][col_end])
            col_end -= 1
            if (row_begin <= row_end):
                for i in range(col_end,col_begin-1,-1):
                    res.append(matrix[row_end][i])
                row_end -= 1
            if (col_begin <= col_end):
                for i in range(row_end,row_begin-1,-1):
                    res.append(matrix[i][col_begin])
                col_begin += 1
        return res
