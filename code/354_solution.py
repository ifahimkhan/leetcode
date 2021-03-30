class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key = lambda x: (x[0], -x[1]))
        dolls = []
        for h, w in envelopes:
            i = bisect.bisect_left(dolls, w)
            if i == len(dolls): dolls.append(w)
            elif w < dolls[i]: dolls[i] = w
        return len(dolls)
                
