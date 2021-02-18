class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        if len(A) <= 2: return 0
        total = strike = 0
        delta = None
        for n1, n2 in zip(A, A[1:]):
            if n2 - n1 == delta: 
                strike += 1
            else:
                total += strike * (strike - 1) // 2
                strike = 1
                delta = n2 - n1
                
        total += strike * (strike - 1) // 2
        return total
