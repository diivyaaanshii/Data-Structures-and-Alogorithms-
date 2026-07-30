class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
      
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
