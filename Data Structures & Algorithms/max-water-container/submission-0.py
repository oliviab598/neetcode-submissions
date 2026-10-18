class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        maxArea = 0

        while left < right:
            lower = heights[left] if heights[left] < heights[right] else heights[right]
            curr = (right - left)*lower
            maxArea = max(maxArea, curr)

            if lower == heights[left]:
                left+=1
            else:
                right-=1
            
        return maxArea
