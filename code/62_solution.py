# in total we need to move m-1(from top to bottom) + n-1(from left to right) steps 
# the question is basically choose m-1 out of (m-1+n-1)
# C_{m+n-2}^{m-1} = (m+n-2)! // (m-1)! // (n-1)!

# f(m,n) = f(m-1,n) + f(m, n-1)
# f(0,j) = 1
# f(i,0) = 1


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # O(M+N) , O(1)
        # div1 = div2 = curr = 1
        # for i in range(1, m+n-1):
        #     curr *= i
        #     if i == m - 1: div1 = curr
        #     if i == n - 1: div2 = curr
        # return curr // div1 // div2
        
        dp = [1] * n
        # O(MN) TIME, O(MIN(M,N))
        for row in range(1, m): 
            for col in range(1, n):
                dp[col] = dp[col] + dp[col-1]
        return dp[-1]
