class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """ Do not return anything, modify board in-place instead. """
        # two pass the board, one pass marking, second pass finalize. 
        #
        # states: 
        # 0 dead | undetermined or will be dead
        # 1 live | undetermined or will be live
        # 2 dead |                 will be live
        # 3 live |                 will be dead
        #
        # => state & 1 tells whether the cell is a live cell in previous state
        #    state in [1, 2] tells whether the cell should live in next state
        nrow, ncol = len(board), len(board[0])
        
        def count_living_neighbors(r, c):
            count = 0
            for nr, nc in [(r + 1, c), (r - 1, c), (r + 1, c + 1), (r + 1, c - 1),
                           (r, c - 1), (r, c + 1), (r - 1, c + 1), (r - 1, c - 1)]:
                if 0 <= nr < nrow and 0 <= nc < ncol: 
                    count += board[nr][nc] & 1
            return count
        
        for r in range(nrow):
            for c in range(ncol):
                living_neighbors = count_living_neighbors(r, c)
                
                if board[r][c] == 1: # rule 2 is no change
                    if living_neighbors < 2: board[r][c] = 3 # rule 1
                    if living_neighbors > 3: board[r][c] = 3 # rule 3
                else: 
                    if living_neighbors == 3: board[r][c] = 2 # rule 4
        
        for r in range(nrow):
            for c in range(ncol):
                board[r][c] = 1 if board[r][c] in [1, 2] else 0
