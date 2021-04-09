class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:

        def check_player(symbol):
            count, has_won = 0, False

            row_counts = [0] * 3
            col_counts = [0] * 3
            diag_counts = [0] * 2 
            
            for i in range(3):
                for j in range(3):
                    if board[i][j] != symbol: continue
                    count += 1
                    row_counts[i] += 1
                    col_counts[j] += 1
                    if i == j: diag_counts[0] += 1
                    if i + j == 2: diag_counts[1] += 1

            if 3 in row_counts or 3 in col_counts or 3 in diag_counts: has_won = True
            return count, has_won
                
        X_count, X_has_won = check_player('X')
        O_count, O_has_won = check_player('O')

        if X_has_won and O_has_won: return False
        if X_has_won: return X_count == O_count + 1
        if O_has_won: return X_count == O_count
        return (X_count - O_count) in [0, 1]
