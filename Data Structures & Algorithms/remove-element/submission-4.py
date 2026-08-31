class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        temp = []
        for num in nums:
            if num == val:
                continue
            temp.append(num)
        print(temp)
        for i in range(len(temp)):
            nums[i] = temp[i]
        return len(temp)