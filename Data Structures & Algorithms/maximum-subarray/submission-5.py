class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        curr = 0

        for num in nums:
            curr = max(curr, 0)
            curr += num
            max_sum = max(curr, max_sum)

        return max_sum