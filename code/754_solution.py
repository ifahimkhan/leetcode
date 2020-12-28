class Solution:
    def reachNumber(self, target: int) -> int:
        target = target if target > 0 else - target
        k = 0
        while target > 0:
            k += 1
            target -= k
            
        if target % 2 == 0: return k
        
        return k + 1 + k % 2
