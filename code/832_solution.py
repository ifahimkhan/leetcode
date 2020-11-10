class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        nrow, ncol = len(A), len(A[0])
        for i in range(nrow):
            l, r = 0, ncol - 1
            while l <= r:
                A[i][l], A[i][r] = 1 - A[i][r], 1 - A[i][l]
                l += 1
                r -= 1
        return A
