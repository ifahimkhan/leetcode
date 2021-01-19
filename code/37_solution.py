class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        digits = set('123456789')
        not_visited = [(r, c) for r in range(9) for c in range(9) if board[r][c] == '.']

        def valid_choices(r, c):
            row = board[r]
            col = [board[i][c] for i in range(9)]
            square = [board[i][j] for i in range(r // 3 * 3, r // 3 * 3 + 3)
                                  for j in range(c // 3 * 3, c // 3 * 3 + 3)]
            choices = digits.difference(row).difference(col).difference(square)
            return choices

        def backtrack(board, not_visited):
            if not not_visited: return True
            (r, c) = not_visited.pop()
            for digit in valid_choices(r, c):
                board[r][c] = digit
                if backtrack(board, not_visited): return True
                board[r][c] = '.'
            not_visited.append((r, c))
            return False

        backtrack(board, not_visited)
