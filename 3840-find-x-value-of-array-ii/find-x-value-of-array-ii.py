class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        nums = [x % k for x in nums]
        queries = [[i, v % k, s, x] for i, v, s, x in queries]
        n = len(nums)
        
        tree_prod = [1] * (4 * n)
        tree_remain = [[0] * k for _ in range(4 * n)]
        
        def merge(l_prod, l_rem, r_prod, r_rem):
            prod = (l_prod * r_prod) % k
            rem = list(l_rem)
            for i in range(k):
                rem[(i * l_prod) % k] += r_rem[i]
            return prod, rem

        def build(node, left, right):
            if left == right:
                tree_prod[node] = nums[left]
                tree_remain[node][nums[left]] = 1
                return
            mid = (left + right) // 2
            build(2 * node, left, mid)
            build(2 * node + 1, mid + 1, right)
            p_l, r_l = tree_prod[2 * node], tree_remain[2 * node]
            p_r, r_r = tree_prod[2 * node + 1], tree_remain[2 * node + 1]
            tree_prod[node], tree_remain[node] = merge(p_l, r_l, p_r, r_r)

        build(1, 0, n - 1)

        def update(node, left, right, idx, val):
            if left == right:
                tree_prod[node] = val
                tree_remain[node] = [0] * k
                tree_remain[node][val] = 1
                return
            mid = (left + right) // 2
            if idx <= mid:
                update(2 * node, left, mid, idx, val)
            else:
                update(2 * node + 1, mid + 1, right, idx, val)
            p_l, r_l = tree_prod[2 * node], tree_remain[2 * node]
            p_r, r_r = tree_prod[2 * node + 1], tree_remain[2 * node + 1]
            tree_prod[node], tree_remain[node] = merge(p_l, r_l, p_r, r_r)

        def query(node, left, right, q_l, q_r):
            if q_l <= left and right <= q_r:
                return tree_prod[node], tree_remain[node]
            if q_r < left or right < q_l:
                return 1, [0] * k
            mid = (left + right) // 2
            p_l, r_l = query(2 * node, left, mid, q_l, q_r)
            p_r, r_r = query(2 * node + 1, mid + 1, right, q_l, q_r)
            return merge(p_l, r_l, p_r, r_r)

        ans = []
        for idx, val, start, x in queries:
            update(1, 0, n - 1, idx, val)
            _, rem = query(1, 0, n - 1, start, n - 1)
            ans.append(rem[x])
        return ans