class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones = -1
        curr = 0

        for i in range(0, len(nums)):
            if nums[i] == 1:
                curr += 1
                max_ones = max(max_ones, curr)
            else:
                curr = 0
        return max(max_ones, 0)