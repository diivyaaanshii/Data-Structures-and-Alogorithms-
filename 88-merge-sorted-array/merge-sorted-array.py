class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        nums1_copy = nums1[:m]
        i=0
        j=0
        idx=0
        while(i<m and j<n):
            if nums1_copy[i]<=nums2[j]:
                nums1[idx]=nums1_copy[i]
                idx+=1
                i+=1
            else:
                nums1[idx]=nums2[j]
                idx+=1
                j+=1
        while i<m:
            nums1[idx]=nums1_copy[i]
            idx+=1
            i+=1
        while j<n:
            nums1[idx]=nums2[j]
            idx+=1
            j+=1

        