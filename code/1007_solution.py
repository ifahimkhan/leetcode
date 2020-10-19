class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        n = len(A)
        # if there is a solution, we have a full row of either A[0] or B[0]
        # just check if either is possible
        for tatget in [A[0], B[0]]:
            rotate_a, rotate_b = 0, 0
            for i, (na, nb) in enumerate(zip(A, B)):
                if na != tatget and nb != tatget: break
                if na != tatget: rotate_a += 1
                if nb != tatget: rotate_b += 1
            else:
                return min(rotate_a, rotate_b)
        return -1
