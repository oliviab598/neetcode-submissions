class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = curr_max = curr_min = nums[0]

        for x in range(1, len(nums)):
            temp_max = max(nums[x], nums[x] * curr_max, nums[x] * curr_min)
            curr_min = min(nums[x], nums[x] * curr_max, nums[x] * curr_min)
            curr_max = temp_max
            res = max(res, curr_max)
        
        return res



