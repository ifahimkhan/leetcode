class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        i, j = 0, len(A) - 1
        while i < j:
            while i < len(A) and not A[i] % 2: i += 1
            while j >= 0 and A[j] % 2: j -= 1
            if i < j: A[i], A[j] = A[j], A[i]
        return A
                
