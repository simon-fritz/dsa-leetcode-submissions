class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        land_set = set()
        counter = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    if (row, col) in land_set:
                        continue
                    else: #initiate dfs
                        counter += 1
                        stack = [(row,col)]
                        while stack:
                            cur = stack.pop()
                            if cur in land_set or grid[cur[0]][cur[1]] == "0":
                                continue
                            else:
                                land_set.add(cur)
                                if cur[0] > 0:
                                    stack.append((cur[0]-1,cur[1]))
                                if cur[0] < len(grid)-1:
                                    stack.append((cur[0]+1,cur[1]))
                                if cur[1] > 0:
                                    stack.append((cur[0],cur[1]-1))
                                if cur[1] < len(grid[0])-1:
                                    stack.append((cur[0],cur[1]+1))
        return counter
                                

        