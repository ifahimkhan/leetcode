class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix: return []
        
        nrow, ncol = len(matrix), len(matrix[0])
        reachable_from_p = [[False] * ncol for _ in range(nrow)]
        reachable_from_a = [[False] * ncol for _ in range(nrow)]
        
        def dfs(r, c, reachable_from):
            reachable_from[r][c] = True
            for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                if not (0 <= nr < nrow and 0 <= nc < ncol): continue
                if reachable_from[nr][nc]: continue
                if matrix[nr][nc] >= matrix[r][c]:
                    dfs(nr, nc, reachable_from)
                    
        for r in range(nrow):
            dfs(r, 0, reachable_from_p)
            dfs(r, ncol - 1, reachable_from_a)
        
        for c in range(ncol):
            dfs(0, c, reachable_from_p)
            dfs(nrow - 1, c, reachable_from_a)
        
        reachable_from_both = [(r, c) for r in range(nrow) 
                                      for c in range(ncol) 
                                      if reachable_from_p[r][c] and reachable_from_a[r][c]
                              ]
        return reachable_from_both
