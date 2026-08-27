class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        row=len(grid)
        col=len(grid[0])
        p=0
        for r in xrange(row):
            for c in range(col):
                if grid[r][c]==1:
                    p+=4
                    if r>0 and grid[r-1][c]==1:
                        p-=2
                    if c>0 and grid[r][c-1]==1:
                        p-=2
        return p