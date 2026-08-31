class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            max_val = -1
            curr = 0
            for j in range(i+1, len(arr)):
                curr = arr[j]
                max_val = max(curr, max_val)
            arr[i] = max_val
            print(arr)
        return arr