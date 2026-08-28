class Solution(object):
    def lexPalindromicPermutation(self, s, target):
        """
        :type s: str
        :type target: str
        :rtype: str
        """
        from collections import Counter
        
        n = len(s)
        count = Counter(s)
        odd_chars = [c for c, freq in count.iteritems() if freq % 2 != 0]
        
        if (n % 2 == 0 and len(odd_chars) != 0) or (n % 2 != 0 and len(odd_chars) != 1):
            return ""
        
        mid_char = odd_chars[0] if odd_chars else ""
        half_len = n // 2
        
        half_counts = {}
        for c, freq in count.iteritems():
            half_counts[c] = freq // 2
            
        def build_smallest(prefix, rem_counts, mid):
            res = list(prefix)
            for ch in sorted(rem_counts.keys()):
                res.extend([ch] * rem_counts[ch])
            half_str = "".join(res)
            if n % 2 != 0:
                return half_str + mid + half_str[::-1]
            return half_str + half_str[::-1]

        best = None

        def check_matching_prefix(l):
            curr_counts = dict(half_counts)
            prefix = []
            for i in xrange(l):
                ch = target[i]
                if curr_counts.get(ch, 0) <= 0:
                    return None
                curr_counts[ch] -= 1
                prefix.append(ch)

            for d in xrange(ord(target[l]) + 1, ord('z') + 1):
                ch = chr(d)
                if curr_counts.get(ch, 0) > 0:
                    next_counts = dict(curr_counts)
                    next_counts[ch] -= 1
                    cand = build_smallest(prefix + [ch], next_counts, mid_char)
                    return cand
            return None

        for l in xrange(half_len - 1, -1, -1):
            cand = check_matching_prefix(l)
            if cand is not None:
                if best is None or cand < best:
                    best = cand
                break

        curr_counts = dict(half_counts)
        exact_prefix = []
        possible = True
        for i in xrange(half_len):
            ch = target[i]
            if curr_counts.get(ch, 0) <= 0:
                possible = False
                break
            curr_counts[ch] -= 1
            exact_prefix.append(ch)

        if possible:
            if n % 2 != 0:
                mid_opts = sorted([c for c, freq in count.iteritems() if c > target[half_len]])
                for m in mid_opts:
                    rem_c = Counter(s)
                    rem_c[m] -= 1
                    h_c = {k: v // 2 for k, v in rem_c.iteritems()}
                    t_c = Counter(exact_prefix)
                    valid = True
                    for k, v in t_c.iteritems():
                        if h_c.get(k, 0) < v:
                            valid = False
                            break
                    if valid:
                        for k, v in t_c.iteritems():
                            h_c[k] -= v
                        cand = build_smallest(exact_prefix, h_c, m)
                        if best is None or cand < best:
                            best = cand
                        break

            half_str = "".join(exact_prefix)
            if n % 2 != 0:
                pal = half_str + mid_char + half_str[::-1]
            else:
                pal = half_str + half_str[::-1]
                
            if pal > target:
                if best is None or pal < best:
                    best = pal

        return best if best is not None else ""