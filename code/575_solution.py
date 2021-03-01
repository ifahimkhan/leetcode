class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        n_total = len(candyType)
        n_unique = len(set(candyType))
        return n_total // 2 if n_unique >= n_total / 2 else n_unique
