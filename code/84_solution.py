class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack = [-1]
        max_area = 0
        
        for i, height in enumerate(heights):
            while height < heights[stack[~0]]:
                h = heights[stack.pop()]
                w = i - stack[~0] - 1
                max_area = max(max_area, h * w)
            stack.append(i)
        
        heights.pop()
        return max_area
