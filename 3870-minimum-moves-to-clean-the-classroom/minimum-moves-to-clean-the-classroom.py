from collections import deque
class Solution(object):
    def minMoves(self, classroom, energy):
        """
        :type classroom: List[str]
        :type energy: int
        :rtype: int
        """
        m, n = len(classroom), len(classroom[0])
        start = None
        litter = []
        
        for r in xrange(m):
            for c in xrange(n):
                ch = classroom[r][c]
                if ch == 'S':
                    start = (r, c)
                elif ch == 'L':
                    litter.append((r, c))
                    
        k = len(litter)
        if k == 0:
            return 0
            
        target_mask = (1 << k) - 1
        litter_map = {pos: i for i, pos in enumerate(litter)}
        
        best_energy = [[[-1] * n for _ in xrange(m)] for _ in xrange(1 << k)]
        
        queue = deque([(start[0], start[1], 0, energy, 0)])
        best_energy[0][start[0]][start[1]] = energy
        
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while queue:
            r, c, mask, curr_energy, moves = queue.popleft()
            
            if mask == target_mask:
                return moves
                
            if curr_energy == 0:
                continue
                
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    cell = classroom[nr][nc]
                    if cell == 'X':
                        continue
                        
                    nmask = mask
                    nenergy = energy if cell == 'R' else curr_energy - 1
                    
                    if cell == 'L' and (nr, nc) in litter_map:
                        nmask |= (1 << litter_map[(nr, nc)])
                        
                    if nenergy > best_energy[nmask][nr][nc]:
                        best_energy[nmask][nr][nc] = nenergy
                        queue.append((nr, nc, nmask, nenergy, moves + 1))
                        
        return -1