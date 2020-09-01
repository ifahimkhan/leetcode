class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        candidates = []
        for a,b,c,d in permutations(A, 4):
            h = a * 10 + b
            m = c * 10 + d
            if h < 24 and m < 60: candidates.append([h, m])
        return '' if not candidates else '{:02d}:{:02d}'.format(*max(candidates))
