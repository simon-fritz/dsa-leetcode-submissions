class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_dict = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in diff_dict:
                return [diff_dict[diff],i]
            diff_dict[nums[i]] = i
        return []
