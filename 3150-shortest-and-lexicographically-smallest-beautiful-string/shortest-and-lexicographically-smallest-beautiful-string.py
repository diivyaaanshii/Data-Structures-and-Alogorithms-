class Solution(object):
    def shortestBeautifulSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """

        n = len(s)
        ans = ""
        
        for i in xrange(n):
            count = 0
            for j in xrange(i, n):
                if s[j] == '1':
                    count += 1
                if count == k:
                    sub = s[i:j+1]
                    if ans == "":
                        ans = sub
                    elif len(sub) < len(ans):
                        ans = sub
                    elif len(sub) == len(ans) and sub < ans:
                        ans = sub
                    break
                    
        return ans