class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        dupearr = arr.copy()
        num0=0
        i=0
        while i+num0<=len(dupearr)-1:
            arr[i+num0]=dupearr[i]
            if dupearr[i]==0 and i+num0+1<=len(dupearr)-1 :
                arr[i+num0+1]=dupearr[i]
                num0+=1
            i+=1
                
        """
        Do not return anything, modify arr in-place instead.
        """
        