class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_buy_price = prices[0]
        max_profit = 0
        for p in prices:
            max_profit = max(p-best_buy_price,max_profit)
            best_buy_price = min(p,best_buy_price)
        return max_profit