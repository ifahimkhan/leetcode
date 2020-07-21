class Solution:
    def variant_1(self, grid: List[List[int]]) -> int:
        nrow, ncol = len(grid), len(grid[0])
        perimeter = 0 
        for r in range(nrow):
            for c in range(ncol):
                if grid[r][c]:
                    perimeter += 4
                    for nr, nc in [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]:
                        if 0 <= nr < nrow and 0 <= nc < ncol and grid[nr][nc]:
                            perimeter -= 1
        return perimeter

    def variant_2(self, grid: List[List[int]]) -> int:
        nrow, ncol = len(grid), len(grid[0])
        perimeter = 0 
        for r in range(nrow):
            for c in range(ncol):
                if grid[r][c]:
                    perimeter += 4
                    for nr, nc in [(r-1,c),(r,c-1)]:
                        if 0 <= nr < nrow and 0 <= nc < ncol and grid[nr][nc]:
                            perimeter -= 2
        return perimeter

    islandPerimeter = variant_2