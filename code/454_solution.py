class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        # cnt = 0
        # m = dict()
        
        # # freq count of sums of all pairs between A, B 
        # for a in A:
        #     for b in B:
        #         m[a + b] = m.get(a + b, 0) + 1
        
        # # check all all pairs between C, D to see if they sum up to complement to a value in m
        # for c in C:
        #     for d in D:
        #         cnt += m.get(-(c + d), 0)
        # return cnt
        return self.kSumCount([A, B, C, D], 0)
        
        
    def kSumCount(self, arrays, target=0):
        k = len(arrays)
        self.cnt = 0
        m = dict()
        
        def freq_count(i, accum):
            if i == k // 2: 
                m[accum] = m.get(accum, 0)  + 1
            else:
                for num in arrays[i]:
                    freq_count(i + 1, accum + num)
            
        freq_count(0, 0)
        
        def check_complement(i, accum):
            if i == k:
                self.cnt += m.get(target - accum, 0)
            else:
                for num in arrays[i]:
                    check_complement(i + 1, accum + num)
        
        check_complement(k // 2, 0)
        return self.cnt
        
