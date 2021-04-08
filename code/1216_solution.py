class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        return len(s) - self.longestPalindromeSubseq(s) <= k
        
    def longestPalindromeSubseq(self, s):
        # from 516
        n = len(s)
        prev = [0] * n
        for r in range(n):
            curr = [0] * n
            curr[r] = 1
            for l in range(r-1, -1, -1):
                if s[l] == s[r]:
                    curr[l] = 2 + prev[l+1]
                else:
                    curr[l] = max(curr[l+1], prev[l])
            prev = curr
        return curr[0]
        
