class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones = -1
        curr = 0

        if nums[0] == 1:
            curr += 1

        for i in range(1, len(nums)):
            print("curr: ", curr)
            print("max ones: ", max_ones)
            if nums[i] == nums[i-1] and nums[i] == 1:
                print('entered')
                curr += 1
            else:
                curr = nums[i]
            max_ones = max(max_ones, curr)
        
        print("curr: ", curr)
        print("max ones: ", max_ones)
        return max(max_ones, curr)

