class Solution:
    def longestPalindrome(self, s: str) -> int:
        length = 0
        has_odd = False
        counts = Counter(s)
        for v in counts.values():
            if v & 1: 
                length += v - 1
                has_odd = True
            else: 
                length += v
        if has_odd: length += 1
        return length
        