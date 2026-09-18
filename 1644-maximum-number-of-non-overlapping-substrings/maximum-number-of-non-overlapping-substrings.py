class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        n = len(s)
        left = [n] * 26
        right = [-1] * 26
        
        for i, c in enumerate(s):
            idx = ord(c) - ord('a')
            left[idx] = min(left[idx], i)
            right[idx] = max(right[idx], i)
            
        intervals = []
        for i in range(26):
            if left[i] != n:
                l, r = left[i], right[i]
                valid = True
                j = l
                while j <= r:
                    c_idx = ord(s[j]) - ord('a')
                    if left[c_idx] < l:
                        valid = False
                        break
                    r = max(r, right[c_idx])
                    j += 1
                if valid:
                    intervals.append((r, l))
                    
        intervals.sort()
        res = []
        prev_r = -1
        for r, l in intervals:
            if l > prev_r:
                res.append(s[l:r+1])
                prev_r = r
                
        return res