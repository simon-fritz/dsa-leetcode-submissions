class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        p = 1
        max_sum = nums[0]
        cur_sum = nums[0]
        while p < len(nums):
            cur_sum = max(nums[p], cur_sum + nums[p])
            max_sum= max(cur_sum,max_sum)
            if cur_sum < 0:
                cur_sum = 0
            p += 1
        return max_sum
        