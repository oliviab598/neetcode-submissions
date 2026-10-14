class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        visited = set()
        max_diff = 0
        
        for right in range(len(prices)):
            visited.add(prices[right])
            max_diff = max(prices[right]-min(visited), max_diff)

            while prices[left] > min(visited):
                left+=1

        return max_diff

