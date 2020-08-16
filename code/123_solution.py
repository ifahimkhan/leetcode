INT_MIN = - 2 ** 32


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_1, buy_2, sell_1, sell_2 = INT_MIN, INT_MIN, 0, 0
        for price in prices:
            buy_1 = max(buy_1, -price)
            sell_1 = max(sell_1, buy_1 + price)
            buy_2 = max(buy_2, sell_1 - price)
            sell_2 = max(sell_2, buy_2 + price)
        return sell_2