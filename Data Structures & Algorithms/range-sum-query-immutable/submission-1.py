class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = []
        total = 0
        for num in nums:
            total += num
            self.prefix.append(total)

    def sumRange(self, left: int, right: int) -> int:
        leftVal = 0 if not left else self.prefix[left-1]
        rightVal = self.prefix[right]
        diff = rightVal - leftVal
        return diff


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)