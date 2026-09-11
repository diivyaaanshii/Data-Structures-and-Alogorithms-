class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        nums = set()
        for i, a in enumerate(digits):
            if a % 2 != 0:
                continue
            for j, b in enumerate(digits):
                if j == i:
                    continue
                for k, c in enumerate(digits):
                    if k == i or k == j:
                        continue
                    if c == 0:
                        continue
                    nums.add(c * 100 + b * 10 + a)
        return len(nums)