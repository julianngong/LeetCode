class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        goingup = True
        if (len(arr)>=2 and arr[0]>arr[1]) or (len(arr)<=1):
            return(False)
        for i in range(len(arr)-1):
            if arr[i]==arr[i+1]:
                return False
            if goingup:
                if arr[i]>arr[i+1]:
                    goingup = False
            else:
                if arr[i]<arr[i+1] and goingup == False:
                    return False
        return(True and not(goingup))