class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = len(nums) - 1
        sort_nums = sorted(nums)

        while i < j:
            curr = sort_nums[i] + sort_nums[j]
            print('curr:', curr)
            if curr == target:
                first = nums.index(sort_nums[i])
                if sort_nums[i] == sort_nums[j]:
                    second = nums.index(sort_nums[j], first+1)
                else:
                    second = nums.index(sort_nums[j])
                return sorted([first, second])
            elif curr < target:
                i+=1
            else:
                j-=1

        return []