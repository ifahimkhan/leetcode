class Solution:
    def solution_all_pairs(self, A, K):
        n = len(A)
        S = -1
        for i in range(n):
            for j in range(i):
                t = A[i] + A[j]
                if t < K: 
                    S = max(S, t)
        return S
    
    def solution_sort(self, A, K):
        n = len(A)
        S = -1
        A.sort()
        l, r = 0, n - 1
        while l < r:
            t = A[l] + A[r]
            if t < K:
                S = max(S, t)
                l += 1
            else:
                r -= 1
        return S
    
    twoSumLessThanK = solution_sort # solution_all_pairs
