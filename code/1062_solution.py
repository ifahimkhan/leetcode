# 1044?
class Solution:
    def longestRepeatingSubstring(self, S: str) -> int:
        A = [ord(char) - ord('a') for char in S]
        P = 26
        MOD = 2 ** 32

        def find(L):
            h = 0
            for c in A[:L]: h = h * P + c
            seen = {h % MOD}

            PP = P ** L % MOD
            for i, c in enumerate(A[L:], L):
                h = (h * P - A[i - L] * PP + c) % MOD
                if h in seen: return True
                seen.add(h)
            return False

        l, h = 1, len(S)
        while l <= h:
            m = (l + h) // 2
            if find(m):
                l = m + 1
            else:
                h = m - 1
        return l - 1
        
        
        
