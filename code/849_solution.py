class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        max_dist, last, n = 0, -1, len(seats)
        for curr, seat in enumerate(seats):
            if not seat: continue
            dist = curr if last < 0 else (curr - last) / 2
            max_dist = max(max_dist, dist)
            last = curr
        max_dist = max(max_dist, n - last - 1)
        return int(max_dist)
