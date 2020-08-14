class Solution:
    def longestPalindrome(self, s: str) -> int:
        length, has_odd = 0, 0
        for v in Counter(s).values():
            if v & 1: 
                has_odd = 1
                v -= 1
            length += v
        return length + has_odd
        