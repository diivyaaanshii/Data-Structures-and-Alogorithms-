class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        i=0
        j=len(nums)-1
        while i<=j:
            mid=(i+j)//2
            if nums[mid]==target:
                return True
            if nums[i] == nums[mid] == nums[j]:
                i += 1
                j -= 1
            elif nums[i]<=nums[mid]:
                if nums[i]<=target<nums[mid]:
                    j=mid-1
                else:
                    i=mid+1
            else:
                if nums[mid]<target<=nums[j]:
                    i=mid+1
                else:
                    j=mid-1
        return False