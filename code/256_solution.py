class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        curr = costs[0]
        
        for r, b, g in costs[1:]:
            pr, pb, pg = curr
            curr = [min(pb + r, pg + r), min(pr + b, pg + b), min(pr + g, pb + g)]
            
        return min(curr)
