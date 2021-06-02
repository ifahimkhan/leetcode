class Solution:    
    def solution_topdown(self, s1: str, s2: str, s3: str) -> bool:
        l1, l2, l3 = list(map(len, [s1, s2, s3]))
        if l1 + l2 != l3: return False
        
        @lru_cache(maxsize=None)
        def backtrack(i1, i2):
            if i1 == l1 and i2 == l2: return True
            if i1 < l1 and s1[i1] == s3[i1 + i2] and backtrack(i1+1, i2): return True
            if i2 < l2 and s2[i2] == s3[i1 + i2] and backtrack(i1, i2+1): return True
            return False
        
        return backtrack(0, 0)

    def solution_bottomup_2d(self, s1: str, s2: str, s3: str) -> bool:
        l1, l2, l3 = list(map(len, [s1, s2, s3]))
        if l1 + l2 != l3: return False
        
        dp = [[False] * (l2+1) for _ in range(l1+1)]
        
        for i1 in range(l1+1):
            for i2 in range(l2+1):
                if i1 == i2 == 0: dp[i1][i2] = True
                elif i1 == 0: dp[i1][i2] = dp[i1][i2-1] and s2[i2-1] == s3[i2-1]
                elif i2 == 0: dp[i1][i2] = dp[i1-1][i2] and s1[i1-1] == s3[i1-1]
                else: dp[i1][i2] = (dp[i1-1][i2] and s1[i1-1] == s3[i1+i2-1]) or \
                                   (dp[i1][i2-1] and s2[i2-1] == s3[i1+i2-1])
        return dp[-1][-1]
    
    
    def solution_bottomup_1d(self, s1: str, s2: str, s3: str) -> bool:
        l1, l2, l3 = list(map(len, [s1, s2, s3]))
        if l1 + l2 != l3: return False
        
        dp = [False] * (l2+1)
        for i1 in range(l1+1):
            for i2 in range(l2+1):
                if i1 == i2 == 0: dp[i2] = True
                elif i1 == 0: dp[i2] = dp[i2-1] and s2[i2-1] == s3[i2-1]
                elif i2 == 0: dp[i2] = dp[i2] and s1[i1-1] == s3[i1-1]
                else: dp[i2] = (dp[i2] and s1[i1-1] == s3[i1+i2-1]) or \
                               (dp[i2-1] and s2[i2-1] == s3[i1+i2-1])
        return dp[-1]
    
    isInterleave = solution_bottomup_1d # solution_bottomup_2d # solution_topdown
