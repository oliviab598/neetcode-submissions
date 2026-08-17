class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        k = 2
        max_profit = 0

        for i in range(0, n):
            curr = 0
            for j in range(1, n):
                curr = prices[j] - prices[i]
                if (i < j):
                    max_profit = max(max_profit, curr)
            print('max profit: ', max_profit)
        return max_profit
