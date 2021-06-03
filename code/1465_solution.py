class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        max_height = max(horizontalCuts[0], h - horizontalCuts[~0])
        for prev, next_ in zip(horizontalCuts, horizontalCuts[1:]):
            max_height = max(max_height, next_ - prev)
        
        verticalCuts.sort()
        max_width = max(verticalCuts[0], w - verticalCuts[~0])
        for prev, next_ in zip(verticalCuts, verticalCuts[1:]):
            max_width = max(max_width, next_ - prev)
        
        max_area = (max_height * max_width) % (10**9 + 7)
        return max_area 
