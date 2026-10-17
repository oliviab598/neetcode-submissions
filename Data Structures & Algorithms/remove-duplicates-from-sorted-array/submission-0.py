class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left=0
        right=0

        while right < len(nums)-1:
            right+=1
            if nums[right] != nums[right-1]:
                left+=1
                nums[left] = nums[right]
        return left+1
