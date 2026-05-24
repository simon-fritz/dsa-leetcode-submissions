class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums, res):
            if not nums:
                return res
            newres = res.copy()
            for r in res:
                newres.append(r + [nums[0]]) 
            return backtrack(nums[1:], newres)
        return backtrack(nums,[[]])
    
        