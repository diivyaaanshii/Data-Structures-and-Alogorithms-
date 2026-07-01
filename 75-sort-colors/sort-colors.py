class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        count_0=0
        count_1=0
        count_2=0
        for i in range (len(nums)):
            if nums[i]==0:
                count_0+=1
            elif nums[i]==1:
                count_1+=1
            else:
                count_2+=1
        idx=0
        for j in range (len(nums)):
            while count_0>0:
                nums[idx]=0
                idx+=1
                count_0-=1
            while count_1>0:
                nums[idx]=1
                idx+=1
                count_1-=1
            while count_2>0:
                nums[idx]=2
                idx+=1
                count_2-=1
        