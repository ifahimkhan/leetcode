class MaxPriorityQueue(object):
    def __init__(self):
        self.container = []
    
    def push(self, x):
        heapq.heappush(self.container, (-x[0], x[1]))
    
    def pop(self):
        x, (r, c) = heapq.heappop(self.container)
        return -x, (r, c)
        

class Solution:
    def solution_pq(self, A):
        nrow, ncol = len(A), len(A[0])
        pq = MaxPriorityQueue()
        pq.push((A[0][0], (0, 0)))
        discovered = [[0] * ncol for _ in range(nrow)]
        discovered[0][0] = 1
        while pq:
            path_min, (r, c) = pq.pop()
            if (r, c) == (nrow - 1, ncol - 1): return path_min
            
            for nr, nc in ((r-1, c), (r+1,c), (r,c-1), (r,c+1)):
                if 0 <= nr < nrow and 0 <= nc < ncol and not discovered[nr][nc]:
                    discovered[nr][nc] = 1
                    pq.push((min(A[nr][nc], path_min), (nr, nc)))
        return -1
    
    maximumMinimumPath = solution_pq
