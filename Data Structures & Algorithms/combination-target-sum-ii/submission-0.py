class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        tree = [(0,-1,[])] #count, highest i, 
        res = []
        while tree:
            newtree = []
            for e in tree:
                for i in range(e[1]+1,len(candidates)):
                    if i > e[1] + 1 and candidates[i] == candidates[i-1]: continue
                    new = (e[0]+candidates[i],i,e[2] + [candidates[i]])
                    if new[0] > target:
                        continue
                    if new[0] == target:
                        res.append(new[2])
                        continue
                    newtree.append(new)
            tree = newtree
        return res
