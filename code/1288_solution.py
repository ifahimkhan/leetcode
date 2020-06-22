class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        count = 0
        max_r = 0
        for l, r in intervals:
            if max_r >= r: count += 1
            else: max_r = r
        return len(intervals) - count