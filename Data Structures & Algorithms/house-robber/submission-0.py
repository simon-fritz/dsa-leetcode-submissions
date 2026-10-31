class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        for i,n in enumerate(nums):
            if i == 0 or i == 1:
                dp[i] = n
                continue
            if i == 2:
                dp[i] = dp[0] + n
                continue
            dp[i] = max(dp[i-3],dp[i-2])+n
        return max(dp[-1],dp[-2]) if len(dp) > 1 else dp[-1]
            
            
            


        