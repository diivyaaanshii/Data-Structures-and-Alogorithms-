class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        i=1
        j=max(piles)
        while i<j:
            m=(i+j)//2
            h_n=sum((p+m-1)//m for p in piles)
            if h_n<=h:
                j=m
            else:
                i=m+1
        return i