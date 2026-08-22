class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s = 0
        p = 1
        temp = n
        
        while temp > 0:
            digit = temp % 10
            s += digit
            p *= digit
            temp //= 10
            
        return n % (s + p) == 0