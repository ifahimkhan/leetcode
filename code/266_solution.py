class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        counts = Counter(s)
        num_odd = 0
        for k, v in counts.items():
            if v & 1: 
                num_odd += 1
                if num_odd > 1: return False
        return True
