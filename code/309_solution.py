class Solution:
    def maxProfit(self, prices: List[int]) -> int:
            #   HOLD[i] = MAX(HOLD[i-1], REST[i-1] - PRICE[i])
            #   SOLD[i] = HOLD[i-1] + PRICE[i]
            #   REST[i] = MAX(REST[i-1], SOLD[i-1]) 
        dp = [[float('-inf'), -1, 0]]
        for price in prices:
            last_hold, last_sold, last_rest = dp[-1]
            hold = max(last_hold, last_rest - price)
            sold = last_hold + price
            rest = max(last_rest, last_sold)
            dp.append([hold, sold, rest])
        return max(dp[-1])
            