class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        for x in range (len(nums)):
            nums[x]=nums[x]*nums[x]
        nums.sort()
        return nums