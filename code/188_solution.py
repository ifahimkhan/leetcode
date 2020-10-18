class Solution:
    @staticmethod
    def _grab_all_profits(prices):
        profit = 0
        for p1, p2 in zip(prices, prices[1:]):
            profit += max(0, p2 - p1)
        return profit        
    
    def solution_bottom_up(self, k, prices):
        n = len(prices)
        
        if k * 2 > n: return self._grab_all_profits(prices)
        
        dp = [0] * n
        # tabulation
        for j in range(k):
            profit = 0
            for i in range(1, n):
                profit = max(profit + prices[i] - prices[i - 1], dp[i])
                dp[i] = max(dp[i-1], profit)
    
        return dp[-1]        
        
    def solution_top_down(self, k, prices):
        n = len(prices)
        
        if k * 2 > n: return self._grab_all_profits(prices)

        memo = dict()
        def dfs(i, k, buy):
            # base case
            if (i >= len(prices)) or (k == 0 and buy): return 0
            
            # transition function
            if memo.get((i, k, buy), 0) == 0:
                 memo[(i, k, buy)] = max(
                    dfs(i + 1, k, buy),
                    dfs(i + 1, k - buy, 1 - buy) + prices[i] * (-1 if buy else 1)
                )
            return memo[(i, k, buy)]
        
        return dfs(0, k, 1)
    
    maxProfit = solution_bottom_up # solution_top_down
