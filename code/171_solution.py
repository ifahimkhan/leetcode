class Solution:
    def titleToNumber(self, s: str) -> int:
        # total = 0
        # for loc, d in enumerate(reversed(s)):
        #     total += (ord(d) - 64) * 26 ** loc
        # return total
        return sum((ord(d) - 64) * 26 ** loc for loc, d in enumerate(reversed(s)))