class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        max_val = -1
        for i in range(n - 1, -1, -1):
            curr = arr[i]
            arr[i] = max_val
            max_val = max(curr, max_val)
        return arr