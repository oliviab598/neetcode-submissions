class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        min_sum = float('inf')
        curr = 0

        for right in range(len(nums)):
            curr += nums[right]
            print(curr)

            while curr >= target:
                min_sum = min(right - left + 1, min_sum)
                curr -= nums[left]
                left += 1

        return min_sum if isinstance(min_sum, int) else 0