class Solution:
    def knightDialer(self, n: int) -> int:
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
            dp = ndp
        return sum(dp.values()) % (10 ** 9 + 7)
