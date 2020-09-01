class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """ Do not return anything, modify matrix in-place instead. """
        nrow, ncol = len(matrix), len(matrix[0])
        
        first_row_zero = any(matrix[0][c] == 0 for c in range(ncol))
        first_col_zero = any(matrix[r][0] == 0 for r in range(nrow))
        
        for r in range(1, nrow):
            for c in range(1, ncol):
                if matrix[r][c] == 0:
                    matrix[r][0], matrix[0][c] = 0, 0
        
        for r in range(1, nrow):
            for c in range(1, ncol):
                if matrix[r][0] == 0 or matrix[0][c] == 0: 
                    matrix[r][c] = 0

        if first_row_zero:
            for c in range(ncol): 
                matrix[0][c] = 0
        
        if first_col_zero:
            for r in range(nrow): 
                matrix[r][0] = 0
