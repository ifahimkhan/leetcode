class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        
        char_freqs = Counter(s)
        for c in t:
            if not char_freqs.get(c, 0): return False
            char_freqs[c] -= 1
        return True
