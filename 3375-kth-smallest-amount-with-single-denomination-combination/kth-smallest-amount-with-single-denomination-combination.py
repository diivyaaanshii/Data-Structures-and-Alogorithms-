import itertools
from fractions import gcd

class Solution(object):
    def findKthSmallest(self, coins, k):
        def lcm(a, b):
            return (a * b) // gcd(a, b)
        
        n = len(coins)
        subsets = []
        for size in xrange(1, n + 1):
            sign = 1 if size % 2 == 1 else -1
            for comb in itertools.combinations(coins, size):
                cur_lcm = comb[0]
                for coin in comb[1:]:
                    cur_lcm = lcm(cur_lcm, coin)
                subsets.append((cur_lcm, sign))
        
        def count_multiples(m):
            cnt = 0
            for cur_lcm, sign in subsets:
                cnt += sign * (m // cur_lcm)
            return cnt
        
        low = 1
        high = min(coins) * k
        ans = high
        
        while low <= high:
            mid = low + (high - low) // 2
            if count_multiples(mid) >= k:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
                
        return ans