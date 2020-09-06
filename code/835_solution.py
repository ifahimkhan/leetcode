class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        n = len(A)
        
        def shift_overlap(A, dx, dy, B):
            total = 0
            for rb, ra in enumerate(range(dy, n)):
                for cb, ca in enumerate(range(dx, n)):
                    total += A[ra][ca] * B[rb][cb]
            return total
        
        max_overlaps = 0
        for dy in range(n):
            for dx in range(n):
                max_overlaps = max(
                    max_overlaps,
                    shift_overlap(A, dx, dy, B),
                    shift_overlap(B, dx, dy, A)
                )
                
        return max_overlaps
