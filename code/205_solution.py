class Solution:
    def solution_1(self, s: str, t: str) -> bool:
        # One pass
        s_to_t = dict()
        t_to_s = dict()
        for ss, tt in zip(s, t):
            if ss not in s_to_t: s_to_t[ss] = tt
            if tt not in t_to_s: t_to_s[tt] = ss
            if s_to_t[ss] != tt: return False
            if t_to_s[tt] != ss: return False
        return True
    
    def solution_2(self, s, t):
        # more pythonic but three pass.
        combo = set((ss, tt) for ss, tt in zip(s, t))
        return len(combo) == len(set(s)) == len(set(t))
        
    isIsomorphic = solution_2