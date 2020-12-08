class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        ranges = []
        for l, r in zip([lower - 1] + nums, nums + [upper + 1]):
            if l == r - 2: ranges.append(str(l + 1))
            if l < r - 2: ranges.append('{}->{}'.format(l + 1, r - 1))
        return ranges
