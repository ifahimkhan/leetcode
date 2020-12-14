class Solution:
    
    @staticmethod
    def is_palindrome(s):
        return s == s[::-1]

    def solution_backtrack(self, s):
        # O(N) aux space, O(N*2^N) time bruteforce all options
        n = len(s)
        solutions = []
        
        
        def backtrack(candidate, i):
            if i == n: solutions.append(candidate.copy())
            for j in range(i + 1, n + 1):
                ss = s[i:j]
                if self.is_palindrome(ss):
                    candidate.append(ss)
                    backtrack(candidate, j)
                    candidate.pop()
                    
        backtrack([], 0)
        return solutions
    
    def solution_dp(self, s):
        # trade space for a bit speed. 
        n = len(s)
        dp = [[] for _ in range(n)] + [[[]]]
        
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n + 1):
                ss = s[i:j]
                if self.is_palindrome(ss):
                    for rest in dp[j]:
                        dp[i].append([ss] + rest)
        return dp[0]
    
    
    partition = solution_dp # solution_backtrack
