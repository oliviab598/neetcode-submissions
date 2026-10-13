class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        curr = 0
        min_len = float('inf')

        for right in range(len(nums)):
            curr += nums[right]

            while curr >= target:
                min_len = min(right-left+1, min_len)
                curr-=nums[left]
                left+=1
        
        return min_len if type(min_len) is int else 0
