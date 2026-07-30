class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Median of Two Sorted Arrays first we hv to to merge the arrays then we have to find the median for the mergeredsorted array

        """

        i=0
        j=len(nums)-1
        while i<j:
            mid =(i+j)//2
            if nums[mid]>nums[j]:
                i=mid+1
            else:
                j=mid
        return nums[i]