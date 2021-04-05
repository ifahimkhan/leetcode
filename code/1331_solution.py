class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank = {val: i for i, val in enumerate(sorted(set(arr)), 1)}
        return [rank[val] for val in arr]
