class Solution(object):
    def maxSubarrayLength(self, nums, k):
        freq = {}
        left = 0
        max_len = 0
        
        for right in xrange(len(nums)):
            num = nums[right]
            freq[num] = freq.get(num, 0) + 1
            
            while freq[num] > k:
                freq[nums[left]] -= 1
                left += 1
                
            max_len = max(max_len, right - left + 1)
            
        return max_len