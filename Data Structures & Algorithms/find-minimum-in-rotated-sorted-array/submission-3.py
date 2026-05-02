class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        while l<r:
            s = (l+r)//2
            if nums[s] < nums[r]:
                r = s
            else:
                l = s+1
        return nums[l]