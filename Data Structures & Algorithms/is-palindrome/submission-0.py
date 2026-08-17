class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_new = ''.join(filter(str.isalnum, s)).lower()
        i = 0
        j = len(s_new) - 1
        while i < j:
            if s_new[i] != s_new[j]:
                return False
            i+=1
            j-=1
        return True