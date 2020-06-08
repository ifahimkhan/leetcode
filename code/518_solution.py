# f(amt, options) = f(amt, options.popfront()) + f(amt - options[0], options)

# f(0, xx) = 1
# f(amt >0, {}) = 0
# f(amt <0, xx) = 0

class Solution:    
    def change(self, amount: int, coins: List[int]) -> int:
#         @lru_cache(maxsize=None)
#         def make_change(amount, i):
#             if amount == 0: return 1
#             if i == len(coins) or amount < 0: return 0
#             return make_change(amount, i+1) + make_change(amount - coins[i], i)
#         return make_change(amount, 0)
        
        dp = [1] + [0] * amount
        for coin in coins:
            for i in range(amount+1):
                if i + coin > amount: break
                dp[i+coin] += dp[i]
        return dp[-1]        
