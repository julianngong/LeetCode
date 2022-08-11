class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        temp1=nums1[:m]
        curr1=0
        curr2=0
        for i in range(len(nums1)):
            if curr1<m and curr2<n:
                if temp1[curr1]>nums2[curr2]:
                    nums1[i]=nums2[curr2]
                    curr2+=1
                else:
                    nums1[i]=temp1[curr1]
                    curr1+=1
            elif curr1==m:
                nums1[i]=nums2[curr2]
                curr2+=1
            else:
                nums1[i]=temp1[curr1]
                curr1+=1
        """
        Do not return anything, modify nums1 in-place instead.
        """
        