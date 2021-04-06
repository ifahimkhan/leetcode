class Solution:
    def solution_hash_by_shift_normalization(self, grid: List[List[int]]) -> int:
        nrow, ncol = len(grid), len(grid[0])
        distinct_islands = set()
        visited = set()
        
        def dfs(r, c):
            rr, cc = r, c
            island = []
            stack = [(r, c)]
            while stack:
                r, c = stack.pop()
                visited.add((r, c))
                island.append((r - rr, c - cc))
                for nr, nc in [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]:
                    if 0 <= nr < nrow and 0 <= nc < ncol and grid[nr][nc] and (nr, nc) not in visited:
                        stack.append((nr, nc))
            return ''.join(['{},{}'.format(r, c) for r, c in island])
        
        for r in range(nrow):
            for c in range(ncol):
                if grid[r][c] and (r, c) not in visited:
                    island = dfs(r, c)
                    distinct_islands.add(island)

        return len(distinct_islands)
    
    def solution_hash_by_path(self, grid: List[List[int]]) -> int:
        nrow, ncol = len(grid), len(grid[0])
        island_signatures = set()
        visited = set()

        def dfs(r, c):
            signature = []
            stack = [(r, c, 'O')]
            while stack:
                r, c, m = stack.pop()
                if m == '0':
                    signature.append(m)
                    continue
                visited.add((r, c))
                signature.append(m)
                stack.append((-1, -1, '0'))  # very crucial to have this indicating braching started. 
                for (nr, nc), m in zip([(r-1,c),(r+1,c),(r,c-1),(r,c+1)], 'UDLR'):
                    if 0 <= nr < nrow and 0 <= nc < ncol and grid[nr][nc] and (nr, nc) not in visited:
                        stack.append((nr, nc, m))
            return tuple(signature)
        
        for r in range(nrow):
            for c in range(ncol):
                if grid[r][c] and (r, c) not in visited:
                    island_signatures.add(dfs(r, c))
        print(island_signatures)
    
    numDistinctIslands = solution_hash_by_path # solution_hash_by_shift_normalization
