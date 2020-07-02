class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        distance = lambda x, y: max(abs(y[0] - x[0]), abs(y[1] - x[1]))
        total = 0
        for p1, p2 in zip(points, points[1:]):
            total += distance(p1, p2)
        return total
