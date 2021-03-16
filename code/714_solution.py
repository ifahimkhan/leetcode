class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        sold, hold = [0] * n, [0] * n
        hold[0] = -prices[0]
        for i in range(1, n):
            sold[i] = max(sold[i - 1], hold[i - 1] + prices[i] - fee)
            hold[i] = max(hold[i - 1], sold[i - 1] - prices[i])
        print(sold, hold)
        return sold[~0]
