class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        
        for i in range(n):
            dp[i + 1] = dp[i]
            
            for j in (i - k + 1, i - k):
                if j >= 0 and s[j:i + 1] == s[j:i + 1][::-1]:
                    dp[i + 1] = max(dp[i + 1], dp[j] + 1)
                    break
            else:
                for j in range(i - k - 1, -1, -1):
                    if s[j:i + 1] == s[j:i + 1][::-1]:
                        dp[i + 1] = max(dp[i + 1], dp[j] + 1)
                        break
                        
        return dp[n]