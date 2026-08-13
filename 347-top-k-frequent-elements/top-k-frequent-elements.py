import heapq

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        cnt={}
        for num in nums:
            if num in cnt:
                cnt[num]+=1
            else:
                cnt[num]=1
        min_heap=[]
        for num,freq in cnt.iteritems():
            heapq.heappush(min_heap,(freq,num))
            if len(min_heap)>k:
                heapq.heappop(min_heap)
        return [num for fre,num in min_heap]
