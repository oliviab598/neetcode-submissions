class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        left = 0
        max_window = 0
        curr = 0
        prev = -1

        for right in range(len(arr)-1):
            curr = 0 if arr[right] < arr[right+1] else 1

            if arr[right] == arr[right+1]:
                left = right + 1

            elif prev == curr:
                left = right

            elif prev != curr:
                max_window =  max(right - left + 2, max_window)
            
            prev = curr

        return max(max_window, 1)