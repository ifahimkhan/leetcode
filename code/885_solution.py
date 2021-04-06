class Solution:
    def spiralMatrixIII(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        order = [(r0, c0)]
        r, c = r0, c0        
        i, steps = 0, 1
        while len(order) != R * C:
            for _ in range(2):
                dr, dc = directions[i % 4]
                i += 1
                for step in range(steps):
                    r, c = r + dr, c + dc
                    if 0 <= r < R and 0 <= c < C:
                        order.append((r, c))
            steps += 1
            
        return order
