class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        arr_0=[]
        arr_1=[]
        arr_2=[]
        arr=[]

        for i in range(len(nums)):
            if nums[i]==0:
                arr_0.append(nums[i])
            elif nums[i]==1:
                arr_1.append(nums[i])
            else:
                arr_2.append(nums[i])
        arr=arr_0+arr_1+arr_2
        for j in range (len(nums)):
            nums[j]=arr[j]