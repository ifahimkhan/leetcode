# f(i,j) = min heath required to save pricess if spawn at (i, j)
# f(0,0) is our answer 

# dungeon               f(ij)
#     0    1   2           0  1  2
#     ------------ 
# 0 | -2 	-3	3       0     
# 1 | -5	-10	1       1     ?  5
# 2 | 10	30	-5      2     1  6  
                                 
# f(2,2) = 6
# f(1,2) = max(1, x from x + 1 >= 6 f(2,2)) = 5
# f(2,1) = max(1, x from x + 30  >= 6 (2,2)) = 1
# f(1,1) = max(1, x from x - 10 >= min(f(1,2), f(2,1)))

# f(i,j) = max(1, x from x + dungeon[i][j] >= min(f(i,j+1), f(i+1,j)))

INT_MAX = 2 ** 32

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        nrow, ncol = len(dungeon), len(dungeon[0])
        hp = [[INT_MAX] * (ncol + 1) for _ in range(nrow + 1)]
        for r in range(nrow-1,-1,-1):
            for c in range(ncol-1,-1,-1):
                # basecase
                if r == nrow - 1 and c == ncol - 1: 
                    hp[r][c] = max(1, 1 - dungeon[-1][-1])
                else: 
                    hp[r][c] = max(1, min(hp[r][c+1], hp[r+1][c]) - dungeon[r][c])
        return hp[0][0]
        
        
        
        