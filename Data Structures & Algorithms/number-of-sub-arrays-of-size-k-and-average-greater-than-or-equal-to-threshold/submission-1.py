class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        avg = 0
        ans = 0

        for i in range(k):
            avg += arr[i]

        left = 0

        if avg//k >= threshold:
                ans += 1

        for right in range(k, len(arr)):     
            avg -= arr[left]
            avg += arr[right]
            left += 1

            if avg//k >= threshold:
                ans += 1

        return ans