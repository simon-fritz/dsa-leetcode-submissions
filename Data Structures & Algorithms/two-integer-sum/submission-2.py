class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_map = {}
        for i,n in enumerate(nums):
            diff_map[target-n] = i
        for i,n in enumerate(nums):
            if n in diff_map and i != diff_map[n]:
                return [i,diff_map[n]]
        return []
