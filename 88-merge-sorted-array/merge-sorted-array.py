class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        num1copy=nums1[:m]
        l=0
        r=0
        idx=0
        while l<m and r<n:
            if num1copy[l]<nums2[r]:
                nums1[idx]=num1copy[l]
                idx+=1
                l+=1
            else:
                nums1[idx]=nums2[r]
                idx+=1
                r+=1
        while l<m:
           
            nums1[idx]=num1copy[l]
            idx+=1
            l+=1
        while r<n:
            nums1[idx]=nums2[r]
            idx+=1
            r+=1
        