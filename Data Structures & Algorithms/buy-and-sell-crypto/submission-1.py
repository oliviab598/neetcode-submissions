class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        max_sell = 0
        visited = set()

        for right in range(len(prices)):
            visited.add(prices[right])
            max_sell = max(prices[right]-prices[left], max_sell)

            while prices[left] > min(visited):
                left+=1

        return max(0, max_sell)