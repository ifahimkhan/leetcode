class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        dp = [0] * n
        dp[0] = min(costs)
        for i in range(1, n):
            dp[i] = dp[i - 1] + costs[0] 
            j = i
            for duration, cost in zip((7, 30), costs[1:]):
                while j >= 0 and days[j] + duration > days[i]: j -= 1
                dp[i] = min(dp[i], (j >= 0) * dp[j] + cost)
        return dp[-1]
