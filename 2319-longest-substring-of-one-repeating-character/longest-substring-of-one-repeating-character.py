class SegmentTree:

  def __init__(self, s):
    self.n = len(s)
    self.tree_max = [0] * (4 * self.n)
    self.tree_pref = [0] * (4 * self.n)
    self.tree_suff = [0] * (4 * self.n)
    self.s = list(s)
    self._build(1, 0, self.n - 1)

  def _merge(self, node, l_idx, mid, r_idx):
    left_child = 2 * node
    right_child = 2 * node + 1

    left_len = mid - l_idx + 1
    right_len = r_idx - mid

    self.tree_max[node] = max(
        self.tree_max[left_child], self.tree_max[right_child]
    )
    self.tree_pref[node] = self.tree_pref[left_child]
    self.tree_suff[node] = self.tree_suff[right_child]

    if self.s[mid] == self.s[mid + 1]:
      combined_mid = self.tree_suff[left_child] + self.tree_pref[right_child]
      self.tree_max[node] = max(self.tree_max[node], combined_mid)

      if self.tree_pref[left_child] == left_len:
        self.tree_pref[node] = left_len + self.tree_pref[right_child]

      if self.tree_suff[right_child] == right_len:
        self.tree_suff[node] = self.tree_suff[left_child] + right_len

  def _build(self, node, l_idx, r_idx):
    if l_idx == r_idx:
      self.tree_max[node] = 1
      self.tree_pref[node] = 1
      self.tree_suff[node] = 1
      return

    mid = (l_idx + r_idx) // 2
    self._build(2 * node, l_idx, mid)
    self._build(2 * node + 1, mid + 1, r_idx)
    self._merge(node, l_idx, mid, r_idx)

  def update(self, node, l_idx, r_idx, pos, ch):
    if l_idx == r_idx:
      self.s[pos] = ch
      return

    mid = (l_idx + r_idx) // 2
    if pos <= mid:
      self.update(2 * node, l_idx, mid, pos, ch)
    else:
      self.update(2 * node + 1, mid + 1, r_idx, pos, ch)

    self._merge(node, l_idx, mid, r_idx)


class Solution(object):

  def longestRepeating(self, s, queryCharacters, queryIndices):
    st = SegmentTree(s)
    ans = []

    for i in xrange(len(queryIndices)):
      idx = queryIndices[i]
      ch = queryCharacters[i]
      st.update(1, 0, len(s) - 1, idx, ch)
      ans.append(st.tree_max[1])

    return ans