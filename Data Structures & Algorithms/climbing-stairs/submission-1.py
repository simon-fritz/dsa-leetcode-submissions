class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {0:1,1:1,2:2}  
        def countSteps(n):
            if n in memo:
                return memo[n]
            added = countSteps(n-1) + countSteps(n-2)
            memo[n] = added
            return added

        return countSteps(n)

        