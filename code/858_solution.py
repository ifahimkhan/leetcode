class Solution:
    def solution_sim(self, p, q):
        if p == q: return 1

        h, v = p, q
        while True:
            h, v = h + p, v + q
            if h % p == 0 and v % (2 * p) == 0: return 0
            if h % (2 * p) == 0 and (v - p) % (2 * p) == 0: return 2
            if (h - p) % (2 * p) == 0 and (v - p) % (2 * p) == 0: return 1
        
    def solution_math(self, p, q):
        while p % 2 == 0 and q % 2 == 0: 
            p, q = p / 2, q / 2
        
        if p % 2 and q % 2: return 1
        if p % 2: return 0
        if q % 2: return 2
    
    mirrorReflection = solution_math # solution_sim
