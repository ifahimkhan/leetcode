class Solution:
    def largestUniqueNumber(self, A: List[int]) -> int:
        freq_counts = Counter(A)
        for i in range(1000, -1, -1):
            if freq_counts[i] == 1: 
                return i
        return -1
