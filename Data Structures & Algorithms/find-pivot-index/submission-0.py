class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l_sum=0
        r_sum=sum(nums)
        for i,n in enumerate(nums):
            r_sum -= n
            if l_sum == r_sum:
                return i
            l_sum += n
        return -1