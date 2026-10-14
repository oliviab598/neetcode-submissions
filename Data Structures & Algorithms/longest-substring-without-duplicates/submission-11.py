class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left=0
        longest=0
        visited = set()
        count=0

        for right in range(len(s)):
            while left < right and s[right] in visited:
                visited.remove(s[left])
                left+=1
                count-=1
            
            visited.add(s[right])
            count+=1
            longest = max(longest, count)

        return longest

