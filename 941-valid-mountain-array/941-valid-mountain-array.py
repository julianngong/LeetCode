class Solution:
    def validMountainArray1(self, arr: List[int]) -> bool:
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
    def validMountainArray(self, A):
        N = len(A)
        i = 0

        # walk up
        while i+1 < N and A[i] < A[i+1]:
            i += 1

        # peak can't be first or last
        if i == 0 or i == N-1:
            return False

        # walk down
        while i+1 < N and A[i] > A[i+1]:
            i += 1

        return i == N-1