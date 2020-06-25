class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        MOD = 10 ** 9 +7
        INT_MIN = - 2 ** 32
        
        # convert list of rectangles to events
        events = [] # tuple of x, type, y1, y2
        for x1, y1, x2, y2 in rectangles:
            events.append([x1, 0, y1, y2])
            events.append([x2, 1, y1, y2])
        events.sort(key=lambda x: (x[0], -x[1]))
        
        # helper function to do total interval length via sweep line
        
        def gain_area(m):
            area = 0
            prev = INT_MIN
            for l, r in open_intervals:
                prev = max(prev, l)
                area += max(0, (r - prev) * m)
                prev = max(r, prev)
            return area
        
        # sweep line to realize area
        # O(N^2logN)
        area = 0
        prev = INT_MIN
        open_intervals = []
        for event in events: # O(N)
            curr, close, y1, y2 = event
            area += gain_area(curr - prev)
            if close:
                open_intervals.remove((y1,y2))
            else:
                open_intervals.append((y1,y2))
                open_intervals.sort()  #O(NlogN)
            prev = curr
        return area % MOD
