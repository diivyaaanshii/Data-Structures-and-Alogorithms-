class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        suf_min = [0] * n
        suf_min[-1] = nums[-1]
        for i in xrange(n - 2, -1, -1):
            suf_min[i] = min(nums[i], suf_min[i + 1])
            
        cur_max = nums[0]
        for i in xrange(n):
            cur_max = max(cur_max, nums[i])
            if cur_max - suf_min[i] <= k:
                return i
                
        return -1