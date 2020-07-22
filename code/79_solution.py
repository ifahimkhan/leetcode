class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # backtrack O(N*4^L) time, space O(L)
        nrow, ncol, n = len(board), len(board[0]), len(word)

        def backtrack(r, c, i):
            # finished
            if i == n: return True
            
            # determine if word[i] == grid[r][c]
            if 0 <= r < nrow and 0 <= c < ncol and board[r][c] == word[i]: 
                char = board[r][c]
                board[r][c] = ''
                # exame other choices
                for rr, cc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
                    if backtrack(rr, cc, i+1): return True
                board[r][c] = char
                
        for r in range(nrow):
            for c in range(ncol):
                if backtrack(r, c, 0): return True
        return False