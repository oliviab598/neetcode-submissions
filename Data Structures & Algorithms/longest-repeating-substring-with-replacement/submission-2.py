class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        visited = {}
        max_sub = 0

        for right in range(len(s)):
            visited[s[right]] = 1 + visited.get(s[right], 0)

            if (right - left + 1) - max(visited.values()) > k:
                visited[s[left]] = visited.get(s[left]) - 1
                left += 1

            max_sub = max(right - left + 1, max_sub)

        return max_sub
                

            