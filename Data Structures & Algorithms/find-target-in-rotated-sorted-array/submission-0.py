class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0 
        right = len(nums) - 1

        while left <= right:
            leftVal = nums[left]
            rightVal = nums[right]
            mid = (right - left)//2 + left
            midVal = nums[mid]

            if target == midVal:
                return mid

            if leftVal <= midVal:
                if leftVal <= target < midVal:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if midVal < target <= rightVal:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1