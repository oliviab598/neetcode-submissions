class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        curr = 0

        for num in nums:
            curr = max(0, curr)
            curr += num
            maxSum = max(maxSum, curr)
        
        return maxSum