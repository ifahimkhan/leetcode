class Solution:
    def solution_window_hash(self, s, k=10):
        freq_counts = dict()
        for i in range(len(s) - k + 1):
            freq_counts[s[i:i+k]] = freq_counts.get(s[i:i+k], 0) + 1
        return [k for k, v in freq_counts.items() if v > 1]
    
    def solution_rolling_hash(self, s, k=10):
        if len(s) < k: return 
        p, pp = 4, 4**k
        to_int = {c:i for i, c in enumerate('ACGT')}
        
        code = 0
        for i in range(k):
            code = code * p + to_int[s[i]]
            
        seen, solutions = set([code]), set()
        
        for i in range(1, len(s) - k + 1):
            code = code * p - to_int[s[i-1]] * pp + to_int[s[i+k-1]]
            if code in seen:
                solutions.add(s[i:i+k])
            seen.add(code)
        return solutions
    
    findRepeatedDnaSequences = solution_rolling_hash # solution_window_hash
