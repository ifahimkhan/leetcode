class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        even_odd = [0, 0]
        for position in position:
            even_odd[position % 2] += 1
        return min(even_odd)
