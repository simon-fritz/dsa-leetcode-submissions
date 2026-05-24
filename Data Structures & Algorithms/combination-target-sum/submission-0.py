class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #tree = sum, largest i, trace
        res = []
        trees = [(0,0,[])]
        while trees:
            newtrees = []
            for t in trees:
                for i in range(t[1],len(nums)):
                    newt = (t[0]+nums[i],i,t[2]+[nums[i]])
                    if newt[0] == target:
                        res.append(newt[2])
                    elif newt[0] < target:
                        newtrees.append(newt)
            trees = newtrees
        return res
                
