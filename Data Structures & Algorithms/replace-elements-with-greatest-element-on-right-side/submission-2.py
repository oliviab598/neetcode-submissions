class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = curr = -1

        for i in range(len(arr)-1, -1, -1):
            curr = arr[i]
            arr[i] = res
            res = max(res, curr)
        
        return arr