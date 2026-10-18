class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = []
        total = 0
        for num in nums:
            total+=num
            prefix.append(total)
        n = len(prefix)

        for p in range(len(prefix)):
            left = prefix[p-1] if p > 0 else 0
            right = prefix[n-1] - prefix[p]
            if left == right:
                return p

        return -1