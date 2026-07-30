class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m=len(nums1)
        n=len(nums2)
        res=[0]*(m+n)
        idx=0
        i=0
        j=0
        while i<m and j<n:
            if nums1[i]<=nums2[j]:
                res[idx]=nums1[i]
                idx+=1
                i+=1
            else:
                res[idx]=nums2[j]
                idx+=1
                j+=1
        while i<m:
            res[idx]=nums1[i]
            idx+=1
            i+=1
        while j<n:
            res[idx]=nums2[j]
            idx+=1
            j+=1
        num_len=len(res)
        mid=num_len//2
        if num_len%2!=0:
            return float(res[mid])
        else:
            return (res[mid-1]+res[mid])/2.0
