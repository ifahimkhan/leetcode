# How many distinct ways can you climb to the top?
# How many distinct ways can you climb to the xth step? f(x)
# f(x) = f(x-1) + f(x-2) 

class Solution:
    def bottom_up(self, n: int) -> int:
        slow, fast = 1, 1 # f_0, f_1
        for i in range(1, n):
            slow, fast = fast, slow + fast
        return fast
    
    def topdown(self, n):
        @lru_cache(None)
        def f(x):
            if x <= 3: return x
            return f(x-1) + f(x-2)
        return f(n)
    
    climbStairs = bottom_up # topdown