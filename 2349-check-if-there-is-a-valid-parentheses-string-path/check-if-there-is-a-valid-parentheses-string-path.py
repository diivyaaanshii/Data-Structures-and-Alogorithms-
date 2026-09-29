class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        if (m + n) % 2 == 0 or grid[0][0] == ')' or grid[m - 1][n - 1] == '(':
            return False
        
        dp = [[set() for _ in range(n)] for _ in range(m)]
        dp[0][0].add(1 if grid[0][0] == '(' else -1)
        
        for r in range(m):
            for c in range(n):
                if not dp[r][c]:
                    continue
                curr_set = dp[r][c]
                for nr, nc in ((r + 1, c), (r, c + 1)):
                    if nr < m and nc < n:
                        val = 1 if grid[nr][nc] == '(' else -1
                        for b in curr_set:
                            nb = b + val
                            if nb >= 0:
                                dp[nr][nc].add(nb)
        
        return 0 in dp[m - 1][n - 1]