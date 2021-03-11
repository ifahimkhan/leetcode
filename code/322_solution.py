class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        min_coin = min(coins)
        dp = [0] + [float('inf')] * amount
        for amt in range(amount + 1):
            if amt < min_coin: continue
            dp[amt] = min({dp[amt - c] for c in coins if amt >= c}) + 1
        return dp[amount] if dp[amount] != float('inf') else -1
