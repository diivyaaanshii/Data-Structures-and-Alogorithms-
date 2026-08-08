class Solution(object):
    def validSequence(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: List[int]
        """
        n, m = len(word1), len(word2)
        
        # last[j] stores the maximum index in word1 that can cover suffix word2[j:]
        last = [-1] * (m + 1)
        last[m] = n
        
        j = m - 1
        for i in range(n - 1, -1, -1):
            if j >= 0 and word1[i] == word2[j]:
                last[j] = i
                j -= 1
                
        ans = []
        j = 0
        changed = False
        
        for i in range(n):
            if j == m:
                break
                
      
            if word1[i] == word2[j]:
                ans.append(i)
                j += 1

            elif not changed and last[j + 1] > i:
                ans.append(i)
                j += 1
                changed = True
                
        return ans if len(ans) == m else []