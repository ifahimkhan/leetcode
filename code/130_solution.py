class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board: return board
        nrow, ncol = len(board), len(board[0])
        safe = set()
        
        def mark_safe(r, c):
            stack = [(r,c)]
            while stack:
                r, c = stack.pop()
                if (r, c) in safe: continue
                safe.add((r, c))
                for rr, cc in [(r-1,c), (r+1,c), (r,c-1), (r,c+1)]:
                    if 0 <= rr < nrow and 0 <= cc < ncol and board[rr][cc] == 'O':
                        stack.append((rr, cc))
        
        # marking
        for r in range(nrow):
            for c in [0, ncol - 1]:
                if board[r][c] == 'O' and (r, c) not in safe: mark_safe(r, c)
                
        for c in range(1, ncol - 1):
            for r in [0, nrow - 1]:
                if board[r][c] == 'O' and (r, c) not in safe: mark_safe(r, c)
        # flipping
        for r in range(nrow):
            for c in range(ncol):
                if board[r][c] == 'O' and (r, c) not in safe: board[r][c] = 'X'