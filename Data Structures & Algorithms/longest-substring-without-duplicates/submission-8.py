class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        left = right = 0
        max_s = count = 0
        hash_set = set()
        
        while right < len(s):
            while left < right and s[right] in hash_set:
                hash_set.remove(s[left])
                left+=1
            hash_set.add(s[right])
            right+=1

            max_s = max(len(hash_set), max_s)

        return max_s
