class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        nrow, ncol = len(heights), len(heights[0])
        efforts = [[10**6] * ncol for _ in range(nrow)]
        efforts[0][0] = 0
        pq = [(0, 0, 0)]
        while pq:
            effort, r, c = heapq.heappop(pq)
            if (r, c) == (nrow - 1, ncol - 1): return effort
            
            for rr, cc in [(r + 1, c), (r - 1, c), (r, c - 1), (r, c + 1)]:
                if not (0 <= rr < nrow and 0 <= cc < ncol): continue
                next_effort = max(effort, abs(heights[rr][cc] - heights[r][c]))
                if efforts[rr][cc] > next_effort:
                    efforts[rr][cc] = next_effort
                    heapq.heappush(pq, (next_effort, rr, cc))
