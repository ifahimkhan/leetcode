# 1 + 2 + ... + k <= n
# k * (k + 1) / 2 <= n
# k^2 + k + 1/4 - 1/4 <= 2n
# (k+1/2)^2 <= 2n + 1/4
# k + 1/2 <= sqrt(2n + 1/4)
# k = floor( sqrt(2n+1/4) - 1/2)

class Solution:
    def arrangeCoins(self, n: int) -> int:
        return int((2*n + 1/4) ** .5 - 1/2)