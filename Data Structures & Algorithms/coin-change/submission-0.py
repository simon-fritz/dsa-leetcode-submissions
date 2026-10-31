class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        optimalChanges = [amount+1] * (amount+1)
        optimalChanges [0] = 0
        for i in range(1, amount+1):
            for c in coins: 
                if i-c >= 0:
                    optimalChanges[i] = min(optimalChanges[i], 1+optimalChanges[i-c])
        return optimalChanges[amount] if optimalChanges[amount] != amount + 1 else -1




        
        