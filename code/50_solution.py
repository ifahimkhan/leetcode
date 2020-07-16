# 2^10 = 1*2*2*2*2*2*2*2*2*2*2 = 1*2^(1+1+1...+1)
#                              = 1*2^(2+8)

# 2^10 = 1* 2^2 * 2^8 

#                8 4 2 1
# bin(10)        1 0 1 0

# 2^(-2) = 2^(-1*2) = (2^-1)*2

class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if n < 0:
            x = 1 / x
            n = - n
            
        accum, p = 1, x
        while n:
            if n & 1: accum *= p
            p *= p
            n >>= 1
        return accum
