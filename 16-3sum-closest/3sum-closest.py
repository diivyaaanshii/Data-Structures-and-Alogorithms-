class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        nums.sort()
        closest_sum=float('inf')
        for i in range(len(nums)):
            left=i+1
            right=len(nums)-1
            while left<right:
                sum=nums[i]+nums[left]+nums[right]
                if abs(target-sum)<abs(target-closest_sum):
                    closest_sum=sum
                elif sum<target:
                    left+=1
                else:
                    right-=1
        return closest_sum
        