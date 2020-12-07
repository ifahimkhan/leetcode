class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        A = [[0] * n for _ in range(n)]
        r, c = 0, 0 
        dr, dc = 0, 1  
        
        for v in range(1, n * n + 1):
            A[r][c] = v
            # oob (x + dx) == n or met values already filled
            if A[(r + dr) % n][(c + dc) % n]: 
                # (0, 1) right -> (1, 0) down -> (0, -1) left -> (-1, 0) up
                dr, dc = dc, -dr 
            r, c = r + dr, c + dc
        return A
