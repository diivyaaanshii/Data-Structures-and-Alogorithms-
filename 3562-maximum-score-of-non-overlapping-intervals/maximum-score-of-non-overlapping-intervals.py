import bisect
import math
import functools

class T:
    def __init__(self, weight: int, selected: tuple[int, ...]):
        self.weight = weight
        self.selected = selected
    def __lt__(self, other: 'T') -> bool:
        if self.weight != other.weight:
            return self.weight < other.weight
        return self.selected > other.selected

class Solution:
    def maximumWeight(self, intervals: list[list[int]]) -> list[int]:
        intervals = sorted((*interval, i) for i, interval in enumerate(intervals))
        
        @functools.lru_cache(None)
        def dp(i: int, quota: int) -> T:
            if i == len(intervals) or quota == 0:
                return T(0, ())
            skip = dp(i + 1, quota)
            _, r, weight, originalIndex = intervals[i]
            j = bisect.bisect_right(intervals, (r, math.inf))
            nextRes = dp(j, quota - 1)
            pick = T(weight + nextRes.weight, tuple(sorted((originalIndex, *nextRes.selected))))
            return max(skip, pick)
            
        return list(dp(0, 4).selected)