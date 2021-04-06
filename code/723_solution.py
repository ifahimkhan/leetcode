class Solution:
    def __init__(self):
        self.to_crush = set()
        
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        nrow, ncol = len(board), len(board[0])
        
        def annotate(r, c):
            if 0 <= r - 1 and r + 1 < nrow:
                if board[r-1][c] == board[r][c] == board[r+1][c]: 
                    self.to_crush.update([(r-1, c), (r, c), (r+1,c)])
            if 0 <= c - 1 and c + 1 < ncol:
                if board[r][c-1] == board[r][c] == board[r][c+1]: 
                    self.to_crush.update([(r, c-1), (r, c), (r,c+1)])
        
        def crush():
            for r, c in self.to_crush:
                board[r][c] = 0
            self.to_crush.clear()
        
        def search():
            self.to_crush.clear()
            for r in range(nrow):
                for c in range(ncol):
                    if board[r][c] == 0: continue
                    annotate(r, c)
            return len(self.to_crush)
        
        def drop():
            for c in range(ncol):
                column_values = [board[r][c] for r in range(nrow-1, -1, -1) if board[r][c]]
                column_values += [0] * (nrow - len(column_values))
                r = nrow - 1
                for val in column_values:
                    board[r][c] = val
                    r -= 1
        
        while search():
            crush()
            drop()
        
        return board
            
