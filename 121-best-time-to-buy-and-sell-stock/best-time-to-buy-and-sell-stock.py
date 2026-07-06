class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        left=0
        max_profit=0
    
        for right in range(len(prices)):
            if prices[right] < prices[left]:
                left = right
            else:
                current_profit=prices[right]-prices[left]
                max_profit=max(max_profit,current_profit)
                
        return max_profit

                