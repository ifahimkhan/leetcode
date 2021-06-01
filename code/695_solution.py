class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        max_area = 0
        nrow, ncol = len(grid), len(grid[0])
        
        def dfs(r, c):
            area = 0
            stack = [(r, c)]
            visited.add((r, c))
            while stack:
                r, c = stack.pop()
                area += 1
                for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                    if 0 <= nr < nrow and 0 <= nc < ncol and grid[nr][nc] and (nr, nc) not in visited:
                        stack.append((nr, nc))
                        visited.add((nr, nc))
            return area
        
        
        for r in range(nrow):
            for c in range(ncol):
                if grid[r][c] and (r, c) not in visited:
                    max_area = max(max_area, dfs(r, c))
        return max_area
        
