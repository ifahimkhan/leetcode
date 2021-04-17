class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        nrow, ncol = len(matrix), len(matrix[0])

        for r in range(nrow):
            for c in range(1, ncol):
                matrix[r][c] += matrix[r][c-1]
                
        total = 0
        
        for y1 in range(ncol):
            for y2 in range(y1, ncol):
                accumulation = {0: 1}
                area = 0
                for x in range(nrow):
                    area += matrix[x][y2]
                    if y1 > 0: area -= matrix[x][y1-1]
                    total += accumulation.get(area - target, 0)
                    accumulation[area] = accumulation.get(area, 0) + 1
        
        return total
