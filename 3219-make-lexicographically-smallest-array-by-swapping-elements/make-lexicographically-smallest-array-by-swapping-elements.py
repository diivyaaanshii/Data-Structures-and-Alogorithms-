class Solution(object):
    def lexicographicallySmallestArray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: List[int]
        """
        n = len(nums)
        pairs = sorted([(nums[i], i) for i in xrange(n)])
        
        result = [0] * n
        i = 0
        while i < n:
            j = i + 1
            while j < n and pairs[j][0] - pairs[j - 1][0] <= limit:
                j += 1
            
            indices = sorted([pairs[k][1] for k in xrange(i, j)])
            for idx, k in enumerate(xrange(i, j)):
                result[indices[idx]] = pairs[k][0]
            
            i = j
            
        return result