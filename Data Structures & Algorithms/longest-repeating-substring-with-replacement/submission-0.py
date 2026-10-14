class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left=0
        visited={}
        long_s=0

        for right in range(len(s)):
            if s[right] in visited:
                visited[s[right]] = visited[s[right]] + 1
            else:
                visited[s[right]] = 1

            window=right-left+1
            remaining=window-max(visited.values())

            if remaining>k:
                visited[s[left]] = visited[s[left]] - 1
                left+=1
                remaining-=1
            else:
                long_s=max(window, long_s)
        
        return long_s
                

            