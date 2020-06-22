class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        ref_l, ref_r = toBeRemoved
        results = []
        for l, r in intervals:
            if l < ref_l: results.append([l, min(r, ref_l)])
            if r > ref_r: results.append([max(l, ref_r), r])
        return results
