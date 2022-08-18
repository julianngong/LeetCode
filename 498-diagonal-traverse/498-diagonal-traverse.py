class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        #important thing to note is the sum of each indicie in the same diagonal is the same
        diagonals = {}
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if i+j not in diagonals:
                    diagonals[i+j]=[mat[i][j]]
                else:
                    diagonals[i+j].append(mat[i][j])
        result=[]
        for index,key in enumerate(diagonals.keys()):
            if index%2 ==0:
                result+=diagonals[key][::-1]
            else:
                result+=diagonals[key]
        return(result)