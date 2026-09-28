class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        d = dict(knowledge)
        res, i, n = [], 0, len(s)
        while i < n:
            if s[i] == '(':
                j = s.find(')', i)
                res.append(d.get(s[i+1:j], '?'))
                i = j
            else:
                res.append(s[i])
            i += 1
        return "".join(res)