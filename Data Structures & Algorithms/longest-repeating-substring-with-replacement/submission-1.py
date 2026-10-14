class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left=0
        visited={}
        long_s=0

        for right in range(len(s)):
            visited[s[right]] = 1 + visited.get(s[right], 0)

            while (right-left+1)-max(visited.values())>k:
                visited[s[left]] -= 1
                left+=1
            long_s=max(right-left+1, long_s)
        
        return long_s
                

            