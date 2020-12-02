class Solution:
    def totalNQueens(self, n: int) -> int:
        rows = [0] * n
        hills = [0] * (2 * n - 1) 
        dales = [0] * (2 * n - 1) 
        
        def backtrack(r, num_queens):
            for c in range(n):
                if rows[c] or hills[r - c] or dales[r + c]: continue
                rows[c] = hills[r - c] = dales[r +  c] = 1                
                num_queens = num_queens + 1 if r == n - 1 else backtrack(r + 1, num_queens)
                rows[c] = hills[r - c] = dales[r +  c] = 0                
            return num_queens                
            
        return backtrack(0, 0)
