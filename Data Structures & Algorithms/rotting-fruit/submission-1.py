from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        fruits = set()
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fruits.add((r,c))
                if grid[r][c] == 2:
                    q.append((r,c,0))

        if not fruits:
            return 0

        while q:
            r,c,i = q.popleft()
            for dr,dc in directions:
                nr = r + dr
                nc = c + dc
                if (nr,nc) in fruits:
                    fruits.remove((nr,nc))
                    if not fruits:
                        return i+1
                    q.append((nr,nc,i+1))
        return -1




