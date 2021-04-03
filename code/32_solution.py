class Solution:
    def solution_stack(self, s: str) -> int:
        stack = [-1]
        max_length = 0

        for i, char in enumerate(s):
            if char == ')':
                stack.pop()
                if stack:
                    max_length = max(max_length, i - stack[-1])
                    continue
            stack.append(i)            
            
        return max_length
    
    def solution_linear_scans(self, s: str) -> int:
        def scan(s, symbol):
            max_length = 0
            curr_length = 0
            to_match = 0
            for r, char in enumerate(s):
                if char == symbol:
                    to_match += 1
                    curr_length += 1
                else:
                    to_match -= 1
                    curr_length += 1
                    if to_match == 0:
                        max_length = max(max_length, curr_length)
                    if to_match < 0:
                        to_match = 0
                        curr_length = 0
            return max_length


        l_max = scan(s, '(')
        r_max = scan(reversed(s), ')')
        return max(l_max, r_max)    

    def solution_dp(self, s: str) -> int:
        n = len(s)
        dp = [0] * n
        
        for i in range(1, n):
            if s[i] == ')':
                if s[i - 1] == '(':
                    dp[i] = dp[i - 2] + 2
                elif i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == '(':
                    dp[i] = dp[i - 1] + dp[i - dp[i - 1] - 2] + 2
        return max(dp) if dp else 0    
    
    longestValidParentheses = solution_stack
