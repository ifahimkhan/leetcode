# f(i,j) = min edit distance between word1[0:i) and word2[0:j)
# f(len(word1),len(word2)) would be our solution
                                                        
# f(i,j) = min of options of four
#          f(i-1,j) + 1 # delete from word1
#          f(i,j-1) + 1 # insert to word1                                                    
#          f(i-1,j-1)   # if tail at both are the same
#          f(i-1,j-1) + 1 # if tail not same, need 1 replacement                                               
# basecase
# f(i,j) = max(i,j) if i==0 or j==0

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1, n2 = len(word1), len(word2)
        dp = list(range(n2+1))
        for r, char1 in enumerate(word1, 1):
            ndp = [r] + [0] * n2
            for c, char2 in enumerate(word2, 1):
                ndp[c] = min(
                    dp[c] + 1,
                    ndp[c-1] + 1,
                    dp[c-1] + int(char1 != char2)
                )
            dp = ndp
        return dp[-1]