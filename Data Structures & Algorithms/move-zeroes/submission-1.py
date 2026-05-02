class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p1 = 0
        p2 = 0
        while p2 < len(nums) and p1 < len(nums):
            while nums[p2] == 0:
                p2 += 1
                if p2 == len(nums):
                    return
            if nums[p1] == 0:
                nums[p1],nums[p2] = nums[p2],nums[p1]
            p1 += 1
            p2 += 1