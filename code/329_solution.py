class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # edge case handle
        if not matrix or not matrix[0]: return 0

        # move set
        nrow, ncol = len(matrix), len(matrix[0])
        def get_neighbor(r, c):
            for nr, nc in [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]:
                if 0 <= nr < nrow and 0 <= nc < ncol:
                    yield nr, nc        

        # graph processing O(N) time and space
        out_edges = defaultdict(list) 
        in_degrees = defaultdict(int) 
        for r in range(nrow):
            for c in range(ncol):
                for nr, nc in get_neighbor(r, c):
                    if matrix[nr][nc] <= matrix[r][c]: continue
                    out_edges[(r,c)].append((nr, nc))
                    in_degrees[(nr, nc)] += 1            
                        
        # find the starting level O(N) time and space
        queue = deque([(r, c) for r in range(nrow) for c in range(ncol) if not in_degrees[(r, c)]])

        # bfs topological sort to count the number of levels O(N) time
        length = 0
        while queue:
            length += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                for nei in out_edges[node]:
                    in_degrees[nei] -= 1
                    if in_degrees[nei] == 0:
                        queue.append(nei)
        return length
                