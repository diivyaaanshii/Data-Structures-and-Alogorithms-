from collections import Counter

class Solution(object):
    def lexGreaterPermutation(self, s, target):
        n = len(s)
        if n != len(target):
            return ""
        
        total_counts = Counter(s)
        matched_prefix_len = 0
        cur_counts = Counter()
        
        for i in xrange(n):
            ch = target[i]
            cur_counts[ch] += 1
            if cur_counts[ch] <= total_counts[ch]:
                matched_prefix_len += 1
            else:
                break
        
        for i in xrange(matched_prefix_len, -1, -1):
            rem = Counter(total_counts)
            for j in xrange(i):
                rem[target[j]] -= 1
            
            if i < n:
                for char_code in xrange(ord(target[i]) + 1, 128):
                    c = chr(char_code)
                    if rem.get(c, 0) > 0:
                        rem[c] -= 1
                        tail = []
                        for code in xrange(128):
                            ch = chr(code)
                            if rem.get(ch, 0) > 0:
                                tail.append(ch * rem[ch])
                        return target[:i] + c + "".join(tail)
        
        return ""