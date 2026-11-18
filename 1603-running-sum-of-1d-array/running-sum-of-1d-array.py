class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        x=0
        y=1
        for i in range (1,len(nums)):
            nums[i]=nums[x]+nums[y]
            x+=1
            y+=1
        return nums
            
