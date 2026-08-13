class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res = 0
        visited = set()

        edgemap = {i: set() for i in range(n)}
        for e in edges:
            edgemap[e[0]].add(e[1])
            edgemap[e[1]].add(e[0])

        def dfs(k,new):
            nonlocal res
            if k in visited:
                return
            visited.add(k)
            if new:
                res+=1
            for n in edgemap[k]:
                dfs(n,False)

        for i in range(n):
            dfs(i,True)
        
        return res
        