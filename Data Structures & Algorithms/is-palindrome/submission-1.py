class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = "".join(filter(str.isalnum, s)).lower()

        left, right = 0, len(filtered) - 1

        while left < right:
            if filtered[right] != filtered[left]:
                return False
            left += 1
            right -= 1

        return True
