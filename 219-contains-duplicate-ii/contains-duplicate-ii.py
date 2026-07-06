class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        window=set()
        left=0
        for right in range(len(nums)):
            if right-left>k:
                window.remove(nums[left])
                left+=1
            if nums[right] in window:
                return True
            window.add(nums[right])
        return False        