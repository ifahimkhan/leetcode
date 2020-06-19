# #  012345
# # "banana"

# # F(L) = True, L=1  'a', 'n'
# # F(L) = True, L=2  'an', 'na'
# # F(L) = True, L=3  'ana' 1-3, 3-5
# # F(L) = False, L=4  'bana' 0-3, 'anan' 1-4, 'nana' 2-5

# # f(L) do we have duplicated substring of size L
# # 1. apply binary search to find the largest duplicated window size

# O(NL)
# 'bana' 0-3, 'anan' 1-4, 'nana' 2-5

# bana
#  anan

# on off on
# 1   0   1 -> 5
# off on on
# 0   1   1 -> 3

# 'bana'
#  a - 0
#  b - 1
#  n - 22
#  1 * 26 ^ 0 + 0 * 26 ^ 1 + 22 * 26 ^ 2 + 0 * 26 ^ 3

# 'anan'
#  0 * 26 ^ 0 + 22 * 26 ^ 1 + 0 * 26 ^ 2 + 22 * 26 ^3
    
class Solution:
    def longestDupSubstring(self, S: str) -> str:
        D = [ord(c) - ord('a') for c in S]
        P = 26
        MOD = 2 ** 32
        
        def rolling_hash(L):
            # initial window
            h = 0
            for c in D[:L]: h = (h * P + c) % MOD
            seen = {h}
            
            PP = P ** L % MOD
            # sliding window
            for r, c in enumerate(D[L:], L):
                # update window
                #  shift left    emit the old left    adding the new right    
                h = (h * P    -   D[r - L] * PP     +   c) % MOD
                if h in seen: return r - L + 1  # return start index for the duplicated window
                seen.add(h)
            return None
        
        # use binary search to find the max length of duplicated windows
        l, h = 0, len(S)
        while l < h:
            m = (l + h) // 2
            if rolling_hash(m): l = m + 1
            else: h = m
        start = rolling_hash(l-1)
        return S[start: start + l - 1]
