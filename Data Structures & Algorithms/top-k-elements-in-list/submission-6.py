class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        ans = {}
        count = 1
        ans[nums[0]] = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                ans[nums[i-1]] = ans[nums[i-1]] + 1
            else:
                ans[nums[i]] = 1
        sorted_ans = sorted(ans, key=ans.get, reverse=True)
        print(sorted_ans)
        return sorted_ans[:k]