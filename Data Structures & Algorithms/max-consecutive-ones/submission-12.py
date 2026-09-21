class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones = curr = 0

        for num in nums:
            if num == 0:
                curr = 0
            else:
                curr += 1
                max_ones = max(curr, max_ones)
        return max_ones


