class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        max_sum = -1
        nums.sort()
        low = 0
        high = len(nums)-1
        while low < high:
            #if candidate
            two_sum = nums[low]+ nums[high]
            if two_sum < k:
                max_sum = max(max_sum,two_sum)
                low += 1
            else:
                high -= 1
        return max_sum



        