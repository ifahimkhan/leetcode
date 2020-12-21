class Solution:
    def smallestRangeII(self, A: List[int], K: int) -> int:
        # +-K to min max is equivalent to +- 0 and 2K to min max
        # sort makes things easier
        A.sort()
        min_range = A[~0] - A[0] 
        for i in range(len(A) - 1):
            large = max(A[~0], A[i] + 2 * K)
            small = min(A[i + 1], A[0] + 2 * K)
            min_range = min(min_range, large - small)
        return min_range
