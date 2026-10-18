class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = "".join(filter(str.isalnum, s)).lower()

        left = 0
        right = len(filtered) - 1

        while left < right:
            print('left', filtered[left])
            print('right', filtered[right])
            if filtered[left] != filtered[right]:
                return False
            left +=1
            right -=1

        return True