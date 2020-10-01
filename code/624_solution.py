class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        minimal, maximum = arrays[0][0], arrays[0][~0]
        max_diff = 0
        for arr in arrays[1:]:
            s, e = arr[0], arr[~0]
            max_diff = max(max_diff, abs(maximum - s), abs(e - minimal))
            minimal = min(minimal, s)
            maximum = max(maximum, e)
        return max_diff
