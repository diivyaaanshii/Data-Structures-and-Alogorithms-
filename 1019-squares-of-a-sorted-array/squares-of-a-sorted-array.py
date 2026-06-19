class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #Optimised solution
        a=[]
        b=[]
        for num in nums:
            if num < 0:
                a.append(abs(num))
                
            else:
                b.append(num)
        a.reverse()      
        n=len(a)
        m=len(b)
        i=0
        j=0
        idx=0
        res=[0]*len(nums)
        while (i<n and j<m):
            if a[i]<=b[j]:
                res[idx]=a[i]
                idx+=1
                i+=1
            else:
                res[idx]=b[j]
                idx+=1
                j+=1
        while j <m:
            res[idx]=b[j]
            idx+=1
            j+=1
        while i< n:
            res[idx]=a[i]
            idx+=1
            i+=1
        for k in range (len(res)):
            res[k]=res[k]*res[k]
        return res



