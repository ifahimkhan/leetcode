class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals: return [newInterval]
        if not newInterval: return intervals
        nl, nr = newInterval
        n = len(intervals)

        if intervals[-1][1] < nl: return intervals + [newInterval]
        if intervals[0][0] > nr: return [newInterval] + intervals

        def intersect(l1, r1, l2, r2):
            l = max(l1, l2)
            r = min(r1, r2)
            return l <= r

        output, l, r = [], None, None
        for i, (il, ir) in enumerate(intervals):
            if intersect(il, ir, nl, nr):
                if l is None: l = min(il, nl)
                if r is None: r = max(ir, nr)
                l = min(l, il)
                r = max(r, ir)
            else:
                if r:
                    output.append([l, r])
                    l, r = None, None
                if i and intervals[i - 1][1] < nl and nr < il:
                    output.append(newInterval)
                output.append([il, ir])
        if r: output.append([l, r])
        return output
