from collections import defaultdict


class Solution(object):

  def maxNumberOfFamilies(self, n, reservedSeats):
    reserved = defaultdict(set)
    for r, c in reservedSeats:
      if 2 <= c <= 9:
        reserved[r].add(c)

    ans = 2 * n

    for r in reserved:
      left = not any(c in reserved[r] for c in (2, 3, 4, 5))
      right = not any(c in reserved[r] for c in (6, 7, 8, 9))
      middle = not any(c in reserved[r] for c in (4, 5, 6, 7))

      if left and right:
        continue
      elif left or right or middle:
        ans -= 1
      else:
        ans -= 2

    return ans