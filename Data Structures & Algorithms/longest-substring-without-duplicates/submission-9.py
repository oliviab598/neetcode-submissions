class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left = right = 0
        max_s = 0
        hash_s = set()

        while right < len(s):

            while s[right] in hash_s:
                hash_s.remove(s[left])
                left+=1

            hash_s.add(s[right])
            right += 1

            max_s = max(len(hash_s), max_s)

            # updates

            # updates

        return max_s
