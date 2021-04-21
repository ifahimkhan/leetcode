MOD = 10 ** 9 + 7
import numpy as np

class Solution:
    def solution_dp(self, n: int) -> int:
        jumps = {
            0: (4, 6),
            1: (6, 8),
            2: (7, 9),
            3: (4, 8),
            4: (3, 9, 0),
            5: (),
            6: (1, 7, 0),
            7: (2, 6),
            8: (1, 3),
            9: (2, 4)
        }
        dp = {i: 1 for i in range(10)}
        
        for i in range(1, n):
            ndp = defaultdict(int)
            for k, v in dp.items():
                for target in jumps[k]:
                    ndp[target] += v
            for k in ndp:
                ndp[k] = ndp[k] % MOD
            dp = ndp
        return sum(dp.values()) % MOD

    def solution_matrix_power(self, n):
        if n == 1: return 10
        
        M = np.matrix([
            # 0 1 2 3 4 5 6 7 8 9
             [0,0,0,0,1,0,1,0,0,0],
             [0,0,0,0,0,0,1,0,1,0],
             [0,0,0,0,0,0,0,1,0,1],
             [0,0,0,0,1,0,0,0,1,0],
             [1,0,0,1,0,0,0,0,0,1],
             [0,0,0,0,0,0,0,0,0,0],
             [1,1,0,0,0,0,0,1,0,0],
             [0,0,1,0,0,0,1,0,0,0],
             [0,1,0,1,0,0,0,0,0,0],
             [0,0,1,0,1,0,0,0,0,0]
        ])
        dp, N = 1, n - 1
        while N:
            if N % 2: dp = dp * M % MOD
            M = M * M % MOD
            N //= 2
        return int(np.sum(dp)) % MOD
    
    knightDialer = solution_matrix_power # solution_dp
            
