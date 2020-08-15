class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        if not n: return 0
        intervals.sort(key=lambda x: x[1])
        prev, count = 0, 0
        for curr in range(1, n):
            count += intervals[prev][1] > intervals[curr][0]
            if intervals[prev][1] <= intervals[curr][0]:  
                prev = curr
            elif intervals[prev][1] > intervals[curr][1]:  
                prev = curr
        return count
