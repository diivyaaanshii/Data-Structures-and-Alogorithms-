class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        count=Counter(nums)
        for c in count:
            if count[c]==1:
                return c