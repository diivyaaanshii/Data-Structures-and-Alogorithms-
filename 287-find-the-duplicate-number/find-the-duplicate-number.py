class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq_map={}
        for i in range (len(nums)):
            if nums[i] in freq_map:
                return nums[i]
            freq_map[nums[i]]=1