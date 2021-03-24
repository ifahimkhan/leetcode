class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        AA = [-1] * n
        
        sorted_A = sorted(A, reverse=True)
        sorted_B = sorted(((b, j) for j, b in enumerate(B)), reverse=True)
        
        l, r = 0, n - 1
        for b, j in sorted_B:
            if l > r: break
            if sorted_A[l] > b:
                AA[j] = sorted_A[l]
                l += 1
            else:
                AA[j] = sorted_A[r]
                r -= 1

        return AA
