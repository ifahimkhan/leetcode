class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        n = len(heights)
        max_height = 0
        ocean_view_bulds = deque()
        for i in range(n-1, -1, -1):
            if heights[i] > max_height:
                ocean_view_bulds.appendleft(i)
                max_height = heights[i]
        return ocean_view_bulds        
