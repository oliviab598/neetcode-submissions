class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones = count = 0

        for num in nums:
            if num == 0:
                max_ones = max(max_ones, count)
                count = 0
            else:
                count += 1

        return max(max_ones, count)

