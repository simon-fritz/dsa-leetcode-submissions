class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:

        dirs = [(0,1),(0,-1),(1,0),(-1,0)]

        def isValidTile(r,c):
            if r >= 0 and r < len(grid) and c >= 0 and c < len(grid):
                return True
            return False

        visit = set()

        def dfs(r,c):
            if isValidTile(r,c) and grid[r][c] and (r,c) not in visit:
                visit.add((r,c))
                for dr,dc in dirs:
                    dfs(r+dr,c+dc)

        
        def bfs():
            res = 0
            queue = deque(visit)
            while queue:
                for _ in range(len(queue)):
                    r,c = queue.popleft()
                    for dr,dc in dirs:
                        cur_r, cur_c = r+dr, c+dc
                        if not isValidTile(cur_r,cur_c) or (cur_r,cur_c) in visit:
                            continue
                        if grid[cur_r][cur_c]:
                            return res
                        queue.append((cur_r,cur_c))
                        visit.add((cur_r,cur_c))
                res += 1
            
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j]:
                    dfs(i,j)
                    return bfs()

        